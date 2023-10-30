#coding: utf-8


import os
from random import*
import pickle



pseudo={}

try:
    with open("utilisateur.pkl", 'rb') as fic :
        ouvrir=pickle.load(fic)
        pseudo = ouvrir
        
except:
    defaut={"md":0}

    with open('utilisateur.pkl', 'wb') as util:
        pickle.dump(defaut, util)
        util.close()
            
    pseudo = defaut






lancer=" "
nomCorrect =" "
score_user=0

while lancer != "k" :
            
            
    #start =" "
    #while start != "q" :
    nom=input("entrez votre pseudo : ")


    test=0
    while test==0 :
        if len(nom)== 0 :
            nom=input("vous devez entrer une valeur  ")
            test=0
            continue
        for el in nom :
            if el.isspace():
                nom=input("le pseudo ne peut pas contenir d'espace ")
                test=0
                break
            elif el.isupper() :
                nom=input("le pseudo ne peut pas contenir de lettre majuscule ")
                test=0
                break
            else :
                nomCorrect = nom
                test = 1   
                    
       # print(nomCorrect)
    #score=0
    #pseudo[nomCorrect]=score

    

    enregistre=True
    if nomCorrect in pseudo.keys() :
        print("bon retour", nomCorrect)
        enregistre=False

    if enregistre==False :
        score_user=pseudo[nomCorrect]
    else :
        pseudo.update({nomCorrect : 0})
            
        print("Bienvenu ", nomCorrect)


    
    

    nb_jeu=randint(0,9)
    essaie=0
        
    score_jeu=0
    for i in range(5) :
            
            nb_choisi=int(input("choisir un nombre :" ))
            while nb_choisi < 0 or nb_choisi >9 :
                nb_choisi=int(input("vous devez choisir un nombre compris entre 0 a 9\n"))
                
            if nb_choisi == nb_jeu :
                print("BRAVO!!!")
                score_jeu=(5-essaie)*30
                print("le score est de cette partie est : ",score_jeu)
                print("votre score total  est : ", score_user +score_jeu)
                break
            elif nb_choisi> nb_jeu :
                print("le nbre est trop grand")
            else :
                print("le nbre est trop petit")
            essaie+= 1
            print("il vous reste ",5-essaie,"chance")
            
            if essaie ==5 :
                print("vous avez perdu le jeu et le nombre cache est : ",nb_jeu)
                print("le score est de cette partie est : ",score_jeu)
                
                if nomCorrect in pseudo.keys() :
                    total = score_jeu + pseudo[nomCorrect]
                    pseudo[nomCorrect] =total
                else :
                    pseudo.update({nomCorrect   : score_jeu})
                    
                
                os.remove("utilisateur.pkl")
                
                
                with open('utilisateur.pkl', 'wb') as util:
                    pickle.dump(pseudo, util)
                    util.close()
                
     
        
        
        
    lancer=input("si vous ne voulez pas continuer de jouer presser k\n")

   