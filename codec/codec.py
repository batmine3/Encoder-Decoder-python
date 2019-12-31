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

#matrix encode
def matrixEncode(matrixUsed):
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
    return matrixSize

#matrix decode
def matrixDecode(matrixUsed):
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
def fileEncode(fileUsed, matrixSize):
    fileOpen = open("file_encode/"+fileUsed, "rb")  #ouverture du fichier
    workFile = fileOpen.read()                      #passage des data dans une variable
    contenerFile = list(workFile)                   #conversion en list
    bits = map(bytes, contenerFile)                 #conversion en bytes
    print(bits)

    fileExtension = fileUsed.split(".")             #recuperation de l'extension
    fileExtension = fileExtension[1]                #
    print(fileExtension)
    workFileLength = len(workFile)
    print(workFileLength)
    print(contenerFile)
    
    ourDict = {}
    iteration = workFileLength / matrixSize
    if iteration > round(iteration):
        iteration += 1
    for i in range(int (iteration)):
        ourDict["X" + str(i)] = getValues(int(iteration), matrixSize, i, contenerFile) # 3 4 {0, 1, 2}
    
    for i in ourDict:    
        print("" + str(ourDict) + "" + str(ourDict[i]) + "")
    
#decouper le fichier par segment binaire de taille Gx trouver au dessus
#compter la taille de la liste pour la longueur de la boucle


def getValues(numberOfValues, matrixSize, endValue, contenerFile):
    i = numberOfValues * matrixSize
    if endValue != 0:
        endValue = matrixSize * endValue - 1
        startValue = (endValue - 1) * matrixSize  
    elif endValue == 0:
        startValue = 0
        endValue = matrixSize 
    j = 0
    result = ""
    while (j > startValue and j < endValue):
        result = result + contenerFile[j]
        j += 1
    return result



#file_decode
def fileDecode(fileUsed):
    fileOpen = open("file_decode/"+fileUsed, "rb")
    workFile = fileOpen.read()
    fileExtension = fileUsed.split(".")
    fileExtension = fileExtension[1]
    print(fileExtension)
    
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

#matrix calculation
def matrixMul():
    ""

#key creation
def keyCreation():
    ""

q = 0
while (q == 0):
    x = input("Select you option : \n 1 - Encode file \n 2 - Decode file \n 3 - Create matrix \n 4 - Quit \n\n Your option : ")
    if (x == "1"):
        print("\n encode file : \n")
        matrix = input(" Entrez le nom de la matrice a selectionner : ")
        matrixSize = matrixEncode(matrix)
        file = input("Entrez le nom du fichier avec son extension: ")
        fileEncode(file, matrixSize)
    elif (x == "2"):
        print("\n decode files : \n")
        matrix = input(" Entrez le nom de la matrice a selectionner : ")
        matrixDecode(matrix)
        file = input(" Entrez le nom du fichier avec son extension: ")
        fileDecode(file)
    elif (x == "3"):
        print("\n creation matrix : \n")
    elif (x == "4"): 
        a = input(" Are you sure want exit ? (y/n) : ")
        if(a == "y" or a == "Y" or a == "yes" or a == "Yes" or a == "YES"):
            q = 1
        else:
            q = 0
    else:
        print(" invalid choice")