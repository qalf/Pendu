from random import choice


def OpenFichier ():
    fichier = open("mot_pendu.txt","r")

    for mots in fichier:
        mots = mots.split(",")

    fichier.close()
    mot = choice(mots)
    
    affiche = mot[0]
    for i in range(len(mot)-1):
        affiche += " _"
        LstAffiche = list(affiche)
        
    del LstAffiche[1::2]
    
    for i in range(1,len(mot)):
        if mot[i] == mot[0]:
            LstAffiche[i] = mot[0]
            
    affiche = " ".join(LstAffiche)

    print(affiche)
    return(mot,LstAffiche,mot[0])


def AfficheLettre(lettre,mot,LstLettre,LstAffiche,erreur,lettre1):
    c=0
    erreur1 = 0
    erreur2 = 0
    
    if lettre in LstLettre:
        print("vous avez déjà mis cette lettre")
        erreur1 += 1
        
    LstLettre.append(lettre)
    
    for i in range(1,len(mot)):
        if mot[i] == lettre:
            LstAffiche[i] = lettre
            c += 1
    if lettre == lettre1:
        c += 1
        
    if c == 0:
        print("La lettre n'est pas dans le mot")
        erreur2 +=1
    
    if erreur1 == 1 or erreur2 == 1:
        erreur +=1
        
    if erreur == 8:
        print("Vous avez perdu")
        return(0,erreur)


    affiche = " ".join(LstAffiche)
    mot2 = "".join(LstAffiche)
    print(affiche)
    

    if mot2 == mot:
        print("vous avez gagné")
        return (1,erreur)
    
    return(2,erreur)


jouer = 1

while jouer == 1:
    mot,LstAffiche,lettre1 = OpenFichier()
    LstLettre = [lettre1]
    erreur = 0
    while True:
        lettre = input("Entrez une lettre :")
        gagner,erreur = AfficheLettre(lettre,mot,LstLettre,LstAffiche,erreur,lettre1)
        if gagner == 1 or gagner == 0:
            jouer = int(input("Voulez vous rejouer (1) ou arrèter (0) ?"))
            break

print("Fin")
