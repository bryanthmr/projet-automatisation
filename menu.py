from fonction import *
from verif2 import *
from modif import *

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
        print("Tu as choisi 'Modifier un AEF'.")
        modifier2()
    elif option == "3":
        supprimer()
    elif option == "4":
        verif()
    elif option == "5":
        improve()
    elif option == "6":
        print("Goodbye !")
        exit
    else:
        print("Choix invalide. Choisir une option valide (1-6).")
        

# menu pour acceder a toutes les verifications
def verif():
    for i in range (10):
        print("\n")
    # Demande à l'utilisateur le nom du fichier CSV à modifier
    #point negatif : il faut se rappeler du nom 
    print("Voici les fichiers déjà existants: zyjgzydgdg ")
    os.system("ls ~/Python/ProjetAutomates/csv |cat")
    #On peut meme afficher les fichier deja exisants et lui demander de choisir sous forme de menu 
    file_name = input("Entrez le nom du fichier CSV à modifier : ")
    csv_folder = "csv"
    csv_file_path = os.path.join(csv_folder, file_name)

    if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
        print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
        return   
    # Lire le fichier CSV existant
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    print("#######################")
    print("Select an option de vérification :")
    print("1. Si un mot est reconnu")
    print("2. Si un automate est complet")
    print("3. Si un automate est deterministe")
    print("4. Si tous les cycles sont unitaires")
    print("5. L'equivalence entre 2 automates")
    print("6. Retour")
    print("########################")

    option = input("Faire votre choix>> ")
    if option == "1":
        mot(automate, mot)
    elif option == "2":
        complet(csv_file_path)
    elif option == "3":

        deterministe(csv_file_path)

        if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
            print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
        else:
            if deterministe(csv_file_path):
                print("L'automate est déterministe.")
            else:
                print("L'automate n'est pas déterministe.")

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


def modifier2():

    print("Tu as choisi 'Modifier un AEF'.")
    
    # Demande à l'utilisateur le nom du fichier CSV à modifier
    #point negatif : il faut se rappeler du nom 
    print("Voici les fichiers déjà existants: ")
    os.system("ls ~/Python/ProjetAutomates/csv |cat")
#On peut meme afficher les fichier deja exisants et lui demander de choisir sous forme de menu 
    file_name = input("Entrez le nom du fichier CSV à modifier : ")
    csv_folder = "csv"
    csv_file_path = os.path.join(csv_folder, file_name)

    if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
        print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
        return
    
    # Lire le fichier CSV existant
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    for i in range (10):
        print("\n")

    print("|||||||||||||||||||||||||||")
    print("Select an option pour modifier l'AEF :")
    print("1. Modifier l'etat initial ou final")
    print("2. Ajouter une ligne")
    print("3. Supprimer une ligne")
    print("5. Retour")
    print("|||||||||||||||||||||||||||")

  

    option = input("Faire votre choix>> ")
    if option == "1":
        ModifierEtat(csv_file_path)
    elif option == "2":
        AjoutLigne()
    elif option == "3":
        SuppLigne()
    elif option == "5":
        menu()
    else:
        print("Choix invalide. Choisir une option valide (1-3).")


