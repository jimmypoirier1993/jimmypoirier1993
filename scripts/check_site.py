#!/usr/bin/env python3
"""Contrôles statiques Paideia sans dépendance externe."""
import json, sys, xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
ROOT = Path(__file__).resolve().parents[1]
BASE = "https://paideiaeducation.ca"

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang, self.h1, self.title, self.desc, self.canonical = "", 0, 0, "", ""
        self.robots, self.ids, self.links = "", [], []
        self.labels, self.controls, self.schema = set(), set(), []
        self.in_schema = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang", "")
        if tag == "h1": self.h1 += 1
        if tag == "title": self.title += 1
        if a.get("id"): self.ids.append(a["id"])
        if tag == "meta" and a.get("name") == "description": self.desc = a.get("content", "")
        if tag == "meta" and a.get("name") == "robots": self.robots = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical": self.canonical = a.get("href", "")
        if tag in ("link", "a") and a.get("href"): self.links.append(a["href"])
        if tag == "script":
            if a.get("src"): self.links.append(a["src"])
            self.in_schema = a.get("type") == "application/ld+json"
            if self.in_schema: self.schema.append("")
        if tag == "label" and a.get("for"): self.labels.add(a["for"])
        if tag in ("input", "select", "textarea") and a.get("id"): self.controls.add(a["id"])
    def handle_data(self, data):
        if self.in_schema: self.schema[-1] += data
    def handle_endtag(self, tag):
        if tag == "script": self.in_schema = False

def url_for(path):
    name = path.relative_to(ROOT).as_posix()
    if name == "index.html": return BASE + "/"
    if name.endswith("/index.html"): return BASE + "/" + name[:-10]
    return BASE + "/" + name

def destination(source, href):
    u = urlsplit(href)
    if u.scheme or u.netloc or href.startswith("//"): return None
    target = ROOT / unquote(u.path.lstrip("/")) if u.path.startswith("/") else source.parent / unquote(u.path) if u.path else source
    target = target.resolve()
    if not target.is_relative_to(ROOT): return ("OUTSIDE", u.fragment)
    if target.is_dir() or u.path.endswith("/"): target = target / "index.html"
    return target, unquote(u.fragment)

def check():
    pages, errors = {}, []
    for path in sorted(ROOT.rglob("*.html")):
        doc = Page()
        doc.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = doc
        label = path.relative_to(ROOT).as_posix()
        if doc.lang != "fr-CA": errors.append(label + " : langue incorrecte")
        if doc.h1 != 1 or doc.title != 1: errors.append(label + " : H1 ou title manquant / dupliqué")
        if not doc.desc: errors.append(label + " : métadescription absente")
        if doc.canonical != url_for(path): errors.append(label + " : URL canonique incorrecte")
        if any(n > 1 for n in Counter(doc.ids).values()): errors.append(label + " : ID dupliqué")
        if doc.controls - doc.labels: errors.append(label + " : labels manquants")
        for raw in doc.schema:
            try: json.loads(raw)
            except json.JSONDecodeError: errors.append(label + " : JSON-LD invalide")
    for path, doc in pages.items():
        label = path.relative_to(ROOT).as_posix()
        for href in doc.links:
            if href.startswith("/") and not href.startswith("//"):
                errors.append(label + " : chemin absolu incompatible avec GitHub Pages en sous-dossier : " + href)
            item = destination(path, href)
            if item is None: continue
            target, frag = item
            if target == "OUTSIDE" or not target.is_file():
                errors.append(label + " : lien brisé " + href)
            elif frag and target.suffix == ".html" and target in pages and frag not in pages[target].ids:
                errors.append(label + " : ancre introuvable " + href)
    sitemap = ROOT / "sitemap.xml"
    if not sitemap.is_file(): errors.append("sitemap absent")
    else:
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = [n.text for n in ET.parse(sitemap).getroot().findall(".//s:loc", ns)]
        expected = {url_for(p) for p,d in pages.items() if "noindex" not in d.robots.lower()}
        if len(urls) != len(set(urls)): errors.append("sitemap : doublons")
        if set(urls) != expected: errors.append("sitemap : URLs manquantes ou superflues : " + str((expected-set(urls), set(urls)-expected)))
    print("Pages analysées :", len(pages))
    for e in errors: print("ERREUR :", e, file=sys.stderr)
    if errors: sys.exit(1)
    print("Contrôles statiques : OK")

if __name__ == "__main__": check()
