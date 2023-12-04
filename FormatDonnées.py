import pandas as pd

print("\nDonnées actuelles du fichier CSV :")

fichier_csv = 'csv/testcomplet'  # A appliquer au choix de fichier libre
df = pd.read_csv(fichier_csv, delimiter=',', skiprows=range(0, 3))

# fonction pour formater chaque ligne
def formater_ligne(row):
    return f"{row.iloc[0]} ➔ {row.iloc[1]} : {row.iloc[2]}"

# Appliquer la fonction à chaque ligne du DataFrame
df_formate = df.apply(formater_ligne, axis=1)


print(df_formate.to_string(index=False))
