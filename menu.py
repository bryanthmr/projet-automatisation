from AEF import *
import csv


automate=Automate()

 
#menu central
def menu():
    
    print("\n"*2) 
    print("----------------------------")
    print("Select an option :")
    print("1. Créer un automate")
    print("2. Modifier un AEF")
    print("3. Supprimer un  AEF")
    print("4. Verification")
    print("5. Ameliorer l'AEF")
    print("6. Opération sur l'AEF")
    print("7. Exit")
    print("----------------------------")

    option = input("Faire votre choix>> ")
    match(int(option)):
        case 1:
            automate.create()
        case 2:
            automate.modifier()
        case 3:
            automate.supprimer()
        case 4:
            verif()
        case 5:
            improve()
        case 6:
            operation()
        case 7:
            print("Goodbye !")
            exit(0)
        case _:
            print("Choix invalide. Choisir une option valide (1-7).")
    menu()
        

# menu pour acceder a toutes les verifications
def verif():
    print("\n"*5)
        
    print("#######################")
    print("Sélectionne une option de vérification :")
    print("1. Si un mot est reconnu")
    print("2. Si un automate est complet")
    print("3. Si un automate est deterministe")
    print("4. Si tous les cycles sont unitaires")
    print("5. L'equivalence entre 2 automates")
    print("6. Retour")
    print("########################")

    option = input("Faites votre choix>> ")
    match(int(option)):
        case 1:
            mot(automate, mot)
        case 2:
            nomCsv=input("Entrez le nom du CSV à importer: ")
            automate.importCSV(nomCsv)
            if(automate.complet()):
                print("L'automate est complet ")
            else:
                print("L'automate n'est pas complet")
        
        case 3:
            nomCsv=input("Entrez le nom du CSV à importer: ")
            automate.importCSV(nomCsv)
            if(automate.estDeterministe()):
                print("L'automate est déterministe ")
            else:
                print("L'automate n'est pas déterministe !")
        case 4:
            automate.unitaire()
        case 5:
            automate.equivalence()
        case 6:
            menu()       
        case _:
            print("Choix invalide. Choisir une option valide (1-6).")

#menu pour acceder aux améliorations possibles
def improve():

    print("\n"*5)

    print("|||||||||||||||||||||||||||")
    print("Sélectionne une option pour améliorer l'AEF :")
    print("1. Rendre un automate complet")
    print("2. Rendre un automate deterministe")
    print("3. Rendre un automate émondé")
    print("4. Rendre un automate minimal")
    print("5. Retour")
    print("|||||||||||||||||||||||||||")

    option = input("Faites votre choix>> ")
    match(int(option)):
        case 1:
            AEF_complet()
        case 2:
            nomCsv=input("Entrez le nom du CSV à importer: ")
            automate.importCSV(nomCsv)
            automate.deterministe()
            with open("csv/"+nomCsv, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                # Écrire les données dans le fichier CSV
                writer.writerow(['État Initial ', automate.initial])
                final= " ".join(automate.final)
                writer.writerow(['État Final ', final])
                writer.writerow([])
                writer.writerow(['Premier etat', 'Deuxieme etat', 'Entrée'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Les données ont été enregistrées dans le fichier {nomCsv}.")
            print("Votre AEF est maintenant déterministe")
        case 3:
            automate.emonde()
        case 4:
            automate.minimal()
        case 5:
            menu()
        case _:
            print("Choix invalide. Choisir une option valide (1-5).")
        
    
def operation():
    print("\n"*5)

    print("|||||||||||||||||||||||||||")
    print("Sélectionne une option pour exécuter une opération sur l'AEF :")
    print("1. Complément d'un AEF")
    print("2. Miroir d'un AEF")
    print("3. Produit de 2 AEF")
    print("4. Concaténation de 2 AEF")
    print("5. Retour")
    print("|||||||||||||||||||||||||||")
    
    option = input("Faites votre choix>> ")
    
    match(int(option)):
        case 1:
            nomCsv=input("Entrez le nom du CSV à importer: ")
            automate.importCSV(nomCsv)
            automate.complement()
            with open("csv/"+nomCsv, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                # Écrire les données dans le fichier CSV
                writer.writerow(['État Initial ', automate.initial])
                final= " ".join(automate.final)
                writer.writerow(['État Final ', final])
                writer.writerow([])
                writer.writerow(['Premier etat', 'Deuxieme etat', 'Entrée'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Les données ont été enregistrées dans le fichier {nomCsv}.")
            print("Complément de l'AEF terminé")
        case 2:
            automate.miroir()
        case 3:
            automate.produit()
        case 4:
            automate.concatenation()
        case 5:
            menu()
        case _:
            print("Choix invalide. Choisir une option valide (1-5).")
            