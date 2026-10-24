# Paideia Éducation — V2 (proposition)

Site vitrine statique en **fr-CA**, sans framework et sans dépendance JavaScript externe. À valider avant toute mise en production.

## Démarrage local

```sh
python3 -m http.server 8000
```

Ouvrir http://localhost:8000. Déploiement possible sur un hébergement statique avec les fichiers à la racine.

## Vérifications obligatoires avant validation

- [ ] Confirmer auprès de Paideia les offres, niveaux, modalités, services et formulations commerciales.
- [ ] Vérifier l'orthographe commerciale exacte de la marque, les droits sur le contenu, l'identité visuelle et le nom de domaine canonique.
- [ ] **Configurer `recipient` dans `main.js`** avec une adresse approuvée et tester le flux. Le formulaire est volontairement inactif sans celle-ci ; aucune demande n'est envoyée côté serveur. Préférer à terme un backend sécurisé avec consentement et protection anti-spam.
- [ ] Faire vérifier les mentions de confidentialité et obligations juridiques applicables avant de recueillir des données personnelles.
- [ ] Tester le site au clavier, sur mobile et avec un lecteur d'écran.
- [ ] Exécuter un audit Lighthouse et corriger les points relevés.
- [ ] Confirmer les redirections www/non-www, HTTPS, le cache et la configuration DNS de l'hébergeur.
- [ ] Ajouter des témoignages, photos, tarifs et coordonnées **uniquement s'ils sont authentiques et autorisés**.

## Choix d'architecture

HTML sémantique, CSS responsive et JS minimal. Métadonnées OpenGraph, données structurées EducationalOrganization, sitemap, robots et lien d'évitement. Pas de cookies analytiques ni de chargement de police externe.

## Limites

Le site public n'a pas pu être consulté pendant l'audit initial ; ce projet est une proposition construite à partir du positionnement général de l'entreprise, **pas** une reproduction ni un audit exhaustif du site existant. Le formulaire doit être configuré avant publication.

## Recette et contrôle qualité

Voir `AUDIT.md` et `VALIDATION.md`. Configurer le courriel autorisé dans `site-config.js` avant publication. Les contrôles statiques n’équivalent pas à un audit Lighthouse ni à une certification WCAG.

## Chemins compatibles GitHub Pages

Les liens vers les ressources et les pages internes utilisent des chemins relatifs (`./` à la racine, `../` dans les sous-répertoires). Cela permet de servir les mêmes fichiers depuis `https://<utilisateur>.github.io/<depot>/` et depuis un domaine personnalisé à la racine, sans compilation ni variable de base URL. Le contrôle statique rejette désormais les liens HTML internes commençant par `/`.
