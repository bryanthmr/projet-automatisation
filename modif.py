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
    return


def SuppTransition(csv_file_path):
    # Lire le fichier CSV existant
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Affiche les données à partir de la ligne 4 avec des indices
    print("\nDonnées actuelles du fichier CSV à partir des transitions avec indices :")
    for i, row in enumerate(data[3:], start=4):
        print(f"{i}. {' '.join(row)}")

    # Demande à l'utilisateur de saisir l'indice de la ligne à supprimer
    while True:
        try:
            index_delete = int(input("Entrez le numéro de la ligne à supprimer (ou '0' pour annuler) : "))
            # Option pour annuler l'opération
            if index_delete == 0:
                print("\nSuppression annulée.")
                return

            # Vérifie si l'indice est valide
            if 4 <= index_delete <= len(data):
                break  # Sort de la boucle si l'indice est valide
            else:
                print("\n\033[91mNuméro de ligne invalide. Veuillez entrer un numéro valide ou '0' pour annuler.\033[0m")
        except ValueError:
            print("\n\033[91mVeuillez entrer un numéro valide ou '0' pour annuler.\033[0m")

    # Supprime la ligne correspondante
    data.pop(index_delete - 1)

    # Écrire les nouvelles données dans le fichier
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("\nLa ligne a été supprimée avec succès.")
    return

def AjoutLigne(csv_file_path):
    # Lire le fichier CSV existant
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Affiche les données à partir de la ligne 4 avec des indices
    print("\nDonnées actuelles du fichier CSV à partir des transitions avec indices :")
    for i, row in enumerate(data[3:], start=4):
        print(f"{i}. {' '.join(row)}")

    # Demande à l'utilisateur de saisir l'indice de la ligne à ajouter
    while True:
        try:
            index_add = int(input("Entrez le numéro de la ligne à ajouter (ou '0' pour annuler) : "))

            # Option pour annuler l'opération
            if index_add == 0:
                print("\nAjout annulé.")
                return

            # Vérifie si l'indice est valide
            if 4 <= index_add <= len(data) + 1:
                break  # Sort de la boucle si l'indice est valide
            else:
                print("\n\033[91mNuméro de ligne invalide. Veuillez entrer un numéro valide ou '0' pour annuler.\033[0m")
        except ValueError:
            print("\n\033[91mVeuillez entrer un numéro valide ou '0' pour annuler.\033[0m")

    new_line = []
    for col_name in ["Premier etat", "Deuxieme etat", "Transitions"]:
        new_value = input(f"Entrez la valeur pour la colonne '{col_name}' : ")
        new_line.append(new_value)

    # Ajoute la nouvelle ligne à la position spécifiée
    data.insert(index_add - 1, new_line)

    # Écrire les nouvelles données dans le fichier
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("\nLa ligne a été ajoutée avec succès.")
    return