from create import *
import os


#menu central
def menu():
    for i in range (10):
        print("\n")  
    print("----------------------------")
    print("Select an option :")
    print("1. Créer un automate")
    print("2. Modifier un AEF")
    print("3. Supprimer un  AEF")
    print("4. Verification")
    print("5. Ameliorer l'AEF")
    print("6. Exit")
    print("----------------------------")

    option = input("Faire votre choix>> ")
    if option == "1":
        create()
    elif option == "2":
        modifier()
    elif option == "3":
        supprimer()
    elif option == "4":
        verif()
    elif option == "5":
        improve()
    elif option == "6":
        print("Goodbye !")
        exit()
    else:
        print("Choix invalide. Choisir une option valide (1-6).")

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

def modifier():
    for i in range(10):
        print("\n")

    fichierExistence()  

    file_name = input("Entrez le nom du fichier CSV à modifier : ")
    csv_folder = "csv"
    csv_file_path = os.path.join(csv_folder, file_name)

    while not os.path.exists(csv_file_path):

        print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
        file_name = input("Entrez le nom du fichier CSV à modifier : ")
        csv_folder = "csv"
        csv_file_path = os.path.join(csv_folder, file_name)
        
        if os.path.exists(csv_file_path):
            exit
    
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Modifier les états")
    print("2. Supprimer des transitions")
    print("3. Ajouter des transitions")
    print("4. Terminé")
    print("~~~~~~~~~~~~~~~~~~~~~~~")

    option = input ("Faire votre choix >> ")

    if option == "1":
        modification(csv_file_path)
    elif option == "2":
        delete()
    elif option == "3":
        add()
    elif option == "4":
        menu()
        exit
    else:
        print("Choix invalide. Choisir une option valide")

# menu pour acceder a toutes les verifications 
def verif():
    for i in range (10):
        print("\n")
    print("#######################")
    print("Select an option de vérification :")
    print("1. Si un mot est reconnu")
    print("2. Si un AEF est deterministe")
    print("3. Si un AEF est complet")
    print("4. Si un AEF est unitaire")
    print("5. Si un AEF est equivalent")
    print("6. Retours")


    print("#######################")
    option = input("Faire votre choix>> ")
    if option == "1":
        mot(automate, mot)
    elif option == "2":
        complet(csv_file_path)
    elif option == "3":
        deterministe()
    elif option == "4":
        unitaire()
    elif option == "5":
        equivalence()
    elif option == "6":
        menu()
        exit
    else:
        print("Choix invalide. Choisir une option valide (1-6).")

#menu pour acceder aux améliorations possibles
def improve():
    for i in range (10):
        print("\n")

    print("|||||||||||||||||||||||||||")
    print("Select an option pour améliorer l'AEF :")
    print("1. Rendre un automate complet")
    print("2. Rendre un automate deterministe")
    print("3. Rendre un automate émondé")
    print("4. Rendre un automate minimal")
    print("5. Retour")
    print("|||||||||||||||||||||||||||")

    option = input("Faire botre choix>> ")
    if option == "1":
        AEF_complet()
    elif option == "2":
        AEF_deterministe()
    elif option == "3":
        emonde()
    elif option == "4":
        minimal()
    elif option == "5":
        menu()
    else:
        print("Choix invalide. Choisir une option valide (1-5).")