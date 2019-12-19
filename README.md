# Projet-Secu-Perso
*Objectifs:*
---
1. Codage d'un fichier à partir d'une matrice choisie
2. Décodage d'un fichier avec la matrice choisie
3. Création de matrice directement du programme


---

## Etape 1:

En tant qu'utilisateur, je dois pouvoir exécuter le script python afin de choisir la matrice de codage et le fichier à coder.  

D'un point de vue du traitement, il faut ouvrir la matrice, récupérer sa taille. Il faut aussi ouvrir le fichier à encoder en mode bainaire pour pouvoir faire des multiplications entre les données.  

Le script doit permettre de créer un fichier contenant les nouvelles données, encodées et terminer son extension avec un "c".  
*(Exemple: test.txt --> test.txtc)*


---

## Etape 2:

En tant qu'utilisateur, je dois pouvoir exécuter le script python afin de pouvoir récupérer le chier coder à partir de la matrice de codage.  

D'un point de vue du traitement, il faut ouvrir le fichier en mode binaire pour récupérer les différents octets, appliquer les colonnes de la matrice identité afin de récupérer les valeurs initiales.  

Le script doit permettre d'ouvrir un fichier dont l'extension se termine par "c", appliquer à l'inverse et récupérer le fichier final avec un "d" à la fin.  
*(Exemple: test.txtc --> test.txtcd || test.txt [ne garde pas l'historique] )*