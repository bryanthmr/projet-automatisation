from AEF import *
import csv


automate=Automate()



 
#menu central
def menu():
    
    print("\n"*2)
    print("\033[38;5;120m┌============================================┐\033[0m")
    print("\033[38;5;120m|\033[0m              Select an option :            \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 1. ~Creation                               \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 2. ~Modification                           \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 3. ~Deletion                               \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 4. ~Verification                           \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 5. ~Improvement                            \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 6. ~Operation                              \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 7. ~Exit                                   \033[38;5;120m|\033[0m")
    print("\033[38;5;120m└============================================┘\033[0m")


    option = input("Select a number >> ")
    match(int(option)):
        case 1:
            print("\nWelcome in Creation!\n")
            automate.create()
        case 2:
            automate.modifier()
        case 3:
            print("\nWelcome in Deletion!")
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
            print("Invalid choice. Choose a valid option (1-7).")
    menu()
        

# menu pour acceder a toutes les verifications
def verif():
    print("\n"*5)
        
    print("----------------------------------------------------------")
    print("        Sélectionne une option de vérification :")
    print("1. Si un mot est reconnu")
    print("2. Si un automate est complet")
    print("3. Si un automate est deterministe")
    print("4. Si tous les cycles sont unitaires")
    print("5. L'equivalence entre 2 automates")
    print("6. Retour")
    print("---------------------------------------------------------")

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

    print("************************************************************")
    print("Sélectionne une option pour améliorer l'AEF :")
    print("1. Rendre un automate complet")
    print("2. Rendre un automate deterministe")
    print("3. Rendre un automate émondé")
    print("4. Rendre un automate minimal")
    print("5. Retour")
    print("************************************************************")

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

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Sélectionne une option pour exécuter une opération sur l'AEF :")
    print("1. Complément d'un AEF")
    print("2. Miroir d'un AEF")
    print("3. Produit de 2 AEF")
    print("4. Concaténation de 2 AEF")
    print("5. Retour")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    option = input("Faites votre choix>> ")
    
    match(int(option)):
        case 1:
            nomCsv=input("Entrez le nom du CSV à importer: ")
            sortie=input("Entrez le nom du CSV pour stocker le complémentaire: ")
            automate.importCSV(nomCsv)
            automate.complement()
            with open("csv/"+sortie, mode='w', newline='') as file:
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
                print(f"Les données ont été enregistrées dans le fichier {sortie}.")
            print("Complément de l'AEF terminé")
        case 2:
            nomCsv=input("Entrez le nom du CSV à importer: ")
            sortie=input("Entrez le nom du CSV pour stocker le miroir: ")
            automate.importCSV(nomCsv)
            automate.miroir()
            with open("csv/"+sortie, mode='w', newline='') as file:
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
                print(f"Les données ont été enregistrées dans le fichier {sortie}.")
            print("miroir de l'AEF terminé")
        case 3:
            automate2=Automate()
            automate3=Automate()
            nomCsv1=input("Entrez le nom du CSV de l'automate 1 à importer: ")
            nomCsv2=input("Entrez le nom du CSV de l'automate 2 à importer: ")
            sortie=input("Entrez le nom du CSV pour stocker le produit: ")
        
            automate2.importCSV(nomCsv1)
            automate3.importCSV(nomCsv2)
            automate=automate2*automate3
            with open("csv/"+sortie, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                # Écrire les données dans le fichier CSV
                writer.writerow(['État Initial ', automate.initial])
                final=" ".join(automate.final)
                writer.writerow(['État Final ', final])
                writer.writerow([])
                writer.writerow(['Premier etat', 'Deuxieme etat', 'Entrée'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Les données ont été enregistrées dans le fichier {sortie}.")
            print("Produit de l'AEF terminé")
        case 4:
            automate2=Automate()
            automate3=Automate()
            nomCsv1=input("Entrez le nom du CSV de l'automate 1 à importer: ")
            nomCsv2=input("Entrez le nom du CSV de l'automate 2 à importer: ")
            sortie=input("Entrez le nom du CSV pour stocker la concaténation: ")
        
            automate2.importCSV(nomCsv1)
            automate3.importCSV(nomCsv2)
            
            
            automate=automate2+automate3
            
            
            with open("csv/"+sortie, mode='w', newline='') as file:
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
                print(f"Les données ont été enregistrées dans le fichier {sortie}.")
            print("concaténation de l'AEF terminé")
        case 5:
            menu()
        case _:
            print("Choix invalide. Choisir une option valide (1-5).")

            
