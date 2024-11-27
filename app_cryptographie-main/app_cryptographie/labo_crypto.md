# Laboratoire

## But

- Manipuler les algorithmes de hashage avec le module hashlib
- Manipuler les chaînes de caractères
- Manipuler les dictionnaires
- Manipuler du code déjà fourni

Dans ce laboratoire, vous devrez utiliser vos connaissances afin de découvrir les mots qui se cachent derrière des chaines
de caractères qui ont été chiffrées de différentes façons.

Dans le code déjà fourni vous trouverez une liste de mots en texte clair. Chacune des chaines chiffrées correspondent 
à un de ces mots.

Vous trouverez également les listes *mots_cesar, mots_hash, mots_cesar_hash*. Ces 3 listes contiennent
les mots que vous devrez déchiffrer.

- mots_cesar : Cette liste contient les mots chiffrés avec le chiffrement de César.
- mots_hash : Cette liste contient des mots qui ont été hashés avec un des algorithmes suivants: md5, sha256, sha512
- mots_cesar_hash : Cette liste contient des mots qui ont tout d'abord été chiffrés à l'aide du chiffrement de César, puis hashés avec l'un des 3 algorithmes cités précédemment.

## Tâches

À l'aide du code fourni et de la librairie hashlib, vous devrez retrouver les mots qui ont été chiffrés.

La fonction *hasher_mots* vous permettra de créer un dictionnaire des hash md5, sha256 et sha512 de chacun des mots fourni en texte clair.
Ce dictionnaire pourra ensuite vous aider à décoder les mots qui ont été hashés.

La fonction *chiffrement_cesar* permettre de prendre un mot et de retourner ce mot chiffré avec un certain nombre de rotations selon l'algorithme de César.

Vous devez compléter ces deux fonctions permettant de faire le chiffrement. 

Vous devez également créer des fonctions vous permettant de décoder les mots des 3 listes chiffrées.

### Tests unitaires

Vous devez également créer les tests unitaires pour toutes les fonctions créées dans ce programme. Ces tests pourront vous permettre
de vous assurer que les différentes méthodes que vous créer pour chiffrer et déchiffrer fonctionnent bien.

Créez un plan de test afin de bien vous assurer de tester différentes possibilités. N'oubliez pas d'inclure des cas qui devraient causer
des erreurs afin de vous assurer que votre programme gère bien ces cas également.
