import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Colonne=['16','17','18','19','20'] #Je donne un nom aux huits lignes
Index=['1','2','3','4','5'] #Je donne un nom aux huits colonnes

df = pd.DataFrame([[5830,5532,5120,4932,5045],
                    [5765,5320,5225,5200,4923],
                    [5926,5758,5445,5100,5122],
                    [5821,5923,5623,5213,5159],
                    [5723,5312,5234,5420,5010]], columns=Colonne, index=Index ) #Matrice faite manuellement à partir de donnée du nombre de voiture selon l'heure et le jour

  
hm = sns.heatmap(df) #Création de la carte thermique

plt.title('Heatmap taux occupation voiture en fonction des jours/heures')
plt.xlabel('Heure')
plt.ylabel('Jour')
plt.show()