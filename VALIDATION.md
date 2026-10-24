# Validation des PR et déploiement

## Série de PR empilées
1. PR #1 : `feat/paideia-v2` → `main`, vitrine de base.
2. PR #2 : `feat/paideia-pages` → `feat/paideia-v2`, pages de services et ressources.
3. PR #3 : `chore/paideia-quality-gates` → `feat/paideia-pages`, contrôles et contact.

**Ne pas fusionner sans validation humaine.** Réévaluer les branches cibles après chaque fusion éventuelle.

## Contrôles automatiques

```sh
python3 scripts/check_site.py
node --check main.js
node --check site-config.js
```

Le script vérifie H1, titres, descriptions, URLs canoniques, liens/ancres internes, labels de formulaire, JSON-LD, présence des ressources et sitemap. Les mesures en navigateur et la qualité éditoriale restent à vérifier.

## Bloquants avant production
- [ ] Valider les services réellement offerts, les zones, niveaux, modalités et biographies.
- [ ] Renseigner `contactEmail` dans `site-config.js` avec une adresse de réception approuvée.
- [ ] Tester l'ouverture du client courriel, puis **l'envoi manuel réel**. La page n'envoie aucun message serveur.
- [ ] Valider les obligations de confidentialité, le traitement des courriels et les journaux de l'hébergeur.
- [ ] Tester navigation mobile, clavier, touche Échap, contrastes et lecteur d'écran.
- [ ] Mesurer Lighthouse / Core Web Vitals et corriger les défauts.
- [ ] Prévoir les redirections des anciennes URL du site WordPress.
- [ ] Valider DNS, HTTPS, sitemap, robots et indexation en préproduction.
- [ ] Autorisation du propriétaire après revue indépendante.

**Aucun score Lighthouse ni niveau de conformité WCAG n'est certifié par ces tests.**
