# coding=utf-8
import os
import getpass

matrice = input("Entrez le nom de la matric à selectionner : ")
print(matrice)
user = getpass.getuser()
print(user)
fileOpend = open("/home/"+user+"/Desktop/Projet-Secu-Perso/codec/key/"+matrice+".txt", "r")
print(fileOpend.read())