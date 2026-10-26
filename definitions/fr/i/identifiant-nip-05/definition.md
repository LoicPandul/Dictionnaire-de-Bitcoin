Identifiant au format d'une adresse e-mail (`nom@domaine`) qu'un utilisateur Nostr déclare dans son profil, et qu'un client contrôle en demandant au domaine quelle clé publique correspond à ce nom. Défini par NIP-05, il rend un compte plus facile à reconnaître et à retrouver, mais il identifie un compte sans vérifier qui se trouve derrière.

Le contrôle repose sur un fichier publié par le domaine. Prenons un exemple. Bob ajoute à son profil, l'événement de kind `0` qui contient son nom et sa description, le champ `"nip05": "bob@example.com"`. Quand le client d'Alice affiche ce profil, il sépare l'identifiant en 2 parties, `bob` et `example.com`, puis envoie une requête HTTPS à l'adresse `https://example.com/.well-known/nostr.json?name=bob`. Le serveur répond par un document JSON qui associe des noms à des clés publiques :

```json
{
  "names": {
    "bob": "b0635d6a9851d3aed0cd6c495b282167acf761729078d975fc341b22650b07b9"
  }
}
```

Si la clé renvoyée pour `bob` est celle qui a signé le profil, le client d'Alice considère l'identifiant comme valide et peut l'afficher à côté du nom de Bob. Sinon, il ne l'affiche pas. NIP-05 impose quelques règles de forme : la partie avant le `@` ne contient que des minuscules, des chiffres et les caractères `-`, `_` et `.` ; la clé s'écrit en hexadécimal minuscule, jamais en `npub` ; le serveur ne doit renvoyer aucune redirection HTTP, et le client doit les ignorer. Le nom passe en paramètre de la requête plutôt que dans le chemin, ce qui permet à un domaine de servir un simple fichier statique qui liste plusieurs noms. L'identifiant `_@example.com` joue le rôle d'identifiant racine, que les clients peuvent afficher comme le seul domaine `example.com`.

Le même mécanisme fonctionne dans l'autre sens, pour trouver quelqu'un. Alice tape `bob@example.com` dans la barre de recherche de son client. Celui-ci interroge le fichier du domaine, obtient la clé de Bob, récupère son profil et vérifie qu'il porte bien le même identifiant. La réponse du domaine peut aussi contenir, en option recommandée, un attribut `relays` qui liste les relais où trouver les événements de Bob, ce qui aide le client à charger ses publications.

Un identifiant NIP-05 valide prouve seulement que le domaine associe ce nom à cette clé. Il ne dit rien de la personne : quiconque contrôle un domaine peut y inscrire le nom de son choix. NIP-05 le précise depuis le 29 août 2024 : il sert à identifier un compte, pour faciliter l'échange de contacts et la recherche, et non à vérifier son titulaire. La seule exception tient au domaine lui-même : celui qui possède un domaine connu (une entreprise) ou qui y est rattaché (un projet) peut utiliser l'identifiant comme attestation de ce lien avec l'organisation qui le gère.

La clé publique reste la véritable identité. NIP-05 demande aux clients de suivre une clé, jamais une adresse NIP-05. Si Alice s'abonne à Bob après avoir trouvé sa clé par `bob@example.com`, son client garde cette clé. Si le domaine se met plus tard à renvoyer une autre clé pour `bob`, le client ne remplace pas la clé suivie : il cesse seulement d'afficher l'identifiant, devenu invalide. Chez les clients qui respectent cette règle, le propriétaire du domaine peut donc retirer l'identifiant d'un compte, mais pas détourner ses abonnés vers une autre clé.

La première version de NIP-05, publiée par fiatjaf le 18 juin 2021, associait un profil à un nom de domaine par un enregistrement DNS `TXT` placé sous `_nostrkey.<domaine>`. Le 30 décembre 2021, fiatjaf la remplace par le schéma actuel : un identifiant de type e-mail et un fichier JSON à l'adresse `/.well-known/nostr.json`. NIP-05 passe au statut final le 22 novembre 2022.

*On le désigne aussi par le seul nom de sa spécification, « NIP-05 ». À ne pas confondre avec une adresse e-mail : l'identifiant n'en reprend que le format, et le client se contente d'une requête HTTPS vers le domaine.*
