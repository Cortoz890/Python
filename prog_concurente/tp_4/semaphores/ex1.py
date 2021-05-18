import os, sys, time
 
N = 10
L = []

for i in range(N+1):
    L.append(i)


def P1(sem, mutex):
    i = 1
    somme_impairs = 0

    while i <= N:
        somme_impairs = somme_impairs + L[i]  
        i = i + 2

    somme = somme + somme_impairs


def P2(sem, mutex):
    i = 0
    somme_pairs = 0
    while i <= N:
        somme_pairs = somme_pairs + L[i]
        i = i + 2
    
    somme = somme + somme_pairs

