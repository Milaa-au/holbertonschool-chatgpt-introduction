#!/usr/bin/python3
"""
factorial_recursive.py

Ce script calcule la factorielle d’un entier positif ou nul
passé en argument sur la ligne de commande, en utilisant
une fonction récursive.
"""

import sys

def factorial(n):
    """
    Calcule la factorielle de n de manière récursive.

    Paramètre:
        n (int): entier positif ou nul

    Retour:
        int: factorielle de n

    Exemple:
        factorial(4) -> 24
    """
    # Cas de base : la factorielle de 0 vaut 1
    if n == 0:
        return 1
    # Cas récursif : n! = n × (n-1)!
    else:
        return n * factorial(n - 1)

# Récupération de l’argument passé en ligne de commande
n = int(sys.argv[1])

# Calcul de la factorielle
f = factorial(n)

# Affichage du résultat
print(f)
