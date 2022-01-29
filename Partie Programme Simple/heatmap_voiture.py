import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Index=['13','14','15','16','17','18','19','20']
Colonne=['1','2','3','4','5','6','7','8']

df = pd.DataFrame([[6332,6223,6120,5830,5532,5120,4932,5045],
                    [6125,6223,5940,5765,5320,5225,5200,4923],
                    [6283,6123,6420,5926,5758,5445,5100,5122],
                    [5973,6153,6042,5821,5923,5623,5213,5159],
                    [6169,6122,5923,5723,5312,5234,5420,5010],
                    [5922,6278,6149,5932,5634,5323,5126,4958],
                    [6146,6439,6334,6024,5979,5738,5584,5392],
                    [6214,5949,6034,5795,5529,5383,5203,5135]], columns=Colonne, index=Index )

  
hm = sns.heatmap(df) 

plt.title('Heatmap taux occupation voiture en fonction des jours/heures')
plt.xlabel('Jour')
plt.ylabel('Heure')
plt.show()