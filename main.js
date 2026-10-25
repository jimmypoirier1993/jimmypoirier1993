"use strict";
const toggle=document.querySelector("#menu-toggle");
const nav=document.querySelector("#navlinks");
toggle?.addEventListener("click",()=>{const expanded=toggle.getAttribute("aria-expanded")==="true";toggle.setAttribute("aria-expanded",String(!expanded));toggle.setAttribute("aria-label",expanded?"Ouvrir le menu":"Fermer le menu");nav?.classList.toggle("is-open",!expanded);});
function closeNav(){nav?.classList.remove("is-open");toggle?.setAttribute("aria-expanded","false");toggle?.setAttribute("aria-label","Ouvrir le menu");}
nav?.querySelectorAll("a").forEach(a=>a.addEventListener("click",closeNav));
document.addEventListener("keydown",event=>{if(event.key==="Escape" && nav?.classList.contains("is-open")){closeNav();toggle?.focus();}});
// Repère la page ou la rubrique active, y compris dans un sous-dossier GitHub Pages.
const currentPath=window.location.pathname.replace(/index\.html$/, "");
nav?.querySelectorAll("a[href]").forEach(link=>{
 const target=new URL(link.getAttribute("href"),window.location.href);
 const targetPath=target.pathname.replace(/index\.html$/, "");
 if(target.hash || target.origin!==window.location.origin)return;
 if(currentPath===targetPath){
  link.setAttribute("aria-current","page");
 }else if(targetPath.endsWith("/") && currentPath.startsWith(targetPath)){
  link.setAttribute("aria-current","location");
 }
});
document.querySelector("#year")?.replaceChildren(document.createTextNode(String(new Date().getFullYear())));
const recipient = typeof window.PAIDEIA_CONFIG?.contactEmail === "string" ? window.PAIDEIA_CONFIG.contactEmail.trim() : ""; // À valider avant publication.
document.querySelector("#contact-form")?.addEventListener("submit",(event)=>{
 event.preventDefault();
 const form=event.currentTarget;
 const status=document.querySelector("#form-status");
 if(!form.reportValidity())return;
 if(!recipient){status.textContent="Le formulaire n'est pas encore configuré. Merci de revenir plus tard : aucune demande n'a été envoyée.";return;}
 const data=new FormData(form);
 const subject="Demande de tutorat Paideia — "+String(data.get("level"));
 const body=["Nom : "+data.get("name"),"Courriel : "+data.get("email"),"Niveau : "+data.get("level"),"","Besoins :",""+data.get("message")].join("\n");
 window.location.href="mailto:"+encodeURIComponent(recipient)+"?subject="+encodeURIComponent(subject)+"&body="+encodeURIComponent(body);
 status.textContent="Votre logiciel de courriel devrait s'ouvrir : vérifiez et envoyez le message pour finaliser votre demande.";
});
