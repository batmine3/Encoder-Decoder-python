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

#matrix
def matrixSelection(matrixUsed):
    keyOpen = open("key/"+matrixUsed+".txt", "r")
    workKey = keyOpen.read()
    keyOpen.close()
    print(workKey)
    begin = workKey.index("[")
    end = workKey.index("]")
    key = workKey[begin+1:end]
    key = key.split(" ")
    matrixSize = len(key)
    print(matrixSize)
    matrixID(matrixSize)

#file_encode
def fileEncode(fileUsed):
    fileOpen = open("file_encode/"+fileUsed, "rb")
    workFile = fileOpen.read()
    fileExtension = fileUsed.split(".")
    fileExtension = fileExtension[1]
    print(fileExtension)
#decouper le fichier par segment binaire de taille Gx trouver au dessus
#compter la taille de la liste pour la longueur de la boucle

#matrix ID
def matrixID(matrixSize):
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
#recuperation de la matrice identitee  

q = 0
while (q == 0):
    x = input("Select you option : \n 1 - Encode file \n 2 - Decode file \n 3 - Create matrix \n 4 - Quit \n\n Your option : ")
    if (x == "1"):
        print("encode file : \n")
        matrix = input("Entrez le nom de la matrice a selectionner : ")
        matrixSelection(matrix)
        file = input("Entrez le nom du fichier : ")
        fileEncode(file)
    elif (x == "2"):
        print("decode files : \n")
    elif (x == "3"):
        print("creation matrix : \n")
    elif (x == "4"): 
        a = input("Are you sure want exit ? (y/n) : ")
        if(a == "y" or a == "Y" or a == "yes" or a == "Yes" or a == "YES"):
            q = 1
        else:
            q = 0
    else:
        print("invalid choice")