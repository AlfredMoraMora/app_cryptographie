import hashlib

def hasher_mots(mots: list[str]) -> dict:
    """
    Fonction qui reçoit une livre de mots et qui génère les hash md5, sha256 et sha512 de chaque mot à
    l'aide du module hashlib.
    La fonction génère ainsi un dictionnaire dont les clés sont les mots et les valeurs sont
    une liste des 3 hash calculés auparavant.
    :param mots: La liste des mots à hasher
    :return: Le dictionnaire généré contenant les hash de chaque mot
    """
    hash_dict = {}
    for mot in mots:
        hash_dict[mot] = [hashlib.md5(mot.encode('utf-8')).hexdigest(), hashlib.sha256(mot.encode('utf-8')).hexdigest(), hashlib.sha512(mot.encode('utf-8')).hexdigest()]

    # TODO: Complétez cette fonction pour qu'elle génère un dictionnaire contenant les 3 hash demandés (md5, sha256, sha512)
    #   pour chacun des mots dans la liste des mots non chiffrés fournie dans le programme principal.

    return hash_dict


def chiffrement_cesar(chaine: str, nb_cesar: int) -> str:
    """
    Cette fonction reçoit un mot ainsi que le nombre de rotation pour chiffrer le mot. Elle en fait le chiffrement
    de césar en utilisant le nombre reçu pour transformer le mot.
    :param chaine: Le mot ou chaîne de caractères à chiffrer
    :param nb_cesar: Le nombre de rotations à faire pour le chiffrement.
    :return: La chaine chiffrée résultante
    """
    caracteres_remplacement = "abcdefghijklmnopqrstuvwxyz"
    chaine_chiffree = ""






    # TODO: à l'aide des caractères de remplacement, du nombre de César et de la chaine originale, faire le chiffrement
    #   de césar et retournez la chaîne ainsi générée




if __name__ == '__main__':

    mots_aleatoires = [
        "arbre", "bateau", "chat", "drapeau", "elephant", "fleur", "glace", "horizon", "iguane", "jonquille",
        "kangourou", "lumiere", "montagne", "nuage", "porte", "quiche", "requin", "soleil", "tigre",
        "univers", "vague", "wagon", "xylophone", "yeti", "zebre", "abeille", "ballon", "canard", "dejeuner",
        "etoile", "fromage", "girafe", "horloge", "internet", "joie", "karaoke", "livre", "magie", "neige",
        "orange", "parapluie", "quartz", "riz", "sable", "telephone", "uniforme", "velo", "weekend", "xylocope",
        "yaourt", "zeste", "amour", "banane", "cerise", "dent", "enfant", "fete", "guitare", "herisson",
        "idee", "jardin", "koala", "lune", "maison", "nature", "oiseau", "pomme", "quai", "riviere",
        "serpent", "tomate", "ulysse", "vent", "whisky", "xenon", "yeux", "zen", "avion", "boulangerie",
        "cerf", "dromadaire", "epinard", "fusil", "grange", "hameau", "ilot", "jongleur", "kilogramme",
        "lavoir", "muguet", "navire", "ours", "pierre", "quatre", "renard", "scie", "trousseau", "universite"
    ]

    mots_cesar = [
        "ozsxkbn",
        "thecqtqyhu",
        "diozmizo"
    ]

    mots_hash = [
        'dc0add0b9d59afd7f5d38ee814f85c37',
        '3378673b4755b9c5d291a295aade6ed10ab531e77cdb96b92e531e3b4be1aa260e34507681117cd8212341e2a37d31540af25302584bb489b5614f805883e2ff',
        'ceac214f32b3bc28669d0e09487d82a171fbc38f7b48140e50279e7774c079ae',
        'ef0738953fcb9fbfedc6795a7c5e8a7d5894d3534adc346e0f9f1bf0a3017f87a21ef14bac9340b7d1fcdc9579906ae1bde0bd514b9b8c1e2e091d1314abf528'
    ]

    mots_cesar_hash = [
        '95b7aa774ee5d86302c89ef3bc6e3fcd',
        '059f79fbb20a17eb6c7dc12883fb6105eca60071034ac32ae201a57762020e07'
    ]

    dict_mots = hasher_mots(mots_aleatoires)

    mot_mystere1 = mots_hash[0]
    mot_mystere2 = mots_hash[1]
    mot_mystere3 = mots_hash[2]
    mot_mystere4 = mots_hash[3]

    # for mot in mots_hash:
    #     option1 = mot
    #     for i in hasher_mots(mots_aleatoires):
    #         option2 = i
    
    # values = dict_mots.values()
    # keys = dict_mots.keys()

    for i in dict_mots.items():
        print(i)


