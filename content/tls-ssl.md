---
title: "TLS SSL"
date: 2020-08-01T10:03:36+01:00
---

## TL;DR

*Too Long Didn’t Read*

* HTTP**S** = HTTP sur TLS
* Les 2 idées majeures de TLS:
    1. Orchestrer le partage d’un secret à distance (cryptographie asymétrique)
    2. Chain of trust: l’ami de mon ami est mon ami
*   Ce sont les acteurs majeurs(Firefox,Google,Microsoft) qui décident, par défaut, de la fiabilité d'un site web

## HTTPS, SSL, TLS ?

**SSL**[^1]**: **le nom historique, **TLS**  la nouvelle version recommandée  par les standards internationaux .

**HTTPS**: la version sécurisée du protocole HTTP, on parle aussi de “[HTTP sur TLS](https://tools.ietf.org/html/rfc2818)”

Pour des raisons de compatibilité, plusieurs logiciels dans leurs paramètres de configuration mentionnent **SSL**[^2] alors que le protocole implémenté et utilisé techniquement est **TLS**.

![stack-overview]({static}/images/tls/tls-ssl-stack.svg)

## TLS - en bref

Il orchestre les différents échanges et permet aux client et serveur distant de:

*   S’accorder sur la façon de sécuriser leurs échanges (combinaison d’algorithmes, échange de clés ...)
*   Vérifier l’identité du serveur distant 


![stack-overview]({static}/images/tls/trust-chain-overview.svg)

## Un certificat ?

Il permet d’assurer à l’utilisateur d’une clé publique qu’elle appartient bien à la personne attendue.

On les retrouve dans la nature sous forme de fichier *.pem ou *.dem.

Il protège d’attaque de type  “man in the middle”. 

## Un navigateur fait confiance à certaines pages et pas d’autres

Firefox arrive avec une liste de certificats considérés comme fiables par un processus défini par Mozilla/Firefox.

Les autres navigateurs majeurs (Chrome,Microsoft Edge, …) se basent sur ceux présents sur le système d’exploitation. 

Les fournisseurs d'OS (Apple/Microsoft/etc) installent des certificats qu’ils pensent fiables via un procédé interne de sélection.

Par transitivité, si je suis un utilisateur Windows, je fais confiance à ce dernier pour gérer et sélectionner les “root” certificats via le [Microsoft Trusted Root Program](https://docs.microsoft.com/en-us/security/trusted-root/participants-list). (~ 150 participants).

![trust chain]({static}/images/tls/trust-chain.svg)


Ces certificats peuvent eux-mêmes signer d’autres certificats, et créent une chaîne de confiance (**chain of trust**) :_ l’ami de mon ami est mon ami _

Pour “khalidck.fr”, si on inspecte le certificat via le [navigateur](https://support.mozilla.org/fr/kb/certificats-authentification-pour-sites-web-securises):

![exchange tls]({static}/images/tls/exchange-tls.png)


“DST ROOT CA” est [connu de firefox](https://ccadb-public.secure.force.com/mozilla/CACertificatesInFirefoxReport) ce qui permet au final d’avoir une validation du navigateur 

![firefox]({static}/images/tls/screen-web-trust.png)


## Bulletproof ?

TLS repose sur une base théorique forte, **mais aussi** sur un principe de confiance: le navigateur et/ou le système d'exploitation est responsable du choix des bons partenaires. 

Ce ne sont pas des machines, mais des êtres humains, des sociétés privées, des institutions ou des pays.

La sécurité est avant tout une histoire de gestion des risques, aucun système n’est infaillible. Comprendre en détail son système et ses outils pour permet de prendre une décision éclairée.

Quelques articles qui traitent du sujet :


*   ROBERT HEATON, “[HTTPS in the real world](https://robertheaton.com/2018/11/28/https-in-the-real-world/)”
*   Wikipedia,” [CA compromised](https://en.wikipedia.org/wiki/Certificate_authority#CA_compromise)”

<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     Il est recommandé de ne plus l’utiliser cf [RFC 7568 - Deprecating Secure Sockets Layer Version 3.0](https://tools.ietf.org/html/rfc7568)

[^2]:
      Par exemple [nginx](https://nginx.org/en/docs/http/configuring_https_servers.html)
