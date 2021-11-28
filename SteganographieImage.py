import numpy as np
from os import chdir
chdir("C:\\")#Il faut mettre le chemin d'accès au photo ici.
import matplotlib.pyplot as plt
def alleger(n):
    n=n//16
    a=0
    for i in range(4):
        if n!=0:
            a+=(n%2)*2**(4+i)
        n=n//2
    return a
def combiner(n,p):
    p=p//16
    n=n//16
    a=0
    for i in range(4):
        if p!=0:
            a+=(p%2)*2**(i)
        if n!=0:
            a+=(n%2)*2**(4+i)
        n=n//2
        p=p//2
    return a
def Elle(N):
    l=N.shape
    F=np.zeros(l)
    for i in range(l[0]):
        for j in range(l[1]):
            for k in range(l[2]):
                F[i,j,k]=int(N[i,j,k]*255+0.5)
    return F
        
def extraire(n):# Extrait à partir d'un pixel une image
    a=0
    for i in range(4):
        if n!=0:
            a+=2**(i+4)*(n%2)
        n=n//2
    return a
    
    
def Chiffrement(M,N): #Crée l'image crypté issue de la combination des deux autres images
    F=Elle(N)
    G=Elle(M)
    j=N.shape
    l=M.shape
    l=list(l)
    if l[0]>j[0]:
        l[0]=j[0]
    if l[1]>j[1]:
        l[1]=j[1]
        
    E=np.zeros(l)
    for i in range(l[0]):
        for j in range(l[1]):
            for k in range(l[2]):
                E[i,j,k]=(combiner(F[i,j,k],G[i,j,k]))/255
    plt.imsave('Imagecrypté.png',E)
    return E

def Dechiffrement(E):#Récupère l'image d'origine à partir de l'image crypté
    G=Elle(E)
    l=E.shape
    F=np.zeros(l)
    for i in range(l[0]):
        for j in range(l[1]):
            for k in range(l[2]):
                F[i,j,k]=extraire(G[i,j,k])/255
    plt.imsave('Imagedorigine',F)
    return F
#Chiffrement(Image1,Image2)
#Dechiffrement(plt.imread('Imagecrypté.png'))  
        
        
        
        
