#!/usr/bin/python
import numpy as np
import mdshare
from sklearn import manifold, datasets
from klasa import Funkcja
import matplotlib.pyplot as plt

def funkcja(n):
    dataset = mdshare.fetch('alanine-dipeptide-3x250ns-heavy-atom-distances.npz')
    with np.load(dataset) as f:
        X = np.vstack([f[key] for key in sorted(f.keys())])

    X_new=X[:1000]  
    color=X_new[:,1]
    Y=Funkcja.fun(X_new, n)

#print(X_new)

#x=X_new.flatten()
#y=Y.flatten()
    #print("aaaaa")
    plt.scatter(Y[:,0], Y[:,1], c=color)

if __name__=="__main__":
    from sys import argv
    for p in argv[1:]:
        print(funkcja(p))
funkcja(4)