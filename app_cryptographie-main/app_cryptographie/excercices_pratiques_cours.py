salutations_chaine = "Allo les amis !"
salutations_liste = ["Allo", "les", "amis", "!"]

# for car in salutations:
#    print(car)

# for i in range(len(salutations_chaine)):
#     print(salutations_chaine[i])

# for i in range(len(salutations_liste)):
#     print(salutations_liste[i])

for i in range(len(salutations_liste)):
    print(salutations_liste[i][-1])

for elt in salutations_liste:
    print(elt[-1])

nouvelle_liste = []

for i in range(len(salutations_chaine)):
    nouvelle_liste.append(salutations_chaine[i])
    print(nouvelle_liste)



