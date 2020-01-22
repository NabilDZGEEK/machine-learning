import random
import termcolor
from termcolor import colored
mat=[[1,1],[2,3]] 
id
lignes = len(mat)
colonnes = len(mat[0])
def generate_identite(l):
    m=[]
    li=[]
    for i in range(0,l):
        for j in range(0,l):
            if i==j:
                li.append(1)
            else:
	            li.append(0)
        m.append(li)
        li=[]
    return m
def permuter(ind):
    res=random.randint(0,lignes-1)
    while(res==ind or mat[res][ind]==0):
        res = random.randint(0, lignes - 1)
    for i in range(colonnes):
        mat[ind][i],mat[res][i]=mat[res][i],mat[ind][i]
        id[ind][i], id[res][i]=id[res][i],id[ind][i]

def diviser(ind):
    p=mat[ind][ind]
    if p!=1:
      for i in range(colonnes):
        mat[ind][i]/=p
        id[ind][i] /= p

def sub(li,col):
    if mat[li][col]!=0:
        if mat[col][col]==0:
            permuter(col)
        a=mat[li][col]/mat[col][col]
        for i in range(colonnes):
            mat[li][i]-=a*mat[col][i]
            id[li][i] -= a * id[col][i]

def ligneEstNul(ind):
    for i in range(colonnes):
        if(mat[ind][i]!=0):
            return False

    return True
def inverser():

    if(lignes==colonnes):
        global id
        id=generate_identite(lignes)
        for j in range(colonnes):
            for i in range(lignes):
                if(i==j): #pivot
                    if(mat[i][j]==0):
                        permuter(i)
                    diviser(i)
                else:
                    sub(i,j)
                    if ligneEstNul(i):
                        return 0
                #afficher(mat)
        return 1
    else:
        return -1
def afficher(x):
    for i in range(lignes):
        for j in range(colonnes):
            print(x[i][j], end='\t')
        print()
    print()
result=inverser()

if result==-1:print(colored("la matrice n'est pas carée!","red"))
if result==0:print(colored("la matrice est inversible!", "red"))
if result==1:afficher(id)
