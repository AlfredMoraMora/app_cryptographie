import hashlib


def hasher_mots(mots: list[str]) -> dict:
    return {
        mot: [
            hashlib.md5(mot.encode('utf-8')).hexdigest(),
            hashlib.sha256(mot.encode('utf-8')).hexdigest(),
            hashlib.sha512(mot.encode('utf-8')).hexdigest()
        ]
        for mot in mots
    }


def find_matches(mots_hash, hash_dict):
    decrypted_words = []
    for hash_item in mots_hash:
        match_found = False
        for word, hashes in hash_dict.items():
            if hash_item in hashes:
                decrypted_words.append(word)
                match_found = True
                break  # Move to the next hash item once a match is found
        if not match_found:
            decrypted_words.append("No match found for this hash")
    return decrypted_words


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
    mots_hash = [
        'dc0add0b9d59afd7f5d38ee814f85c37',
        '3378673b4755b9c5d291a295aade6ed10ab531e77cdb96b92e531e3b4be1aa260e34507681117cd8212341e2a37d31540af25302584bb489b5614f805883e2ff',
        'ceac214f32b3bc28669d0e09487d82a171fbc38f7b48140e50279e7774c079ae',
        'ef0738953fcb9fbfedc6795a7c5e8a7d5894d3534adc346e0f9f1bf0a3017f87a21ef14bac9340b7d1fcdc9579906ae1bde0bd514b9b8c1e2e091d1314abf528'
    ]

    # Create the dictionary of hashes
    dict_mots = hasher_mots(mots_aleatoires)

    # Find matches
    results = find_matches(mots_hash, dict_mots)

    # Output results
    for hash_item, decrypted in zip(mots_hash, results):
        print(f"Hash: {hash_item} -> Word: {decrypted}")