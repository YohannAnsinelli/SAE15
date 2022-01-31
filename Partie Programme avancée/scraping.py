################
# WEB SCRAPING #
################

import requests
from lxml import etree

def web_content(id):

    """ renvois le contenu de la page recherchée a partir de l'id du parking recherché """

    base_url = "https://data.montpellier3m.fr/sites/default/files/ressources/" 
    extention_url = ".xml" 
    url = base_url+id+extention_url 
    
    
    r = requests.get(url) 
    content = r.text 

    return content


def xml_vmag_parse(xml_path_file):
    """ fonction qui parse le xml"""
    
    result = []

    tree = etree.parse(xml_path_file) # on initialise l'arboressence du fichier
    
    for si in tree.xpath("/vcs/sl/si"): # pour toutes les balises <si> se trouvant encapsulé dans /vcs/sl/
        one_station=[]                  # initialisation / reset de la liste contenant les infomations d'une station

        one_station.append(si.get("na"))  # prend le nom de la station
        one_station.append(si.get("av"))  # prend le nombre de vélo en circulation de la station
        one_station.append(si.get("fr"))  # prend le nombre de vélo libre de la station
        one_station.append(si.get("to"))  # prend le nombre total de vélo de la station

        result.append(one_station)        # prend les informations de chaque station sous forme de liste de liste

    return result   # renvois sous forme de liste de liste le fichier parsé