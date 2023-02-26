import pandas as pd

#Nom du csv
name = "result.csv"

#On ouvre le csv
df = pd.read_csv("test.csv")

#Tableau des colonnes à supprimer
column_remove = [
    'Series_reference',
    'Suppressed',
    'STATUS',
    'UNITS',	
    'Magnitude',
    'Subject',	
    'Group',
    'Series_title_1',
    'Series_title_3',
    'Series_title_4',
    'Series_title_5'
]

#On supprime les colonnes indésirables
df = df.drop(columns = column_remove)

#On initialise les variables pour chaque colonne
Period         = []	
Data_value     = []	
Series_title_2 = []

#On parcours le DataForm du CSV
for index, row in df.iterrows():
    #On récupère les lignes avec les valeurs suivantes
    if row["Series_title_2"] == "Credit" or row["Series_title_2"] == "Debit" or row["Series_title_2"] == "Services":
        Period.append(row["Period"])
        Data_value.append(row["Data_value"])
        Series_title_2.append(row["Series_title_2"])

#Création de l'objet result avec les différents tableaux 
result = {
    "Period"         : Period,
    "Data_value"     : Data_value,
    "Series_title_2" : Series_title_2
}

#Création du Data frame avec les valeurs finales (On supprime les lignes vides)
rt = pd.DataFrame(result).dropna()

#Ajout de la colonne 'id' auto incrémentée
rt.insert(0, "id", range(1, len(rt) + 1))

#On crée le csv
rt.dropna().to_csv(name, index=False)