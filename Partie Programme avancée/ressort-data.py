
import csv
from copy import deepcopy # fonction de copie profonde
from math import sqrt


# Module personnel 
import calcule as clc

def csv_file_reader_per_month_and_day_by_hour(file,day,index=['free_vmag_space','total_vmag_space']):

    """Fonction permettant de donner sous forme de matrice le jour avec les informations par heure.
    Prends comme argument le fichier, le jour de recherche, ainsi que les noms des catégories recherche"""

    result = [] # type = list | elle sert de matrice
    hour_list = [] # type = list
    hour = "00" # début de la journée 
    

    with open(file, newline='') as csvfile:   
        reader = csv.DictReader(csvfile) 

        for row in reader :
            
            if row['day&month']=='': # s'il n'y a pas de date dans la ligne 

                continue


            if day == row['day&month'] : # Si on est a la bonne date
                
                if hour == row['hour&min'][0:2] : # la bonne heure
                    
                    hour_list.append( [row [index[0] ], row[ index[1]],row['day&month'],row['hour&min'] ])

                else:    # heure suivante
                    hour = str( int(hour)+1 )

                    if len(hour) == 1: 
                        hour = "0" + hour # pour avoir la même forme que dans la base de données

                    result.append(deepcopy(hour_list))
                    hour_list = []


            elif (int(day[3:])+1) == int(row['day&month'][3:]) or  row['day&month'][3:] == "00":
                result.append(deepcopy(hour_list))
                hour_list = [row [index[0] ], row[ index[1] ]]
                return result

            
            

def average_occupied(liste):
    """ Fonction qui prend comme argument une liste contenant le nombre de places libres et le nombre de places total et renvois une liste des places occupés """


    taken_space = []

            
    taken_space.append((int(liste[1])-int(liste[0]))/int(liste[1]))
        
        
    return taken_space


def ressort_global():

    """ fonction qui va afficher la moyenne globale et l'écart-type des parkings"""

    vmag_total_average = []
    vmag_total_standard_scratch = []

    park_total_average = []
    park_total_standard_scratch = []

    for i in range (17,22): # du jour 17 au jour 21

        print("01-"+ str(i) ) # affiche le jour en traitement 

        y = (csv_file_reader_per_month_and_day_by_hour("stat_vmag.csv","01-"+str(i),["free_vmag_space","total_vmag_space"]))
        
        x = (csv_file_reader_per_month_and_day_by_hour("stat_park.csv","01-"+str(i),["free_park_space","total_park_space"]))

        for j in range(24): # pour chaque heure
            
            try:
                for k in range (len(y[j])): # pour chaque donnée de l'heure j
                    
                    vmag_total_average.append(clc.average(average_occupied(y[j][k])))
                    vmag_total_standard_scratch.append(clc.standard_scratch(average_occupied(y[j][k])))
                    
            except IndexError:
                pass

            for k in range (len(x[j])): # pour chaque donnée de l'heure j

                park_total_average.append(clc.average(average_occupied(x[j][k])))
                park_total_standard_scratch.append(clc.standard_scratch(average_occupied(x[j][k])))

    """ fait un arrondi de la moyenne en % """
    vmag_total_average = round(clc.average(vmag_total_average)/100,2) 
    vmag_total_standard_scratch = round(clc.average(vmag_total_standard_scratch)/100,2)

    park_total_average = round(clc.average((park_total_average))/100,2)
    park_total_standard_scratch = round(clc.average((park_total_standard_scratch))/100,2)

    """ affiche les résultats"""

    print(f"Vmag moyenne global : {vmag_total_average}")
    print(f"Vmag écart-type global : {vmag_total_standard_scratch}")

    print(f"Park moyenne global : {park_total_average}")
    print(f"Park écart-type global : {park_total_standard_scratch}")


def dat_file():

    """ Création du fichier .dat permettant la création du graphique """ """ renvois également les données permetant la covarivance"""

    vmag_total_average = []
    park_total_average = []

    file_name = "data.dat"

    file = open(file_name,'w',encoding='utf8') # ouvre le fichier en mode écriture ( si inexistant : création file )

    header = "#Day.Hour #Vmag% #Park%\n" # commentaire pour savoir à quoi corresponde les valeurs
    file.write(header)                           

    
    for i in range (17,22): # du jour 17 jusqu'au 21

        print("01-"+ str(i) ) # affiche jour en traitement 

        y = (csv_file_reader_per_month_and_day_by_hour("stat_vmag.csv","01-"+str(i),["free_vmag_space","total_vmag_space"]))
        
        x = (csv_file_reader_per_month_and_day_by_hour("stat_park.csv","01-"+str(i),["free_park_space","total_park_space"]))

        liste_park = []
        liste_vmag = []

        for j in range(24):
            
            try:
                for k in range (len(y[j])):
                   
                    vmag_total_average.append(clc.average(average_occupied(y[j][k])))

            except IndexError:
                pass
            
            for k in range (len(x[j])):

                park_total_average.append(clc.average(average_occupied(x[j][k])))

            content_vmag = round(clc.average(vmag_total_average)/100,2)
            content_park = round(clc.average(park_total_average)/100,2)
            
            try:
                content_to_write = f"{y[j][0][2][3:5]}.{y[j][0][3][0:2]} {content_vmag} {content_park}\n" # contenu sous la forme de : jour.heure 
                file.write(content_to_write)
            except IndexError:
                continue
            liste_park.append(content_park)
            liste_vmag.append(content_vmag)
    file.close()        # ferme proprement le fichier

    return liste_park, liste_vmag

def correlation(liste_somme_placeoccup_voiture,liste_somme_placeoccup_velo):
    """ fonction qui calcule la corrélation entre les parkings et les Vmag"""

    moy_liste_voiture = sum(liste_somme_placeoccup_voiture)/len(liste_somme_placeoccup_voiture)
    moy_liste_velo=sum(liste_somme_placeoccup_velo)/len(liste_somme_placeoccup_velo)
    nombre_delement=len(liste_somme_placeoccup_voiture) #j'aurai pu prendre velo c'est la même chose
    somme_cov=0
    somme_varx=0
    somme_vary=0
    element=1/nombre_delement
    for i in range(nombre_delement):
        cov_voiture=liste_somme_placeoccup_voiture[i]-moy_liste_voiture
        cov_velo=liste_somme_placeoccup_velo[i]-moy_liste_velo
        multi=cov_voiture*cov_velo
        somme_cov=somme_cov+multi
    covxy=element*somme_cov #je calcule la covariance des vélos avec les voitures
    
    for i in range(nombre_delement):
        var=(liste_somme_placeoccup_voiture[i]-moy_liste_voiture)**2
        somme_varx=somme_varx+var
    varx=element*somme_varx #je calcule la variance des voitures
    
    for i in range(nombre_delement):
        var=(liste_somme_placeoccup_velo[i]-moy_liste_velo)**2
        somme_vary=somme_vary+var
    vary=element*somme_vary #je calcule la variance des vélos
    
    multi_var=varx*vary
    racine_var=sqrt(multi_var)
    coefficient_correlation=covxy/racine_var #Formule du coefficient de correlation
    print(f' le coefficient de correlation est : {coefficient_correlation}')


""" Ici vous retrouverez les appels des différentes fonction permettant de sortir les données. Pour les utilisez il suffit d'enlever les '#' """

#ressort_global()

donnee_corelation = dat_file()

correlation(donnee_corelation[0],donnee_corelation[1])
