import csv
import os




def deterministe(automate_csv):
    transitions = {}
    etats = []
    alphabet = []
    etat_initial = None

    # Lire le fichier CSV
    with open(automate_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Ignorer les quatre premières lignes
        for _ in range(4):
            next(csv_reader)

        # Parcourir les lignes du fichier CSV à partir de la ligne 5
        for row in csv_reader:
            premier_etat = row[0]
            deuxieme_etat = row[1]
            entree = row[2]

            # Ajouter les états à la liste des états (sans doublons)
            if premier_etat not in etats:
                etats.append(premier_etat)
            if deuxieme_etat not in etats:
                etats.append(deuxieme_etat)

            # Ajouter le symbole d'entrée à la liste de l'alphabet (sans doublons)
            if entree not in alphabet:
                alphabet.append(entree)

            # Si c'est la première transition, définir l'état initial
            if etat_initial is None:
                etat_initial = premier_etat

            # Vérifier si une transition pour cet état et ce symbole existe déjà
            if premier_etat in transitions and entree in transitions[premier_etat]:
                print(f"Transition redondante : {premier_etat} --{entree}--> {transitions[premier_etat][entree]}")
                return False  # Automate non déterministe

            # Ajouter la transition à la liste des transitions
            if premier_etat not in transitions:
                transitions[premier_etat] = {}
            transitions[premier_etat][entree] = deuxieme_etat

    # Vérifier si chaque état a une transition pour chaque symbole de l'alphabet
    for etat in etats:
        if etat not in transitions:
            print(f"État sans transition : {etat}")
            return False

    # Vérifier si l'état initial et l'état final sont bien définis


    return True





'''''''''''
deterministe:
Il possède un unique état initial.
Il ne possède pas d’epsilon-transitions.
Pour chaque état de cet automate, il existe au maximum une transition issue de cet état possédant le même symbole.

complet:
Depuis n’importe quel état, tous les symboles de l’alphabet doivent appartenir au moins une fois aux transitions (sortantes).
Pour obtenir un automate équivalent, complet, il suffit de créer un état “puits”, ou état “poubelle”. 

emondé:
Un automate est dit émondé (ou utile) si tous les états de cet automate peuvent former au moins un mot du langage.
Par exemple : Cet automate est fini émondé. q0, q1 et q3 peuvent servir tous les 3 à la création du langage.
'''''''''



