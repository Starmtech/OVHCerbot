# Automatisation de la création de certificats Let's Encrypt avec OVH DNS

Ce dépôt contient un script Python qui automatise le processus de création de certificats SSL/TLS à l'aide de Let's Encrypt et de l'API OVH DNS pour la vérification DNS-01. Ce processus vous permet d'obtenir des certificats pour sécuriser votre domaine en utilisant le mécanisme de vérification DNS de Let's Encrypt.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir les éléments suivants configurés :

- Comptes OVH : Vous devez avoir un compte OVH avec des clés d'API valides.
- Domaine géré par OVH : Le domaine pour lequel vous souhaitez obtenir un certificat doit être géré par OVH.
- Installation de Certbot : Vous devez avoir Certbot installé sur votre système.
- Configuration OVH DNS : Assurez-vous d'avoir configuré vos enregistrements DNS OVH pour permettre la vérification DNS-01.

## Utilisation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en exécutant `pip install ovh certbot certbot-dns-ovh`.
3. Configurez vos informations d'authentification OVH dans le script ou utilisez un fichier `.env` pour les stocker de manière sécurisée.
4. Remplacez les valeurs dans le script par vos propres informations (clés, domaine, etc.).
5. Exécutez le script : `python script.py`.
6. Attendez que le script génère le certificat et mette à jour l'enregistrement DNS OVH pour la vérification.
7. Une fois la propagation DNS effectuée, le certificat Let's Encrypt sera obtenu et validé.

**N'oubliez pas de suivre les bonnes pratiques de sécurité et de confidentialité lors de l'utilisation de ce script. Assurez-vous de comprendre chaque étape avant de l'exécuter en production.**

## Avertissement

L'utilisation de ce script peut affecter vos enregistrements DNS et potentiellement rendre votre site indisponible si mal utilisé. Assurez-vous d'avoir sauvegardé toutes vos configurations et de comprendre les implications avant de l'exécuter.
