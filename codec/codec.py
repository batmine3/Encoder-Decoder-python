#!/usr/bin/env python3
#coding:utf-8

# Script name: codec
# Description: programme avec Clé de chiffrement matricielle
# Made by: Ezeqielle & Batmine3
# Begin: 14/12/2019
# End: 

# /!\ ne pas oublier d'enlever les print() de debug a la fin /!\

#Add creation de matrice

import os

q = 0
while (q == 0):
    x = input("Select you option : \n 1 - Decode file \n 2 - Encode file \n 3 - Create matrix \n 4 - Quit \n\n Your option : ")
    if (x == "1"):
        print("some code")
    elif (x == "2"):
        print("some other code")
    elif (x == "4"): 
        a = input("Are you sure want exit ? (y/n) : ")
        if(a == "y" or a == "Y" or a == "yes" or a == "Yes" or a == "YES"):
            q = 1
        else:
            q = 0
    else:
        print("invalid choice")


"""

#matrix
matrice = input("Entrez le nom de la matrice a selectionner : ")
keyOpen = open("key/"+matrice+".txt", "r")
workKey = keyOpen.read()
keyOpen.close()
print(workKey)
begin = workKey.index("[")
end = workKey.index("]")
key = workKey[begin+1:end]
key = key.split(" ")
print(key)
matrixSize = len(key)
print(matrixSize)
#compter la longueur de la cle pour determiner la taille de la matrice G4 ou G5 ou G6 etc ... afin de rendre le programme utilisable pour toutes les matrices

#file
workFile = input("Entrez le nom du fichier : ")
fileOpen = open("file_encode/"+workFile, "rb")
print(fileOpen.read())
fileExtension = workFile.split(".")
fileExtension = fileExtension[1]
print(fileExtension)
#decouper le fichier par segment binaire de taille Gx trouver au dessus
#compter la taille de la liste pour la longueur de la boucle

#matrix multiplication

#encode Key for decoding
#boucler pour le nombre d'occurence en fonction de la taille de la matrice
#recuperation de la matrice identitee
print("Entrez la cle d'encodage de la matrice : ")
c = 0
i = 0
encodeKey = [0] * matrixSize
while (i < matrixSize):
    c += 1
    G = input("column "+str(c)+" : ")
    encodeKey[i] = G
    i += 1
print(encodeKey)

#output


"""