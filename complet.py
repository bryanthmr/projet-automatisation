import csv
import os


print("Voici les fichiers déjà existants: ")
os.system("ls ~/Python/ProjetAutomates/csv |cat")
# On peut même afficher les fichiers déjà existants et lui demander de choisir sous forme de menu
file_name = input("Entrez le nom du fichier CSV à vérifier : ")
csv_folder = "csv"
csv_file_path = os.path.join(csv_folder, file_name)

if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
    print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")



def complet(automate_csv):
    transitions = {}
    etats = []
    alphabet = []

    # Lire le fichier CSV
    with open(automate_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Ignorer les quatre premières lignes
        for _ in range(4):
            next(csv_reader)

        # Parcourir les lignes du fichier CSV à partir de la ligne 5
        for row in csv_reader:
            premier_etat = row[0]
            entree = row[2]

            # Ajouter l'état à la liste des états (sans doublons)
            if premier_etat not in etats:
                etats.append(premier_etat)

            # Ajouter le symbole d'entrée à la liste de l'alphabet (sans doublons)
            if entree not in alphabet:
                alphabet.append(entree)

            # Ajouter la transition à la liste des transitions
            if premier_etat not in transitions:
                transitions[premier_etat] = []
            transitions[premier_etat].append(entree)

    # Vérifier si chaque état a une transition pour chaque symbole de l'alphabet
    for etat in etats:
        if etat not in transitions:
            return False
        if len(transitions[etat]) != len(alphabet):
            return False

    return True


if complet(csv_file_path):
    print("L'automate est complet.")
else:
    print("L'automate n'est pas complet.")



