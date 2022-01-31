from time import sleep
import threading as th # Bibliothèque permettant de réaliser des tâches de façons asynchrone // installées par défaut avec python3

# Module personnel
import search_park as park
import search_veloMag as vmag
import scraping as scp

def VeloMag():
    """ fonction permettant de faire le scrapping et stockage Vmag"""

    vmag.writer(scp.web_content(id[24]),"vmag","w",".xml")
    vmag.csv_file_writer_parse(scp.xml_vmag_parse("./station_file/vmag.xml"),csv_existe)

def Parking():
    """ fonction permettant de faire le scrapping et stockage Parking"""

    park.csv_file_writer_parse(id[0:24],csv_existe)

def existe_file():
    """fonction permettant de géré l'écriture de l'entête """
    global csv_existe

    sleep(60)
    csv_existe = True


id = ["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO", # Identifiant de chaque parking. L'on aurait pu les récupérés automatiquement
      "FR_MTP_FOCH","FR_MTP_GAMB","FR_MTP_GARE","FR_MTP_TRIA", # mais pour le peu de parking celà aurait pris plus de temps pour rien
      "FR_MTP_ARCT","FR_MTP_PITO","FR_MTP_CIRC","FR_MTP_SABI",
      "FR_MTP_GARC","FR_MTP_SABL","FR_MTP_MOSS","FR_STJ_SJLC",
      "FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109",
      "FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE","FR_MTP_POLY",
      "TAM_MMM_VELOMAG"]



th3 = th.Thread(target=existe_file) # initialisation du thread3 qui va effectuer la fonction donnée dans le target

i=0
csv_existe = False # Dans le cas ou vous voudriez faire un test, merci de bien supprimer touts les fichiers txt / csv / xml

th3.start() # lancement de la tâche

while i<=2016:
    th1 = th.Thread(target=VeloMag)
    th2 = th.Thread(target=Parking)

    th1.start()
    th2.start()

    th1.join() # permet d'attendre que les tâches th1 et th2 soit fini pour lancer la suite
    th2.join()

    sleep(60*10)
    i+=1
    



