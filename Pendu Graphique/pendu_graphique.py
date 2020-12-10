"""
Jeu pendu version graphique
10/12/2020
Lucas Fleury
"""

from random import choice
from tkinter import *

def OpenFichier (): #On récupère un mot au hasard dans le fichier "mot_pendu.txt"
    global affiche,mot,LstAffiche,lettre1,Lettres
    fichier = open("mot_pendu.txt","r")

    for mots in fichier:
        mots = mots.split(",")

    fichier.close()
    mot = choice(mots)
    lettre1=mot[0]
    Lettres = []

    affiche = mot[0]
    for i in range(len(mot)-1):
        affiche += " _"
        LstAffiche = list(affiche)
        
    del LstAffiche[1::2]
    
    for i in range(1,len(mot)):
        if mot[i] == mot[0]:
            LstAffiche[i] = mot[0]
    for i in range(1,len(mot)):
        Lettres.append(mot[i])
        
    affiche = " ".join(LstAffiche)

    return
def ProposerLettre(): # Donne une lettre du mot recherché au hasard et augmente le nombre d'erreur de 2
    global Lettres,mot,erreur
    lettre = choice(Lettres)
    InputLettre.set(lettre)
    erreur+=2
    Lettres.remove(lettre)
    AfficheLettre()
    
def FctRejouer(): #une fois la partie gagner ou perdu, si on rentre 1 dans l'entry, on a un nouveau mot donc une nouvelle partie
    global erreur,biscuit,item
    OpenFichier()
    affichevar.set(affiche)
    erreur = 1
    erreurvar.set(erreur)
    biscuit=PhotoImage(file='Bonhomme'+str(erreur)+'.gif')
    item=Canevas.create_image(0,0,image=biscuit,anchor = "nw")
    
def AfficheLettre(): # programme principale qui est appelé à chaque fois qu'on propose une lettre et qui traite si la lettre est bonne ou non
    global lettre,mot,LstLettre,LstAffiche,erreur,lettre1,affiche,item,biscuit
    rejouer.set('')
    lettre = InputLettre.get()
    InputLettre.set('')
    if lettre == str(1):
        FctRejouer()
        return
    c=0
    erreur1 = 0
    erreur2 = 0
    if lettre in LstLettre:
        erreur1 += 1
        
    LstLettre.append(lettre)
    
    for i in range(1,len(mot)):
        if mot[i] == lettre:
            LstAffiche[i] = lettre
            Lettres.remove(lettre)
            c += 1
            
    if c == 0:
        erreur2 +=1
    
    if erreur1 == 1 or erreur2 == 1:
        erreur +=1
        

    affiche = " ".join(LstAffiche)
    mot2 = "".join(LstAffiche)
    affichevar.set(affiche)
    erreurvar.set(erreur)
    if erreur >= 8:
        affichevar.set("Vous avez perdu le mot était : "+mot)
        rejouer.set('Proposer "1" si vous voulez rejouer')
        biscuit=PhotoImage(file='Bonhomme8.gif')
        item=Canevas.create_image(0,0,image=biscuit,anchor = "nw")
        return
    if mot2 == mot:
        affichevar.set("Vous avez gagné le mot était : "+mot)
        rejouer.set('Proposer "1" si vous voulez rejouer')
        biscuit=PhotoImage(file='Bonhomme'+str(erreur)+'.gif')
        item=Canevas.create_image(0,0,image=biscuit,anchor = "nw")
        return
    
    biscuit=PhotoImage(file='Bonhomme'+str(erreur)+'.gif')
    item=Canevas.create_image(0,0,image=biscuit,anchor = "nw")
    

    
        
OpenFichier()
LstLettre=[]
erreur = 1

Mafenetre=Tk()
Mafenetre.title('Jeu du Pendu')
Mafenetre.configure(bg='#3c3e43')

Largeur=300
Hauteur=300
Canevas=Canvas(Mafenetre,width=Largeur, height=Hauteur,bg='white', highlightthickness=0)

biscuit=PhotoImage(file='Bonhomme'+str(erreur)+'.gif')
item=Canevas.create_image(0,0,image=biscuit,anchor = "nw")

InputLettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=InputLettre)

BoutonProposer=Button(Mafenetre,text='Proposer',command = AfficheLettre,font=("Helvetica"))

BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy,font=("Helvetica"))

BoutonProposerLettre=Button(Mafenetre,text='Proposer une lettre',command = ProposerLettre,font=("Helvetica"))

affichevar=StringVar()
affichevar.set(affiche)
LabelMot=Label(Mafenetre,textvariable=affichevar,fg='white',font=("Helvetica", 20),bg='#3c3e43')

erreurvar=StringVar()
erreurvar.set(erreur)
LabelErreur=Label(Mafenetre,textvariable=erreurvar,fg='white',font=("Helvetica", 20),bg='#3c3e43')
LabelTxtErreur=Label(Mafenetre,text="Nombre d'erreur :",fg='white',font=("Helvetica", 20),bg='#3c3e43')

rejouer=StringVar()
LabelRejouer=Label(Mafenetre,textvariable=rejouer,fg='white',font=("Helvetica", 20),bg='#3c3e43')

LabelRejouer.grid(row=1,column=1,columnspan=2)
LabelTxtErreur.grid(row=2,column=1)
LabelErreur.grid(row=2,column=2)
LabelMot.grid(row=3,column=1,columnspan=2)
BoutonEntry.grid(row=4,column=1,columnspan=2)
BoutonProposer.grid(row=5,column=1,columnspan=2)
BoutonQuitter.grid(row=6,column=1,columnspan=2)
BoutonProposerLettre.grid(row=7,column=1,columnspan=2)
Canevas.grid(row=1,column=3,rowspan=7)

Mafenetre.mainloop()
