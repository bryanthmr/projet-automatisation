import os
import csv
from menu import *

def fichierExistence():

    csv_directory = os.path.expanduser("csv")

    # On va demander à l'utilisateur de choisir son fichier :

    # Vérifier si le répertoire existe
    if os.path.exists(csv_directory):
        print("Voici les fichiers déjà existants : ")
        
    # La fonction os.listdir permet d'obtenir la liste des fichiers dans le répertoire en question sur linux et windows
    files = os.listdir(csv_directory)
        
    # Afficher tous les fichiers
    for file in files:
        print(file) 



class Automate:
    
    
    def __init__(self):
        self.initial=""
        self.final=""
        self.transition=[]
        
        
    def importCSV(self,filename):
        if not os.path.exists(f"csv/{filename}"):  # Vérifier si le fichier existe
            print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
            return 0
        file=open(f'csv/{filename}','r')
        reader=csv.reader(file,delimiter=",")
        i=0
        self.transition=[]
        for row in reader:
            i+=1
            
            match(i):
                case 1:
                    self.initial=row[1]
                    
                case 2:
                    self.final=row[1]
                    
                case 3:
                    next(reader)

                case _:
                    self.transition.append([row[0],row[1],row[2]])
                    
        return 1

    
    def create(self):
    
        print("Tu as choisis 'Créer un AEF'.")
        
        # Demander à l'utilisateur le nom du fichier + le mettre dans le dossier et faire les vérifications
        file_name = input("Entrez le nom du fichier CSV : ")
        csv_folder = "csv"

        if not os.path.exists(csv_folder):  # Vérifie si le dossier csv existe sinon le crée
            os.mkdir(csv_folder)
        csv_file_path = os.path.join(csv_folder, file_name)

        if os.path.exists(csv_file_path):  # Vérifie si le fichier existe
            print("\n\033[91mLe fichier existe déjà. Veuillez choisir un autre nom.\033[0m")
        else:
            with open(csv_file_path, mode='w', newline='') as file:  # Donne l'accès pour créer le fichier
                writer = csv.writer(file)
            print("Le fichier CSV a été créé dans le dossier.")

            # Demander à l'utilisateur l'état initial et l'état final
            self.initial = input("Entrez le seul état initial de l'automate : ")
            
            # Vérification si l'utilisateur a entré plusieurs valeurs avec ','
            if ',' in self.initial:
                print("\033[91mErreur : Un automate à état fini possède un seul état initial mais peut avoir plusieurs états finaux.\033[0m\n")
                return

            self.final = input("Entrez l'état final de l'automate : ")

            # Demander à l'utilisateur de saisir les transitions sous forme de matrice
            print("\nEntrez les transitions de votre automate sous forme de matrice (séparez les éléments par des espaces) :")
            print("Pour finir mettre 'ok'\n")
            
            #transitions = []  # Pour stocker les transitions dans une liste

            #on effectue une boucle tant qu'il n'appuie pas sur ok on continu
            while True:
                transition_input = input()
                if transition_input == 'ok':
                    break
                else: #et on regarde la forme 
                    transition_data = transition_input.split()
                    if len(transition_data) != 3:
                        print("\033[91mErreur : Format de transition invalide.\033[0m")
                    else:
                        self.transition.append(transition_data)
            
            # Créer un fichier CSV avec le nom spécifié pour enregistrer les données
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                
                # Écrire les données dans le fichier CSV
                writer.writerow(['État Initial ', self.initial])
                writer.writerow(['État Final ', self.final])
                writer.writerow([])
                writer.writerow(['Premier etat', 'Deuxieme etat', 'Entrée'])
                for transition in self.transition:
                    writer.writerow(transition)   
            print("\n")
            print(f"Les données ont été enregistrées dans le fichier {file_name}.")
            
       
#fonction pour supprimer des automates
    def supprimer(self):
        print("Tu as choisi 'Supprimer un fichier'.")
        # Demande à l'utilisateur le nom du fichier CSV à modifier
        print("Voici les fichiers déjà existants: ")
        fichierExistence()

        # toujours la possibilité de coder un menu contenant tous les fichier csv
        file_name = input("Entrez le nom du fichier CSV à supprimer : ")
        csv_folder = "csv"
        csv_file_path = os.path.join(csv_folder, file_name)
    
        if os.path.exists(csv_file_path):  # Vérifier si le fichier existe
            confirmation = input(f"Êtes-vous sûr de vouloir supprimer le fichier '{file_name}' ? (Oui/Non) : ")
            if confirmation.lower() == 'oui': #condition de verification
                os.remove(csv_file_path)  # Supprimer le fichier
                print(f"Le fichier '{file_name}' a été supprimé.")
            else:
                print(f"Le fichier '{file_name}' n'a pas été supprimé.")
        else:
            print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant à supprimer.\033[0m")

#fonction pour modifier : fait apparaitre le sous menu 
    # ...

    def modifier(self):
        while True:
            print("Tu as choisi 'Modifier un automate")
            # Demande à l'utilisateur le nom du fichier CSV à modifier 
            print("Voici les fichiers déjà existants: ")
            fichierExistence()
        
            file_name = input("Entrez le nom du fichier CSV à modifier : ")
            csv_folder = "csv"
            csv_file_path = os.path.join(csv_folder, file_name)

            if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
                print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
                return

            
            print("\n"*10)

            print("|||||||||||||||||||||||||||")
            print("Select an option pour modifier l'AEF :")
            print("1. Modifier l'etat initial ou final")
            print("2. Ajouter une ligne")
            print("3. Supprimer une ligne")
            print("5. Retour")
            print("|||||||||||||||||||||||||||")
        
            option = input("Faire votre choix>> ")
            if option == "1":
                self.modifier_etat(csv_file_path)  # Passer le nom du fichier à la fonction
            elif option == "2":
                self.ajout_ligne(csv_file_path)
            elif option == "3":
                self.supprimer_ligne(csv_file_path)
            elif option == "5":
                break
            else:
                print("Choix invalide. Choisir une option valide (1-3).")

#fonction pour modifier les etats
    def modifier_etat(self, csv_file_path):
        # Lire le fichier CSV existant
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Vérifier si la liste data a au moins deux éléments (pour éviter l'erreur d'index)
        if len(data) < 2 or len(data[0]) < 2 or len(data[1]) < 2:
            print("Le fichier CSV ne contient pas les données attendues.\n\n")
            return
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
         # Vérification si l'utilisateur a entré plusieurs valeurs avec ','
            if ',' in new_initial_state:
                print("\033[91mErreur : Un automate à état fini possède un seul état initial mais peut avoir plusieurs états finaux.\033[0m\n")
            if ' ' in new_initial_state:
                print("\033[91mErreur : Un automate à état fini possède un seul état initial mais peut avoir plusieurs états finaux.\033[0m\n")
                return
            
        # Nouvel état final
        new_final_state = input(f"Nouvel état final ({data[1][1]}): ")
        if new_final_state:
            data[1][1] = new_final_state

        # Écrire les nouvelles données dans le fichier
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("\n\033[92mLes données ont été mises à jour avec succès.\033[0m")
        return
    
#fonction pour supprimer une ligne 
    def supprimer_ligne(self, csv_file_path):
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
                    print("\n\033[91mNuméro de ligne invalide. Veuillez entrer un numéro valide ou '0' pour annuler.\033[0m\n")
            except ValueError:
                print("\n\033[91mVeuillez entrer un numéro valide ou '0' pour annuler.\033[0m\n")

        # Supprime la ligne correspondante
        data.pop(index_delete - 1)

        # Écrire les nouvelles données dans le fichier
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("\nLa ligne a été supprimée avec succès.")
        return
    


    def ajout_ligne(self, csv_file_path):
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




    def estDeterministe(self):
        transitions = {}
        etats = []
        alphabet = []
        etat_initial = None
        """
        # Lire le fichier CSV
        with open(automate_csv, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

        # Ignorer les quatre premières lignes
        for _ in range(4):
            next(csv_reader)
"""
        # Parcourir les lignes du fichier CSV à partir de la ligne 5
        for trans in self.transition:
            premier_etat = trans[0]
            deuxieme_etat = trans[1]
            entree = trans[2]

            # Ajouter les états à la liste des états (sans doublons)
            if premier_etat not in etats:
                etats.append(premier_etat)
            if deuxieme_etat not in etats:
                etats.append(deuxieme_etat)

            # Ajouter le symbole d'entrée à la liste de l'alphabet (sans doublons)
            if entree not in alphabet:
                alphabet.append(entree)

            """
            inutile je pense 
            # Si c'est la première transition, définir l'état initial
            if self.initial is None:
                 self.initial = premier_etat
            """
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
    
    
    def complet(self):
        transitions = {}
        etats = []
        alphabet = []
        """
        # Lire le fichier CSV
        with open(automate_csv, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Ignorer les quatre premières lignes
            for _ in range(4):
                next(csv_reader)
        """
        # Parcourir les lignes du fichier CSV à partir de la ligne 5
        for trans in self.transition:
            premier_etat = trans[0]
            entree = trans[2]
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


    def deterministe(self):
        mat_trans={}
        lst={}
        new_transition=[]
        etats=set()
        
        
        
        for transition in self.transition:
            transition2=transition.copy()
            etats.update({transition2[0]})
            etats.update({transition2[1]})
           

        
        for etat in etats:
            
            mat_trans[etat]={}
            
        symbole=set()
        for transition in self.transition:
            etat1=transition[0]
            etat2=transition[1]
            car=transition[2]
            symbole.update({car})
            if(mat_trans[etat1].get(car,"nothing")!="nothing"):
                etat2={etat2}
                mat_trans[etat1][car].update(etat2)
            else:
                mat_trans[etat1][car]={etat2}


        i=0
        lst[f'S{i}']={self.initial}
        i+=1
       
        r=set()
        fini=False
        lst_copie=lst.copy()
        etat_fait=[]
        etat_finaux=[]
    
        while len(etat_fait)!=len(lst_copie):
            lst=lst_copie.copy()
            for elt in lst.keys():
                if(elt not in etat_fait):
                    
                    etat_fait.append(elt)
                    for char in symbole:
                        for etat in lst[elt]:
                            if(char in mat_trans[etat].keys()):
                                r.update(mat_trans[etat][char])
                        if(r!=set()):                
                            if (r not in lst_copie.values()):
                                lst_copie[f'S{i}']=r
                                new_transition.append([elt,f'S{i}',char])
                                i+=1
                                
                                r=set()
                            else:
                                key=[k for (k,v) in lst_copie.items() if v==r]
                                etat1=key[0]
                                new_transition.append([elt,etat1,char])
                                r=set()
                              
        self.transition=new_transition
        print(self.transition)
        
        #self.estDeterministe()             
                    
            
            
"""
    if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
        print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
    else:
        if deterministe(csv_file_path):
            print("L'automate est déterministe.")
        else:
            print("L'automate n'est pas déterministe.")


  
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
    """
    
    