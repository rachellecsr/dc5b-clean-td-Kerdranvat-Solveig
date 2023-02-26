import pandas as pd

#Nom du csv
name = "tondeuse.csv"

#Initialisation des tabs pour l'objet data
Ids       = []
Nom       = []
Puissance = []
Autonomie = []
Energie   = []

#On rempli les 5 tableaux avec 19 entrées (transformation du compteur i en string pour concaténer)
for i in range(19):
    Ids.append(i+1)
    Nom.append("Tondeuse " + str(i+1))
    Puissance.append(1200)
    Autonomie.append(90)
    Energie.append(220)

#Création de l'objet Data avec les différents tableaux
data = {
    'Id'                 : Ids,
    'Nom de la tondeuse' : Nom,
    'Puissance'          : Puissance,
    'Autonomie'          : Autonomie,
    'Energie'            : Energie
} 

#Création du Data frame
df = pd.DataFrame(data)

#On crée le csv avec l'objet data et le nom du CSV
df.to_csv(name , index=False)