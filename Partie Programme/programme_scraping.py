import requests
import time
from bs4 import BeautifulSoup
from math import *
from lxml import etree



parking_id=['FR_MTP_ANTI.xml','FR_MTP_COME.xml','FR_MTP_CORU.xml','FR_MTP_EURO.xml','FR_MTP_FOCH.xml','FR_MTP_GAMB.xml','FR_MTP_GARE.xml','FR_MTP_TRIA.xml','FR_MTP_ARCT.xml',
            'FR_MTP_PITO.xml','FR_MTP_CIRC.xml','FR_MTP_SABI.xml','FR_MTP_GARC.xml','FR_MTP_SABL.xml','FR_MTP_MOSS.xml','FR_STJ_SJLC.xml','FR_MTP_MEDC.xml','FR_MTP_OCCI.xml',
            'FR_CAS_VICA.xml','FR_MTP_GA109.xml','FR_MTP_GA250.xml','FR_MTP_ARCE.xml','FR_MTP_POLY.xml'] #liste des identifiants

deb_url = 'https://data.montpellier3m.fr/sites/default/files/ressources/' #url des ressources qui va me servir à ajouter les identifiants pour les parkings voiture

velo_url= 'https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml'

velo=requests.get(velo_url)

f1=open("pagecontenu.txt","w", encoding='utf8')
f1.write(velo.text)
f1.close() 
tree = etree.parse("pagecontenu.txt")


heure = 0,1
minute = heure*60



def moyenne(x):
	somme=0
	for i in x: #parcours la liste demandé
		somme=somme+i #boucle pour faire la somme des membres d'une boucle
	moy=somme/len(x) #formule de la moyenne : somme de l'effectif / effectif
	return moy

def ecartype(x):
	somme=0 
	moy=moyenne(x) #j'attribue à une variable la moyenne pour appeler la fonction une seule fois
	for i in x:
		calcul=((i-moy)**2)/len(x) #Je fais tout le calcul de l'écart type sans la racine carré et pour chaque valeur
		somme=somme+calcul #J'additionne à chaque tour mes valeurs pour faire un total
	sigma=sqrt(somme) #j'applique la racine carré à mon total pour trouver sigma
	return sigma
        

def fichier_parking(graph,nombre_echantillon):
    nom_fichier=input('Choisir un nom de fichier pour les voitures : ')
    nom_fichier=str(nom_fichier+'.txt')
    parking=open(nom_fichier,"w",encoding='utf8')#j'ouvre mon fichier pour mettre les données dedans
    
    nom_fichier=input('Choisir un nom de fichier pour les velos : ')
    nom_fichier=str(nom_fichier+'.txt')
    parking_v=open(nom_fichier,"w",encoding='utf8')
    
    echantillon=int(nombre_echantillon)
    while echantillon>0:  #n sera remplacé par le nombre d'heure où je veux récupérer des informations
        #heure=heure-1
        echantillon=echantillon-1
        compteur_park=0 #compteur de parking
        place_total=0 #compteur place total de parking
        place_libre=0 #compteur place libre 
        pourcentage_ville=0 #pourcentage de place libre dans la ville
        place_occup=[] #Liste pour les places occupées
        temps=time.asctime()
        parking.write(time.asctime()) #à l'aide de time j'affiche la date et l'heure du jour où ma boucle se lance
        parking.write('\n\n')
        
        
        for park in parking_id: #je parcours les identifiants
            pourcentage_parking=0
            compteur_park=int(compteur_park)+1
            url=str(deb_url+park) #j'ajoute l'indendifiant à mon url
            reponse = requests.get(url) #j'utilise requests pour récuperer les informations de la page

            soup=BeautifulSoup(reponse.content, features="lxml") #Cela me permet de créer un objet soup qui contient le contenu de la page et ne pas prendre les balises lxml

            first_header = soup.find("name") #je cherche la balise name dans le lxml
            second_header = soup.find("free") #je cherche la balise free
            third_header = soup.find("total") #je cherche la balise total

            donnees=[first_header.text,second_header.text,third_header.text] #l'extension .text avec bs4 me permet d'enlever les balises et de récupérer uniquement la donnée
            présentation=['Nom Parking','Place Libre','Place total','Place occupée'] #liste pour de l'esthétique sur le rendu de mon .txt

            occup=int(third_header.text)-int(second_header.text) #calcul les places occupées
            place_occup.append(occup) #structure de ma liste des places occupées
            occup=str(occup) 
            donnees.append(occup) #j'ajoute la valeur occup à ma liste de donnée

            place_total=place_total+int(third_header.text) #calcul de place total avec la balise total
            place_libre=place_libre+int(second_header.text) #calcul de place libre avec la balise free
            pourcentage_ville=(place_libre*100)/place_total #j'utilise la formule de calcul de pourcentage

            titre='Parking '
            compteur_park=str(compteur_park)
            titre=str(titre+compteur_park) #Ce petit bloc rajoute de l'esthétique pour rajouter un numéro à chaque parking

            pourcentage_parking=(int(second_header.text)*100)/int(third_header.text) #calcul du pourcentage de place libre par parking

            parking.write('\n\n')
            parking.write(titre)
            parking.write('\n\n')
            for i in zip(présentation,donnees): #Boucle qui va parcourir deux listes en même temps pour les mettres en concordances
                i=str(i)
                parking.write(i)
                parking.write('\n')
            pourcentage_parking=str(pourcentage_parking)
            parking.write('Pourcentage Place Libre : ')
            parking.write(pourcentage_parking)
            parking.write('%')
            parking.write('\n\n')
        
        #######VELO#######
        
            
        parking_v.write(temps)
        parking_v.write('\n')
        page=requests.get(velo_url)
        liste_occupv=[]
        
        root=tree.getroot()

        for donneev in root.findall('./sl/si'):
            name = donneev.get('na')
            occupp = donneev.get('av')
            libre = donneev.get('fr')
            total = donneev.get('to')
            
            liste_occupv.append(int(occupp))
            
            parking_v.write('Nom Parking : ')
            parking_v.write(name)
            parking_v.write('\n')
            parking_v.write('Nbr Place occup : ')
            parking_v.write(occupp)
            parking_v.write('\n')
            parking_v.write('Nbr Place libre : ')
            parking_v.write(libre)
            parking_v.write('\n')
            parking_v.write('Place total : ')
            parking_v.write(total)
            parking_v.write('\n')
            parking_v.write('\n')
            
            
            
        gnuplot(place_occup,graph,temps,liste_occupv)
        parking.write('\n')
        moy=moyenne(place_occup)
        moy=str(moy)
        sigma=ecartype(place_occup)
        sigma=str(sigma)
        parking.write('Moyenne de place occupée : ')
        parking.write(moy)
        parking.write('\n\n')
        parking.write('Ecartype de cette moyenne : ')
        parking.write(sigma)
        parking.write('\n\n')
        parking.write('Pourcentage de place libre dans la ville : ')
        pourcentage_ville=str(pourcentage_ville)
        parking.write(pourcentage_ville)
        parking.write('%')
        parking.write('\n\n')
        time.sleep(8) #Fait un tour toute les 8 secondes
    parking.close()

def gnuplot(place_occup,graph,temps,liste_occupv):
    sommeoccup=sum(place_occup)
    sommeoccupv=sum(liste_occupv)
    graph.write('\n')
    temps=temps.split()
    temps=temps[3]
    temps=str(temps)
    temps=temps.replace(':','.')
    sommeoccup=str(sommeoccup)
    sommeoccupv=str(sommeoccupv)
    graph.write(temps)
    graph.write(' ')
    graph.write(sommeoccup)
    graph.write(' ')
    graph.write(sommeoccupv)
    


nombre_echantillon=input('Choisir un nombre d echantillon : ')
graph=open("data.dat","w",encoding='utf8')
graph.write('# Time Placeoccupvoi Placeoccupvelo')
fichier_parking(graph,nombre_echantillon)
graph.close()

#---Pour afficher le graphique---
# cd ! ce mettre dans le bon répertoire
#set terminal png size 700,500 enhanced fname 'arial' fsize 10 butt solid ! Je met l'image en png
#set key inside bottom right
#set xlabel 'Time heure'
#set ylabel 'Nbr Places occupées'
#set title 'graphique parking voiture/velo'
#plot "data.dat" using 1:2 title 'Placeoccupvoiture' with linespoints, "data.dat" using 1:3 title 'Placeoccupvelo' with linespoints
#set output 'C:\Users\Yohann\image.png' ! chemin pour créer mon image
