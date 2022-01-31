import csv
from datetime import datetime

# Module personnel 
import calcule as clc
import scraping as scp
import log as lg




def finder(what,area): 
    """ Recherche et retourne l'élément à l'intérieur la balise donné (what). Il a aussi besoin de la zone de recherche(area)
    Si jamais la balise n'est pas trouvée, elle est affichée dans notre terminal"""

    result = "" 
    i = 0 # compteur


    while i<300: # recherche le motif 
                 #s'il ne trouve aucun nom il s'arrête automatiquement après 300 bouclages 
                 # ( par sécurité  [ le fichier en contient ~275])

        if area[i:i+len(what)]==what:       # Si la balise est trouvée

            i+=len(what)                    # Passe la balise

            while area[i] != "<":           # tant que l'on n'est pas arrivé à la balise de fin

                result += area[i]           

            break                           # Travail fini j'arrête la boucle

        i+=1                                

    
    return result

def sort(content):
    """Trie le contenu de la page et renvois le contenue des balises demandées"""

    time = finder("<DateTime>",content)            # Date de la mise à jour 
    name = finder("<Name>",content)                # Nom du parking
    free = finder("<Free>",content)                # nombre de places libres
    total = finder("<Total>",content)              # nombre de places totales du parking

    return time, name, free, total
    

def writer(content):
    """ Mets le contenu de la page dans un fichier txt au nom de la station ( si pas de fichier : il le crée)"""


    station_name = "./station_file/"+finder("<Name>",content) + ".txt" # trouve le nom de la station puis rajoute l'extention .txt pour le fichier 

    fichier = open(station_name,"a",encoding='utf8') # ouvre le fichier en mode écriture ( si inexistant : création file )

    fichier.write(content)                           # écrit dans le fichier le contenu de la page web

    fichier.close()                                  # ferme proprement le fichier
    

def import_xml(id):
    """ importe le contenu de la page xml et appel la fonction d'écriture dans un .txt"""

    xml= scp.web_content(id)   # va chercher les informations de la page de l'id

    writer(xml)            # appel de la fonction d'écriture

    return xml
    
def csv_file_writer_parse(id,csv_existe):

    """" écrit dans le fichier stat.csv les données xml de manière ordonée"""
    #global csv_existe

    with open('stat_park.csv', 'a', newline='') as csvfile:      # ouvre un fichier CSV en écriture nommée stat.csv ou le crée si existe pas
        
        fieldnames = ['station_name', 'free_park_space','total_park_space','year','day&month','hour&min']     # donne les noms de chaque catégorie
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)                 # donne attirbut csv et les sépatateurs a la variable writer

        if csv_existe == False :    # Si le fichier csv est défini dans le main comme non existant ALORS
            writer.writeheader()    # On écrit le titre des catégories +
            csv_existe = True       # On défini dans le main le fichier comme existant 

        for i in range (len(id)):
            content=import_xml(id[i])
            writer.writerow({'station_name': sort(content)[1], 'free_park_space': sort(content)[2], 'total_park_space': sort(content)[3],  'year': sort(content)[0][0:4],  'day&month': sort(content)[0][5:10],  'hour&min': sort(content)[0][11:16]})   # écrit dans le fichier csv
    time=str(datetime.now())
    lg.log_write(f"Une donnée a été enregisté dans le fichier stat_park.csv le {time[5:10]} à {time[11:16]} prochain relevé prévu a {time[11:13]}:{str(int(time[14:16])+10)}")


def csv_file_reader(file):

    """Fonction lisant un fichier csv ( file ) et retourne sous forme de liste tous les éléments du fichier"""

    result = [] # initiation de la variable result ( type list )

    with open(file, newline='') as csvfile:   # ouvre un fichier 
        reader = csv.DictReader(csvfile)      # lis le contenu 
    
        for row in reader:
            result.append([row['station_name'], row['free_park_space'], row['total_park_space'],row['year'],row['day&month'],row['hour&min']]) # ajoute sous forme de liste chaque élément du fichier de manière ordonnée
    
    return result # type(list)

