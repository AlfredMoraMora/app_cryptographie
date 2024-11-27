# La cryptographie

# Qu'est-ce que la cryptographie

La cryptographie est une façon de protéger des informations et données à l'aide de différentes
méthodes. Ces différentes méthodes ont toutes des forces de protection de l'information différentes.

## Le chiffrement

Le chiffrement des données permet de transformer des données pour qu'elles soient déchiffrables 
seulement par la personne à qui elles sont destinées. Par exemple, utiliser un langage secret, donner un code secret
à un ami pour qu'il puisse lire un message qu'on a modifié, ce sont des formes de chiffrement.

### Le chiffrement de César

Une méthode de chiffrement utilisée depuis longtemps est le chiffrement de César. Cette méthode porte ce nom car elle a
été historiquement utilisée par Jules César pour transmettre des informations à ses généraux 
afin qu'elles ne puissent être lues que par ces derniers.

La méthode consiste à décaler toutes les lettres d'un mot ou d'un message d'un certain nombre de caractères dans l'alphabet.
César avait comme méthode de décaler tout de 3 lettres. Par exemple, le mot "bonjour" chiffré de cette façon devient "erqmrxu"

- b décalé de 3 caractères vers la droite devient e
- o décalé de 3 caractères vars la droite devient r
- et ainsi de suite...

Pour bien comprendre comment le chiffrement de fait, il peut être plus simple de visualiser l'alphabet comme étant un tout circulaire,
c'est à dire qu'après "z" on recommence à "a".

Ce chiffrement peut être utilisé avec n'importe quelle valeur de rotation vers la droite, on choisira le caractère selon le nombre de
décalage voulu. Un algorithme populaire nommé ROT13, consiste en fait à utiliser le chiffrement de César avec une valeur de rotation de 13. 

Le chiffrement de César est considéré comme un chiffrement relativement faible car avec suffisamment de rotations on peut retrouver
le mot ou message initial. 


## Le hashage

Le hashage fait également partie de la cryptographie et consiste à générer une séquence de caractères (appelée hash)
pour remplacer les données à chiffrer. Il existe plusieurs algorithmes de hashage qui produisent des résultats différents 
pour les mêmes données. Un algorithme de hashage est également irréversible, on ne peut donc pas retrouver les données initiales
de façon algorithmique.

L'avantage d'un algorithme particulier est qu'il donnera toujours le même résultat pour une série de données particulières.
Grâce à cela, on utilise les algorithmes de hashage pour stocker les mots de passe dans les bases de données. Lorsqu'un utilisateur
saisit son mot de passe en créant un compte, ce mot de passe est hashé et sauvegardé dans la base de données. Quand il veut 
ensuite s'authentifier, il saisit à nouveau son mot de passe. Ce dernier est hashé puis comparé au hash stocké dans la base de données.
Si les deux hash correspondent l'utilisateur est alors authentifié.

Par exemple voici le résultat de différents algorithmes de hashage sur la phrase "Hello, World!"
- md5 : 65a8e27d8879283831b664bd8b7f0ad4
- sha256 : dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
- sha512 : 374d794a95cdcfd8b35993185fef9ba368f160d8daf432d08ba9f1ed1e5abe6cc69291e0fa2fe0006a52570ef18c19def4e617c33ce52ef0a6e5fbe318cb0387

Chaque algorithme créera un hash de la même longueur peu importe la taille des données initiales. 
Par exemple, la taille d'un hash md5 sera toujours de 32 caractères, que ce soit le hash d'un seul mot ou du texte complet d'un livre.

## Le module hashlib

[hashlib Python 3.12](https://docs.python.org/3/library/hashlib.html#usage)

Le module hashlib est un module intégré au langage python. Il ne requiert pas l'installation d'un module externe et peut être
tout simplement importé dans les fichiers python sans manipulation supplémentaire.

Une fois importé, on peut l'utiliser pour faire calculer les hash d'une chaîne de caractères voulue.

***Important***: Le hash se calcule sur les bytes de la chaîne de caractères. Il faudra donc en faire la conversion pour que le
calcul puisse se faire. Cela peut se faire de différentes façon

```python
# Au moment de la déclaration de la chaîne
chaine_en_bytes = b"Ceci sera converti en bytes"

# Conversion d'une variable
mot = "Bonjour"
mot_en_bytes = mot.encode()
```

Pour faire calculer un hash il suffit de spécifier quel type de hash on veut calculer via hashlib. Pour obtenir un format
relativement lisible pour nous (et non une chaîne binaire) on utilisera ```hexdigest()``` pour convertir le tout en un chaîne 
de caractères hexadécimaux.

```python
hash_md5 = hashlib.md5(b"allo").hexdigest()
```
