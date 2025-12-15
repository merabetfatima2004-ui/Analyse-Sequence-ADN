#Master 1 Génétique|Merabet fatima|Lien Githup :
http://githup.com /Merabet fatima/ Analyse-Séquece
-ADN | Date : 15/12/2025
#Membre de groupe : Merabet fatima 
import pandas as pd

# 1) Création du tableau de données
data = {
    "Séquence": [
        "ATGCGTACGTA",
        "GCTAGCTAGGCC",
        "ATGCGCGTAAGT",
        "TACGATCGTA",
        "ATGAAAGGCTT",
        "CGTACGTAGC",
        "TTAACCGGAT"
    ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

df = pd.DataFrame(data)

print("Tableau initial :")
print(df)

# 2) Sélection et affichage de la colonne "Longueur"
print("\nColonne Longueur :")
print(df["Longueur"])

# 3) Filtrage des séquences dont la longueur est supérieure à 10
df_filtre = df[df["Longueur"] > 10]
print("\nSéquences dont la longueur > 10 :")
print(df_filtre)

# 4) Calcul du pourcentage moyen de GC (3 chiffres après la virgule)
moyenne_gc = round(df["Pourcentage GC"].mean(), 3)
print("\nPourcentage moyen de GC :", moyenne_gc)

# 5) Ajout de la colonne "Catégorie GC"
def categorie_gc(gc):
    if gc > 55:
        return "Riche"
    elif 45 <= gc <= 55:
        return "Moyen"
    else:
        return "Faible"

df["Catégorie GC"] = df["Pourcentage GC"].apply(categorie_gc)

# 6) Ajout d’une colonne indiquant le nombre de 'G' dans chaque séquence
df["Nombre de G"] = df["Séquence"].apply(lambda x: x.count("G"))

# 7) Calcul de l’écart-type du %GC et de la longueur
ecart_type_gc = df["Pourcentage GC"].std()
ecart_type_longueur = df["Longueur"].std()

print("\nÉcart-type du %GC :", round(ecart_type_gc, 3))
print("Écart-type de la longueur :", round(ecart_type_longueur, 3))

# 8) Sauvegarde du tableau final dans un fichier CSV
df.to_csv("analyse_sequences_ADN.csv", index=False)

print("\nLe tableau final a été sauvegardé dans le fichier 'analyse_sequences_ADN.csv'")
