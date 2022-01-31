def log_write(content):
    """ crée un fichier / alimente un fichier log """


    station_name = "./station_file/log.txt" # trouve le nom de la station puis rajoute l'extention .txt pour le fichier 

    fichier = open(station_name,"a",encoding='utf8') # ouvre le fichier en mode écriture ( si inexistant : création file )

    fichier.write(content+"\n")                           # écrit dans le fichier le contenu de la page web

    fichier.close()                                  # ferme proprement le fichier