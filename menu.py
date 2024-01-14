from AEF import *
import csv




automate=Automate()

 
#main menu
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
    print("\033[38;5;120m|\033[0m 7. ~Display                                \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 8. ~Unit Tests                             \033[38;5;120m|\033[0m")
    print("\033[38;5;120m|\033[0m 9. ~Exit                                   \033[38;5;120m|\033[0m")
    print("\033[38;5;120m└============================================┘\033[0m")

    try:
        option = int(input("Select a number >> "))
    except:
        menu()
    match(int(option)):
        case 1:
            print("\nWelcome in Creation!\n")
            automate.create()
        case 2:
            print("\nWelcome in Modification!\n")
            automate.modifier()
        case 3:
            print("\nWelcome in Deletion!")
            automate.supprimer()
        case 4:
            print("\nWelcome in Verification!")
            verif()
        case 5:
            print("\nWelcome in Improvement!")
            improve()
        case 6:
            print("\nWelcome in Operation!")
            operation()
        case 7:
            automate.afficher()
        case 8:
            print("Automaton's Importation")
            try:
                automate.importCSV("test")
                print("Automaton import successed")
            except:
                print("Automation import failed")
            
            print("Is 'abab' recognized ?")
            try:
                if(verifier_mot(automate,"abab")):
                    print("abb is recognized")
                else:
                    print("abb isn't recognized")
                
                
            except:
                print("word verification failed")
            
            print("Is the automaton complete ?")
            
            try:
                if(automate.estComplet("test")):
                    print("automaton is complete")
                else:
                    print("automaton isn't complete")
            except:
                print("Complete automaton verification failed ")
                
            print("Is the automaton deterministic ?")
            
            try:
                if(automate.estDeterministe()):
                    print("automaton is deterministic")
                else:
                    print("automaton isn't deterministic")
            except:
                print("Deterministic automaton verification failed ")
               
            print("Is the automaton and itself are equivalent (supposed to be true)?")
            
            try:
                if(automate.equivalence(automate)):
                    print("automaton and itself are equivalent")
                else:
                    print("automaton and itself aren't equivalent(failed)")
            except:
                print("Automaton equivalence failed ")
            
                
            print("Make the automaton deterministic")
            try:
                automate1=Automate()
                automate1.importCSV("test")
                automate1.deterministe()
                print(f"Is automaton deterministic ? True = success False = fail: {automate1.estDeterministe()}")
                with open("csv/testDeterministic", mode='w', newline='') as file:
                    writer = csv.writer(file)
                        
                    # Écrire les données dans le fichier CSV
                    writer.writerow(['Initial State', automate1.initial])
                    final= " ".join(automate1.final)
                    writer.writerow(['Final State', final])
                    writer.writerow([])
                    writer.writerow(['First State', 'Second State', 'Event'])
                    for transition in automate1.transition:
                        writer.writerow(transition)   
                    print("\n")
                    print(f"Data has been saved in csv/testDeterministic.")
            except:
                print("Make deterministic the automaton failed")
            
            print("Generating in csv/TestComplementary the complementary of our automaton")
            try:
                automate.complement()
                with open("csv/TestComplementary", mode='w', newline='') as file:
                    writer = csv.writer(file)
                        
                    # Écrire les données dans le fichier CSV
                    writer.writerow(['Initial State', automate.initial])
                    final= " ".join(automate.final)
                    writer.writerow(['Final State', final])
                    writer.writerow([])
                    writer.writerow(['First State', 'Second State', 'Event'])
                    for transition in automate.transition:
                        writer.writerow(transition)   
                    print("\n")
                    print(f"Data has been saved in csv/TestComplementary.")
                print("Complementary of the FSA saved successfully.")
            except:
                print("Complementary failed")
            
            print("Generating in csv/testMirror the mirror of our automaton")
            try:
                automate.miroir()
                with open("csv/TestMirror", mode='w', newline='') as file:
                    writer = csv.writer(file)
                        
                    # Écrire les données dans le fichier CSV
                    writer.writerow(['Initial State', automate.initial])
                    final= " ".join(automate.final)
                    writer.writerow(['Final State', final])
                    writer.writerow([])
                    writer.writerow(['First State', 'Second State', 'Event'])
                    for transition in automate.transition:
                        writer.writerow(transition)   
                    print("\n")
                    print(f"Data has been saved in csv/TestMirror.")
                print("Mirror of the FSA saved successfully.")
            except:
                print("Mirror failed")
                
            print("Generating in csv/testProduct the product between mirror and complementary")
            try:
                automate1=Automate()
                automate2=Automate()
                automate3=Automate()
                automate2.importCSV("TestMirror")
                automate3.importCSV("TestComplementary")
                automate1=automate2*automate3
                with open("csv/testProduct", mode='w', newline='') as file:
                    writer = csv.writer(file)
                        
                    # Écrire les données dans le fichier CSV
                    writer.writerow(['Initial State', automate1.initial])
                    final= " ".join(automate1.final)
                    writer.writerow(['Final State', final])
                    writer.writerow([])
                    writer.writerow(['First State', 'Second State', 'Event'])
                    for transition in automate1.transition:
                        writer.writerow(transition)   
                    print("\n")
                    print(f"Data has been saved in the file csv/testProduct.")
                print("Product saved successfully.")
            
            except:
                print("Product failed")        
                
            print("Generating in csv/testConcatenation the concatenation of mirror automaton and the complementary")
            try:
                
                automate2.importCSV("TestComplementary")
                automate3.importCSV("TestMirror")
                
                
                automate1=automate2+automate3
                
                
                with open("csv/testConcatenation", mode='w', newline='') as file:
                    writer = csv.writer(file)
                        
                    # Écrire les données dans le fichier CSV
                    writer.writerow(['Initial State', automate1.initial])
                    final= " ".join(automate1.final)
                    writer.writerow(['Final State', final])
                    writer.writerow([])
                    writer.writerow(['First State', 'Second State', 'Event'])
                    for transition in automate1.transition:
                        writer.writerow(transition)   
                    print("\n")
                    print(f"Data has been saved in the file csv/testConcatenation.")
                print("Concatenation saved successfully.")
            
            except:
                print("concatenation failed")
                
            print("Generating regular expression for the automata test ")
            try:
                automate.importCSV("test")
                print("Regular expression : "+automate.regex())
            except:
                print("Regular expression failed")

            
                
            
        case 9:
            print("Goodbye !")
            exit(0)
        case _:
            print("Invalid choice. Choose a valid option (1-7).")
    menu()
        

# verification menu
def verif():
    print("\n"*5)
        
    print("\033[38;5;120m----------------------------------------------------------\033[0m")
    print("                    Select an option :            ")
    print("1. If a word is recognized")
    print("2. If an automaton is complete")
    print("3. If an automaton is deterministic")
    print("4. If two automata are equivalent")
    print("5. Return")
    print("\033[38;5;120m----------------------------------------------------------\033[0m")

    option = input("Select a number >> ")
    match(int(option)):
        case 1:
            mot()
        case 2:
            nomCsv=input("Enter the name of the file you want to import: ")
            automate.importCSV(nomCsv)
            if(automate.estComplet(nomCsv)):
                print("This is a complete automaton.")
            else:
                print("This is not a complete automaton.")
        
        case 3:
            nomCsv=input("Enter the name of the file you want to import: ")
            automate.importCSV(nomCsv)
            if(automate.estDeterministe()):
                print("This is a deterministic automaton.")
            else:
                print("This is not a deterministic automaton.")
        case 4:
            automate2=Automate()
            nomCsv=input("Enter the name of the file 1 you want to import: ")
            automate.importCSV(nomCsv)
            nomCsv=input("Enter the name of the file 2 you want to import: ")
            automate2.importCSV(nomCsv)
            if(automate.equivalence(automate2)):
                print("These Automata are equivalents")
            else:
                print("These Automata aren't equivalents")
        case 5:
            menu()       
        case _:
            print("Invalid choice. Choose a valid option (1-6).")

#improvement menu
def improve():

    print("\n"*5)

    print("\033[38;5;120m************************************************************\033[0m")
    print("                    Select an option :            ")
    print("1. Make a complet automaton")
    print("2. Make a deterministic automaton")
    print("3. Make a pruned automaton")
    print("4. Make a minimal automaton")
    print("5. Return")
    print("\033[38;5;120m************************************************************\033[0m")

    option = input("Select a number>> ")
    match(int(option)):
        case 1:
            nomCsv=input("Enter the name of the second file you want to import: ")
            automate.importCSV(nomCsv)
            automate.complet(nomCsv)
            
        case 2:
            nomCsv=input("Enter the name of the file you want to import: ")
            automate.importCSV(nomCsv)
            automate.deterministe()
            with open("csv/"+nomCsv, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                writer.writerow(['Initial State', automate.initial])
                final= " ".join(automate.final)
                writer.writerow(['Final State', final])
                writer.writerow([])
                writer.writerow(['First State', 'Second State', 'Event'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Data has been saved in the file {nomCsv}.")
            print("Your FSA is now deterministic!")
        case 3:
            print("Not available")
        case 4:
            print("Not available")
        case 5:
            menu()
        case _:
            print("Invalid choice. Choose a valid option (1-5).")
        
#operations menu
def operation():
    print("\n"*5)

    print("\033[38;5;120m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
    print("                          Select an option :            ")
    print("1. Complementary")
    print("2. Mirror")
    print("3. Product")
    print("4. Concatenation")
    print("5. Regular Expression")
    print("6. Return")
    print("\033[38;5;120m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
    
    option = input("Select a number>> ")
    
    match(int(option)):
        case 1:
            automate=Automate()
            nomCsv=input("Enter the name of the file you want to import: ")
            sortie=input("Enter the name of the file where you want to stock the complementary: ")
            automate.importCSV(nomCsv)
            automate.complement()
            with open("csv/"+sortie, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                writer.writerow(['Initial State', automate.initial])
                final= " ".join(automate.final)
                writer.writerow(['Final State', final])
                writer.writerow([])
                writer.writerow(['First State', 'Second State', 'Event'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Data has been saved in the file {sortie}.")
            print("Complementary of the FSA saved successfully.")
            
        case 2:
            automate=Automate()
            nomCsv=input("Enter the name of the file you want to import: ")
            sortie=input("Enter the name of the file where you want to stock the mirror: ")
            automate.importCSV(nomCsv)
            automate.miroir()
            with open("csv/"+sortie, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                writer.writerow(['Initial State', automate.initial])
                final= " ".join(automate.final)
                writer.writerow(['Final State', final])
                writer.writerow([])
                writer.writerow(['First State', 'Second State', 'Event'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Data has been saved in the file {sortie}.")
            print("Mirror of the FSA saved successfully.")
        case 3:
            automate2=Automate()
            automate3=Automate()
            nomCsv1=input("Enter the name of the first file you want to import: ")
            nomCsv2=input("Enter the name of the second file you want to import: ")
            sortie=input("Enter the name of the file where you want to stock the product: ")
        
            automate2.importCSV(nomCsv1)
            automate3.importCSV(nomCsv2)
            automate=automate2*automate3
            with open("csv/"+sortie, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                writer.writerow(['Initial State', automate.initial])
                final= " ".join(automate.final)
                writer.writerow(['Final State', final])
                writer.writerow([])
                writer.writerow(['First State', 'Second State', 'Event'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Data has been saved in the file {sortie}.")
            print("Product saved successfully.")
        case 4:
            automate2=Automate()
            automate3=Automate()
            nomCsv1=input("Enter the name of the first file you want to import: ")
            nomCsv2=input("Enter the name of the second file you want to import: ")
            sortie=input("Enter the name of the file where you want to stock the concatenation: ")
        
            automate2.importCSV(nomCsv1)
            automate3.importCSV(nomCsv2)
            
            
            automate=automate2+automate3
            
            
            with open("csv/"+sortie, mode='w', newline='') as file:
                writer = csv.writer(file)
                    
                writer.writerow(['Initial State', automate.initial])
                final= " ".join(automate.final)
                writer.writerow(['Final State', final])
                writer.writerow([])
                writer.writerow(['First State', 'Second State', 'Event'])
                for transition in automate.transition:
                    writer.writerow(transition)   
                print("\n")
                print(f"Data has been saved in the file {sortie}.")
            print("Concatenation saved successfully.")
        case 5:
            automate=Automate()
            nomCsv=input("Enter the name of the file you want to import: ")
            automate.importCSV(nomCsv)
            print(automate.regex())
        case 6:
            menu()
        case _:
            print("Invalid choice. Choose a valid option (1-5).")
            
menu()
