# coding=utf-8
import os
import getpass

matrice = input("Entrez le nom de la matric à selectionner : ")
print(matrice)
user = getpass.getuser()
print(user)
fileOpend = open("/home/"+user+"/Projet-Secu-Perso/codec/key", "r")
if fileOpend ==NULL{
    print("KO")
}else{
    print("OK")
}
