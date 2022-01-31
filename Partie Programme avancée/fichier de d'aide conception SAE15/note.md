# Type de livrable ou de production : 

- Codes informatiques développés;
- Démonstration technique commenté;
- et/ou rapport technique avec tutoriel d'installation ; 
- Alimenté le portfolio 
<br>

# méthode de mise en place du programme : 

- Commencer par un Algorithme
- Chercher la doc de "request" pour chercher les données sur internet ( vu en NSI, demander sur discord si c'est pas le bon ( notamment Jules)) .
- Voir également si la biliothèque Selenium peut être utile (utilisé pour aller directement sur un navigateur web [utilisé dans le programme ent/visio])
- a côté de chaque variable : mettre un commentaire pour dire a quoi elle correspond.

<br>

# Obtjectif 
- collecter, traiter, présenter et publier des données.
<br>
<br>

# Collecte de données :
- Mise en place d'une automatisation des données a l'aide de programmes / scripts)
  
  ## Exemples : 
  -  Récupération de la température chaque heure dans une serre agricole,
  -  récupération de l'état du trafic routier,
  -  surveillance de l'état des pations dans un hôpital,
  -  suivi du nombre de cas de personnes positives au Covid-19,
  -  Etc...
  <br>
<br>

  
  ## Web scraping : 
  - Méthode automatique qui permet d'obtenir de grandes quantités de données à partir de sites web. La plupart de ces données sont des données non structurées au format HTML/WML/JSON... qui sont ensuite converties en données structurées dans un tableau ect... 
<br>
<br>

    ### Principe :

    - Crée des données structurée a partir d'un site web avec des données non structurés.
  
  <br>

  
    ### Utilisation : 
    - surveillance des prix
    - étude de marché 
    - apprentissage automatique et intelligence artificielle (IA)
    - Surveillance des actualités
    - Analyse des sentiments 
    - Marketing par couriel

  <br>
<br>

# Traitement des données : 

- Vérifier leur consistance et leur authenticité.
  - exemple : une serre qui dit qu'il fait 500°c dedans ( problè de capteur ou changement de la zone de capture)
- Mise en place de filtrage ( filtrage, élimination des données aberrantes, etc..)
  
<br>

# Analyse des données
- l'écart type 
- moyenne


<br>


# Extraction d'informations : 
  - Extraire uniquement les donnée pertinentes ( moyenne etc..)
<br>
<br>

# présentation des données :

- mise en forme de tableau / graphique
- pouvoir faire des synthèses afin de les exploités
  <br>
<br>

# Publication des données :
- Un fois les données mis en forme il faudra pouvoir les déposés sur un site web

<br>
<br>

# Cas d'étude :

- Données issues du site : https://data.montpellier3m.fr/ Ce sont des donénes mises à la disposition du public par Montpellier Méditerranée Métropole.
- Exemple de données mises à disposition : 
  - Indices de qualité de l'air
  - Occupation des parking de la ville 
  - disponibilité des places vélomag en temps réel
  - Etc..

- Nous utiliserons dans les travaux pratiques les donénes concernatn l'occupation des partiking de la ville.
- Pour chaque parking, un fichier XML donne les informations suivante en temps réel ( exemple pour le parking parking Comédie):

chaque nom en gras est comptenu dans une balise ( pouvant donc permettre de chercher les informations ciblé facilement)<br>

**< park> < /park>** = définit le début et la fin des données<br>
**DateTime** = date de la dernière mise à jour,<br>
**Name** = nom du parking,<br>
**Status** = statut d'ouverture,<br> 
**Free** = Nombre de place libre,<br>
**Total** = nombre total de place.<br>

<br>

# Stripping

# Librairies python a chercher :

-   **requests**
-   **lxml**
-   **time**


# Liens utiles : 

- Documentation lxml python :
  - https://python.doctor/page-xml-python-xpath
<br><br>
- Documentation requests python :
  - https://docs.python-requests.org/en/latest/
<br><br>
- Documentation Sea HeatMap :
  - https://seaborn.pydata.org/generated/seaborn.heatmap.html