#!/usr/bin/env python3
#coding:utf-8

# Script name: codec
# Description: programme avec Clé de chiffrement matricielle
# Made by: Ezeqielle & Batmine3
# Begin: 14/12/2019
# End: 

import os

#matrix
matrice = input("Entrez le nom de la matrice a selectionner : ")
fileOpen = open("key/"+matrice+".txt", "r")
workKey = fileOpen.read()
print(workKey)
begin = workKey.index("[")
end = workKey.index("]")
key = workKey[begin+1:end]
key = key.split(" ")
print(key)
#compter la longueur de la cle pour determiner la taille de la matrice G4 ou G5 ou G6 etc ... afin de rendre le programme utilisable pour toute les matrices

#file
workFile = input("Entrez le nom du fichier : ")
fileOpen = open("file_encode/"+workFile, "rb")
print(fileOpen.read())
#decouper le fichier par segment binaire de taille Gx trouver au dessus

#matrix multiplication

#encode Key for decoding
#boucler pour le nombre d'occurence en fonction de la taille de la matrice
print("Entrez la cle d'encodage de la matrice : ")
G1 = input("1 : ")
G2 = input("2 : ")
G3 = input("3 : ")
G4 = input("4 : ")
encodeKey = (G1, G2, G3, G4)
print(encodeKey)

#output