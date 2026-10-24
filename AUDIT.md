# Audit initial — 24 octobre 2026

## Sources examinées

- Dépôt GitHub `jimmypoirier1993/Siteweb` et PR #1 ; son code contient une page d'accueil, une feuille CSS, un script de navigation/formulaire, un favicon, sitemap et robots.
- Les tentatives de consultation de `https://paideiaeducation.ca/`, de la variante www et de la variante HTTP ont échoué depuis les outils disponibles. Il est impossible de vérifier les contenus du site actuellement publié, ses performances et ses coordonnées.

## Constats confirmés dans le dépôt

1. L'architecture actuelle est un site statique (HTML/CSS/JS) sans dépendances externes et à destination d'un hébergement standard.
2. La PR #1 est un site monopage : les services et la méthode sont des sections mais ne possèdent pas de pages éditoriales dédiées.
3. Le formulaire en pied de page dépend de la constante `recipient` vide ; aucune demande ne peut être envoyée tant qu'une vraie adresse n'est pas validée et configurée.
4. La PR #1 ne fournit ni procédure de contrôle automatique, ni résultats Lighthouse, ni tests navigateur reproduits.
5. Les contenus de la PR #1 décrivent des services probables, mais leur concordance avec la véritable offre n'a pas été établie.

## Stratégie retenue

- Garder une architecture statique pour éviter la complexité d'une compilation non justifiée sur l'hébergement existant.
- Ajouter des pages utiles, lisibles et riches : présentation, méthode, familles de services et ressources éducatives.
- Utiliser des URLs françaises, titres et descriptions uniques, liens croisés et sitemap mis à jour.
- Éviter tout témoignage, tarif, diplôme ou biographie non vérifié.
- Préparer ensuite les tests automatisés et une procédure de validation avant déploiement, dans une PR distincte.

## Points bloquants avant mise en ligne

1. Vérifier les services, les niveaux, les zones desservies, les modalités et la marque sur le site existant ou auprès du propriétaire.
2. Confirmer l'adresse de réception des demandes et le dispositif de confidentialité.
3. Réaliser des tests en navigateur réel, mobile, clavier et lecteur d'écran.
4. Mesurer les Core Web Vitals et les scores Lighthouse, puis corriger les défauts observés.
5. Valider les liens et les URLs finales après configuration du domaine.

**Ce document n'est pas un audit de performance du site en production.**
