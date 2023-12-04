import csv
import os


def ModifierEtat(csv_file_path):

    # Lire le fichier CSV existant
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Affiche les données actuelles
    print("\nDonnées actuelles du fichier CSV :")
    for row in data:
        print(' '.join(row))

    # Demande à l'utilisateur de saisir de nouvelles données
    print("\nEntrez les nouvelles données pour le fichier CSV (ou appuyez sur Entrée pour garder les valeurs actuelles) :")

    # Nouvel état initial
    new_initial_state = input(f"Nouvel état initial ({data[0][1]}): ")
    if new_initial_state:
        data[0][1] = new_initial_state

    # Nouvel état final
    new_final_state = input(f"Nouvel état final ({data[1][1]}): ")
    if new_final_state:
        data[1][1] = new_final_state

    # Écrire les nouvelles données dans le fichier
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("\nLes données ont été mises à jour avec succès.")
