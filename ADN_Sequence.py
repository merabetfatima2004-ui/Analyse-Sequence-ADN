# Master 1 Génétique
# Chef du projet : Chebab Nesrine
# Lien GitHub : https://github.com/merabetfatima2004-ui/Analyse-Sequence-ADN
# Date : 15/12/2025
# Membres du groupe : Merabet Chaima

import pandas as pd

# 1) Creation du tableau de donnees
data = {
    "Sequence": [
        "ATGCGTACGTA",
        "GCTAGCTAGGCC",
        "ATGCGCGTAAGT",
        "TACGATCGTA",
        "ATGAAAGGCTT",
        "CGTACGTAGC",
        "TTAACCGGAT"
    ],
    "Longueur": [11, 12, 12, 10, 11, 10, 10],
    "Pourcentage_GC": [45.45, 66.67, 58.33, 40, 45.45, 60, 50]
}

df = pd.DataFrame(data)

print("Tableau initial :")
print(df)

# 2) Selection de la colonne Longueur
print("\nColonne Longueur :")
print(df["Longueur"])

# 3) Filtrage longueur > 10
df_filtre = df[df["Longueur"] > 10]
print("\nSequences dont la longueur > 10 :")
print(df_filtre)

# 4) Moyenne GC
moyenne_gc = round(df["Pourcentage_GC"].mean(), 3)
print("\nPourcentage moyen de GC :", moyenne_gc)

# 5) Categorie GC
def categorie_gc(gc):
    if gc > 55:
        return "Riche"
    elif 45 <= gc <= 55:
        return "Moyen"
    else:
        return "Faible"

df["Categorie_GC"] = df["Pourcentage_GC"].apply(categorie_gc)

# 6) Nombre de G
df["Nombre_G"] = df["Sequence"].apply(lambda x: x.count("G"))

# 7) Ecart-type
print("\nEcart-type GC :", round(df["Pourcentage_GC"].std(), 3))
print("Ecart-type Longueur :", round(df["Longueur"].std(), 3))

# 8) Sauvegarde CSV
df.to_csv("analyse_sequences_ADN.csv", index=False)
print("\nFichier CSV sauvegarde avec succes")
