import csv
import os

def AutomateCharge(csv_file_path):
    automate = {}
    etat_initial = None
    etat_final = None

    with open(csv_file_path, newline='') as csvfile:
        lecteur = csv.reader(csvfile)
        lignes = list(lecteur)

        # Récupère l'état initial et final 
        etat_initial = lignes[0][1].strip()
        etat_final = lignes[1][1].strip()

        # Construire l'automate
        for ligne in lignes[3:]:
            etat_depart, etat_arrivee, symbole = map(str.strip, ligne)
            automate[(etat_depart, symbole)] = etat_arrivee

    return automate, etat_initial, etat_final

def verifier_mot(automate, etat_initial, etat_final, mot):
    etat_courant = etat_initial

    for symbole in mot:
        transition = (etat_courant, symbole)

        # Vérifier si la transition est définie dans l'automate
        if transition in automate:
            etat_courant = automate[transition]
        else:
            # Si la transition n'est pas définie, le mot n'est pas accepté
            return False

    # Vérifier si l'état final est atteint à la fin du mot
    return etat_courant == etat_final

def testeur():
    while True:
        print("Voici les fichiers déjà existants: ")
        os.system("ls ~/Python/ProjetAutomates/csv | cat")

        # Demander à l'utilisateur d'entrer le nom du fichier CSV à vérifier
        file_name = input("Entrez le nom du fichier CSV à vérifier : ")
        csv_folder = "csv"
        csv_file_path = os.path.join(csv_folder, file_name)

        if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
            print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
            continue  # Revenir au début de la boucle pour redemander le fichier

        # Charger l'automate à partir du fichier CSV
        automate, etat_initial, etat_final = AutomateCharge(csv_file_path)

        while True:
            # Demander à l'utilisateur d'entrer un mot
            UserWord = input("Entrez un mot : ")

            # Vérifier si le mot appartient au langage de l'automate
            if verifier_mot(automate, etat_initial, etat_final, UserWord):
                print("Le mot appartient au langage de l'automate.")
            else:
                print("Le mot n'appartient pas au langage de l'automate.")

            reponse = input("Voulez-vous tester un autre mot? (oui/non) : ")
            if reponse.lower() != 'oui':
                choix = input("Voulez-vous choisir un autre fichier ou retourner au menu principal? (fichier/menu) : ")
                if choix.lower() == 'fichier':
                    break  
                elif choix.lower() == 'menu':
                    return  
                else:
                    print("Choix non valide. Retour au menu principal.")
                    return

# Appel initial de la fonction menu
testeur()
