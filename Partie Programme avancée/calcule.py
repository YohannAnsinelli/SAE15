########################
# CALCULE MATHEMATIQUE #
########################

from math import sqrt


def average(liste):
    """ Renvois la moyenne d'une liste d'int"""
    
    return round(sum(liste)/len(liste)*100,2)

def standard_scratch(liste):
    """ Renvois l'écart type d'une liste d'int"""
    
    moy = average(liste)
    result = 0

    for i in range (len(liste)):

        result += (float(liste[i]) - float(moy))**2
    return round(sqrt(result/len(liste)),2)

