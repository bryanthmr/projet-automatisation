import os
import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#display the existing files
def fichierExistence():

    csv_directory = os.path.expanduser("csv")

    # verify if the directory exist
    if os.path.exists(csv_directory):
        print("\nHere are the existing files: ")
        
    # os.listdir to display all the files existing in the directory 
    files = os.listdir(csv_directory)
        
    # Afficher tous les fichiers
    for file in files:
        print(file) 

#verification if the word belongs to the language
def verifier_mot(automate, mot):
    etat_courant = automate.initial

    for symbole in mot:
        for transition in automate.transition:
            if (transition[0] == etat_courant) & (transition[2]==symbole):
                etat_courant=transition[1]
                break

    # verification if the final state is reached
    return etat_courant in automate.final

def mot():
        fichierExistence()
     # ask the user to enter the name of the file
        file_name = input("Enter the name of the file you want to use to verify your word : ")
  
        automate=Automate()
        automate.importCSV(file_name)

        while True:
            # ask the user to enter a word
            UserWord = input("Please enter a word: ")

            # verify the function 
            if verifier_mot(automate, UserWord):
                print("This word belongs to the language")
            else:
                print("This word don't belongs to the language")

            reponse = input("Do you want to test another word? (yes/no) : ")
            if reponse.lower() != 'yes':
                choix = input("Do you want to choose another file or return to the main menu? (file/menu) : ")
                if choix.lower() == 'file':
                    break  
                elif choix.lower() == 'menu':
                    return  
                else:
                    print("Invalid choice. Back to main menu.")
                    return


#applies the Arden's lemma to equations
def arden(equation):
    right=equation.split("=")[1]
    left=equation.split("=")[0]
    
    if("+" not in right):
        return equation
    
    acc=0
    d={}
    e=0
    for l in right:
        if(l=="("):
            acc+=1
            if(d.get(f"S{e}","nothing")=="nothing"):
                d[f"S{e}"]=l
            else:
               d[f"S{e}"]=d[f"S{e}"]+l 
        elif(l==")"):
            acc-=1
            d[f"S{e}"]=d[f"S{e}"]+l 
        elif(acc>0):
            d[f"S{e}"]=d[f"S{e}"]+l
        elif(acc==0):
            e+=1
            
    if(d!={}):      
        for elt in d:
            right=right.replace(d[elt],elt)
    
    lst=right.split("+")
    
    for i in range(len(lst)):
        if((left in lst[i]) & (len(lst)>1)):
            if(len(lst[i].split("L")[0])>1):
                tmp=lst[i].split("L")[0]
                if(tmp in d.keys()):
                    if(not((d[tmp][0]=="(") & (d[tmp][-1]==")"))):
                        tmp=f"({tmp})"
                elif(not((tmp[0]=="(") & (tmp[-1]==")"))):
                    tmp=f"({tmp})"
                lst[i]=tmp+"L"+lst[i].split("L")[1]
                lst[i]=lst[i].replace(f"{left}","*")
            else:
                lst[i]=lst[i].replace(f"{left}","*")
            
            tmp=lst[i]
            lst.remove(lst[i])
            if(lst[0]=="ε"):
                lst[0]=tmp
            else:
                
                lst[0]=tmp+lst[0]
            right="+".join(lst)
            if(len(right.split("+"))):
                break
    
    if(d!={}):
        for elt in d:
            right=right.replace(elt,d[elt])
        
    return f"{left}={right}"


#applies the factorisation rules to equations
def factorisation(equation):
    
    right=equation.split("=")[1]
    left=equation.split("=")[0]
    
    if("+" not in right):
        equation=equation.replace("ε","")
        return equation
       
    
    acc=0
    k={}
    e=0
    for l in right:
        if(l=="("):
            acc+=1
            if(k.get(f"S{e}","nothing")=="nothing"):
                k[f"S{e}"]=l
            else:
               k[f"S{e}"]=k[f"S{e}"]+l 
        elif(l==")"):
            acc-=1
            k[f"S{e}"]=k[f"S{e}"]+l 
        elif(acc>0):
            k[f"S{e}"]=k[f"S{e}"]+l
        elif(acc==0):
            e+=1
    
    
    
    if(k!={}):      
        for elt in k:
            right=right.replace(k[elt],elt) 
    d={}
    lst=right.split("+")
    for i in range(len(lst)):
        if(len(lst[i].split("L"))==1):
            d["epsilon"]=lst[i]
            
        elif(d.get(lst[i].split("L")[1],"nothing")!="nothing"):
            d[lst[i].split("L")[1]].append(lst[i].split("L")[0])
        else:
           
            d[lst[i].split("L")[1]]=[lst[i].split("L")[0]] 
    lst=[]  
    for elt in d:
        if(elt=="epsilon"):
            lst.append(f"{d[elt][0]}")
        elif(len(d[elt])>1):
            lst.append(f"({d[elt][0]}+{d[elt][1]})L{elt}")
        else:
            lst.append(f"{d[elt][0]}L{elt}")
        
    

    
    
    right="+".join(lst)
    
    if(k!={}):
        for elt in k:
            right=right.replace(elt,k[elt])
    
    
    return f"{left}={right}"
            
#display the data in the format first state -> second state : event
def Données(csv):
    print("\nYour current file data:")

     # A appliquer au choix de fichier libre
    df = pd.read_csv(csv, delimiter=',', skiprows=range(0, 3))

    # fonction pour formater chaque ligne
    def formater_ligne(row):
        return f"{row.iloc[0]} ➔ {row.iloc[1]} : {row.iloc[2]}"

    # Appliquer la fonction à chaque ligne du DataFrame
    df_formate = df.apply(formater_ligne, axis=1)


    print(df_formate.to_string(index=False))      
            
#define class Automate
class Automate:
    
    
    def __init__(self):
        self.initial=""
        self.final=[]
        self.transition=[]
        
     #import the automata choosen   
    def importCSV(self,filename):
        if not os.path.exists(f"csv/{filename}"):  # Vérifier si le fichier existe
            print("\n\033[91mThis file doesn't exist. Please choose another file.\033[0m")
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
                    self.final=row[1].split(" ")
                    
                case 3:
                    next(reader)

                case _:
                    self.transition.append([row[0],row[1],row[2]])
                    
        return 1

    #create a new automata in a new file and store it in the directory 'csv'
    def create(self):
        
        file_name = input("Enter the file name : ")
        csv_folder = "csv"

        if not os.path.exists(csv_folder):  # verifies if the csv directory exist. If it doesn't exist, creates one
            os.mkdir(csv_folder)
        csv_file_path = os.path.join(csv_folder, file_name)

        if os.path.exists(csv_file_path):  #verifies if the file exist
            print("\033[91mThis name already exists. Please choose another name.\n\033[0m")
            self.create()
        else:
            with open(csv_file_path, mode='w', newline='') as file:  
                writer = csv.writer(file)
            print("\033[38;5;83mYour file has been created successfully!\n\033[0m")

            self.initial = input("Please enter the only initial state: ")
            
            # ensure that there is a only one initial state
            if ',' in self.initial:
                print("\033[91mError: A finite states automaton has only one initial state.\033[0m\n")
                return

            self.final = input("\nPlease enter the final state (if several final states, please separate them with a space): ")

            # ask user to enter transitions as a matrix
            print("\nEnter the transitions of your automaton as a matrix with 'State1 State2 Event'(please separate elements with spaces)")   
            print("For example: q0 q1 a")
            print("Put 'ok' to finish.")
            print("Your turn:\n")

            
            #loop until the user presses ok
            while True:
                transition_input = input()
                if transition_input == 'ok':
                    break
                else: 
                    transition_data = transition_input.split()
                    if len(transition_data) != 3:
                        print("\033[91mError: Invalid transition format.\033[0m")
                    else:
                        self.transition.append(transition_data)
            
            # create csv file with the data
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                
                writer.writerow(['Initial State ', self.initial])
                writer.writerow(['Final State ', self.final])
                writer.writerow([])
                writer.writerow(['First State', 'Second State', 'Event'])
                for transition in self.transition:
                    writer.writerow(transition)   
            print("\n")
            print(f"\033[38;5;83mThe data has been saved in the file {file_name}.\033[0m")

            
       #delete an automata
    def supprimer(self):
        
        
        fichierExistence()

        file_name = input("Enter the name of the file to delete: ")
        csv_folder = "csv"
        csv_file_path = os.path.join(csv_folder, file_name)
    
    #ask a confirmation and delete if the answer is yes
        if os.path.exists(csv_file_path):  
            confirmation = input(f"Are you sure you want to delete the file '{file_name}' ? (Yes/No) : ")
            if confirmation.lower() == 'yes': 
                os.remove(csv_file_path) 
                print(f"\033[38;5;83mThe file '{file_name}' has been deleted.\033[0m")
            else:
                print(f"\n\033[91mThe file '{file_name}' hasn't been deleted.\033[0m")
        else:
            print("\n\033[91mThis file doesn't exist. Please choose another file to delete.\033[0m")

#modification
    def modifier(self):
        while True:
            
            
            fichierExistence()
        
            file_name = input("\nEnter the name of the file to modify: ")
            csv_folder = "csv"
            csv_file_path = os.path.join(csv_folder, file_name)

            if not os.path.exists(csv_file_path): 
                print("\033[91mThis file doesn't exist. Please choose another file.\033[0m")
                self.modifier()
                return
            with open(csv_file_path, mode='r') as file:
                reader = csv.reader(file)
                data = list(reader)
                print(f"\nInitial state: {data[0][1]}")
                print(f"Final state: {data[1][1]}")
            #display the automata with his data
            Données(csv_file_path)

            #menu to select the modification to do
            print("\n"*1)

            print("\033[38;5;120m" + "//////////////////////////////////////////////////////////" + "\033[0m")
            print("             Select an option to modify")
            print("1. Modify initial or final state")
            print("2. Add a line")
            print("3. Delete a line")
            print("4. Exit")
            print("\033[38;5;120m" + "//////////////////////////////////////////////////////////" + "\033[0m")
        
            option = input("Select a number >> ")
            if option == "1":
                self.modifier_etat(csv_file_path) 
            elif option == "2":
                self.ajout_ligne(csv_file_path)
            elif option == "3":
                self.supprimer_ligne(csv_file_path)
            elif option == "4":
                break
            else:
                print("Invalid choice. Choose a valid option (1-4).")

#modify the initial or final states only
    def modifier_etat(self, csv_file_path):
        # Lire le fichier CSV existant
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

        if len(data) < 2 or len(data[0]) < 2 or len(data[1]) < 2:
            print("The file doesn't contain the expected data.\n\n")
            return
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
            print(f"\nInitial state: {data[0][1]}")
            print(f"Final state: {data[1][1]}")

        print("\nEnter the new data (or press Enter to keep the current values)")
        new_initial_state = input(f"New initial state ({data[0][1]}): ")
        if new_initial_state:
            data[0][1] = new_initial_state
            if ',' in new_initial_state:
                print("\033[91mError: A finite states automaton has only one initial state.\033[0m\n")
            if ' ' in new_initial_state:
                print("\033[91mError: A finite states automaton has only one initial state.\033[0m\n")
                return
            
        new_final_state = input(f"New final state ({data[1][1]}): ")
        if new_final_state:
            data[1][1] = new_final_state

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("\n\033[92mData updated successfuly! \033[0m")
        return
    
#delete a line and ask the user to select the index of the line he wants to delete
    def supprimer_ligne(self, csv_file_path):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

        print("\nYour current file data")
        for i, row in enumerate(data[3:], start=4):
            print(f"{i}. {' '.join(row)}")

        while True:
            try:
                index_delete = int(input("Enter the line number to delete (or press '0' to cancel) : "))
                if index_delete == 0:
                    print("Deletion canceled.")
                    return

                if 4 <= index_delete <= len(data):
                    break  
                else:
                    print("\n\033[91mInvalid line number. Please enter a valid number or '0' to cancel.\033[0m\n")
            except ValueError:
                print("\n\033[91mPlease enter a valid number or '0' to cancel.\033[0m\n")

        
        data.pop(index_delete - 1)

      
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("\nThe line was deleted successfully.")
        return
    

#add a line in the file and ask the user to give the new transitions
    def ajout_ligne(self, csv_file_path):
       
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

        print("\nYour current file data : ")
        for i, row in enumerate(data[3:], start=4):
            print(f"{' '.join(row)}")

        new_line = []
        for col_name in ["First State", "Second State", "Event"]:
            new_value = input(f"Enter the value for column '{col_name}' : ")
            new_line.append(new_value)

        data.insert(i, new_line)

        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("\nThe line has been successfully added.")
        return


#verify if the automata is deterministic
    def estDeterministe(self):
        etats=set()
        symbole=set()
        mat_trans={}
        for transition in self.transition:
            transition2=transition.copy()
            etats.update({transition2[0]})
            etats.update({transition2[1]})
           

        
        for etat in etats:
            mat_trans[etat]={}
        
        for transition in self.transition:
            etat1=transition[0]
            etat2=transition[1]
            car=transition[2]
            symbole.update({car})
            if(mat_trans[etat1].get(car,"nothing")!="nothing"):
                mat_trans[etat1][car].update({etat2})
            else:
                mat_trans[etat1][car]={etat2}
        
        verif=True
        for elt in mat_trans:
            for s in symbole:
                if(mat_trans[elt].get(car,"nothing")!="nothing"):
                    if(len(mat_trans[elt][car])>1):
                        verif=False
                        break


        
        return verif


    
#make an automata deterministic 
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
                mat_trans[etat1][car].update({etat2})
            else:
                mat_trans[etat1][car]={etat2}


        i=0
        lst[f'S{i}']={self.initial}
        i+=1
       
        r=set()

        lst_copie=lst.copy()
        etat_fait=[]
        etat_finaux=set()
    
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
        
        for elt in lst:
            for final in self.final:
                if final in lst[elt]:
                    etat_finaux.update({elt})
            
        self.final=list(etat_finaux)
        
        self.initial="S0"
        
  #create the complementary of the automate      
    def complement(self): 
        new_final=set()
        for transition in self.transition:
            t1=transition[0]
            t2=transition[1]
            if t1 not in self.final:
                new_final.update({t1})
            if t2 not in self.final:
                new_final.update({t2})
        
        self.final=list(new_final)
                      
    #create the mirror of the automate      
    def miroir(self):
        new_transition=[]

        
        for transition in self.transition:
            new_transition.append([transition[1],transition[0],transition[2]])
        
        self.transition=new_transition

        if(len(self.final)>1):
            for t in self.transition:
                if(t[0] in self.final):
                    self.transition.append(["S0'",t[1],t[2]])
            self.final=[self.initial]
            self.initial="S0'"
        else:
            final=self.final[0]
            self.final=[self.initial]
            self.initial=final
            
# concatenate two automaton
    def __add__(self,automate2):
        
        lstState={}
        i=0
        for transition in self.transition:
            if(lstState.get(transition[0],"nothing")=="nothing"):
                lstState[transition[0]]=f"C{i}"
                i=1
            if(lstState.get(transition[1],"nothing")=="nothing"):     
                lstState[transition[1]]=f"C{i}"
                i+=1
        
        new_final=[]
        self.initial=self.initial.replace(self.initial,lstState[self.initial])
        for final in self.final:
            new_final.append(final.replace(final,lstState[final]))
        
        self.final=new_final
        
        new_trans=[]
        for transition in self.transition:
            transition[0]=transition[0].replace(transition[0],lstState[transition[0]])
            transition[1]=transition[1].replace(transition[1],lstState[transition[1]])
            new_trans.append(transition)
        
        self.transition=new_trans    
        
        initial=self.initial
        final=automate2.final
        
        transition=[]
        
        for t in self.transition:
            transition.append(t)

        for f in self.final:
            for t in automate2.transition:
                if(t[0] == automate2.initial):
                    transition.append([f,t[1],t[2]])
        
        for t in automate2.transition:
            transition.append(t)
        
        
        
        automate3=Automate()
        automate3.initial=initial
        automate3.final=final
        automate3.transition=transition
        return automate3

#convert an automata in an equations system
    
    def init_equation(self,etat,fait,d,i,equations):
        for t in self.transition:
            if((etat in self.final) & ([etat,"?","ε"] not in fait)):
                if(etat != self.initial):
                    if(d.get(etat,"nothing")=="nothing"):
                        d[etat]=f"L{i}"
                        i+=1
                    equation=f"{d[etat]}=ε"
                    equations.remove(f"{d[etat]}=?")
                    equations.append(equation)
                    
                    fait.append([etat,"?","ε"])
                else:
                    for e in range(len(equations)):
                        if(equations[e].split("=")[0]==d[etat]):
                            equations[e]=equations[e]+"+ε"
            if((t[0]==etat) & (t not in fait)):
                if(d.get(t[0],"nothing")=="nothing"):
                    d[t[0]]=f"L{i}"
                    i+=1
                    fait.append(t)
                    if(d.get(t[1],"nothing")=="nothing"):
                        d[t[1]]=f"L{i}"
                        i+=1
                        equation=f"{d[t[1]]}=?"
                        equations.append(equation)
                    equation=f"{d[t[0]]}={t[2]}{d[t[1]]}"
                    equations.append(equation)
                    
                    
                    self.init_equation(t[1],fait,d,i,equations)
                    
                else:
                    fait.append(t)
                    for e in range(len(equations)):
                        if(equations[e].split("=")[0]==d[t[0]]):
                            if(d.get(t[1],"nothing")=="nothing"):
                                d[t[1]]=f"L{i}"
                                i+=1
                                equation=f"{d[t[1]]}=?"
                                equations.append(equation)
                            if(equations[e].split("=")[1]=="?"):
                                tmp=equations[e].split("=")[1]
                                tmp=f"{t[2]}{d[t[1]]}"
                                
                            else:
                                tmp=equations[e].split("=")[1]
                                tmp=f"{tmp}+{t[2]}{d[t[1]]}"
                                
                            equations[e]=equations[e].split("=")[0]+"="+tmp
                
                    self.init_equation(t[1],fait,d,i,equations)
            
                           

        
        return equations

 #generate a regular expression from the equations system   
    def regex(self):
        
        
        equations=self.init_equation(self.initial,[],{},0,[])
        for i in range(len(equations)):
        
            if("ε+" in equations[i] or "+ε" in equations[i]):
                equations[i]=equations[i].replace("ε+","")
                equations[i]=equations[i].replace("+ε","")
                equations[i]=equations[i]+"+ε"
          
            
            
        
        fait={}
        eq=""
        for i in range(len(equations)-1,-1,-1):
            
            
            for e in equations:
                if((e.split("=")[0]).split("L")[1]==f"{i}"):
                    eq=e
            
            if(eq):
                
                
                right=eq.split("=")[1]
                left=eq.split("=")[0]
                
                
                acc=0
                d={}
                e=0
                for l in right:
                    if(l=="("):
                        acc+=1
                        if(d.get(f"S{e}","nothing")=="nothing"):
                            d[f"S{e}"]=l
                        else:
                            d[f"S{e}"]=d[f"S{e}"]+l 
                    elif(l==")"):
                        acc-=1
                        d[f"S{e}"]=d[f"S{e}"]+l 
                    elif(acc>0):
                        d[f"S{e}"]=d[f"S{e}"]+l
                    elif(acc==0):
                        e+=1
                        
                if(d!={}):      
                    for elt in d:
                        right=right.replace(d[elt],elt) 
                            
                lst=right.split("+")
                for j in range(len(equations)):
                    for elt in lst:
                        if(elt!="ε"):
                            if(elt.split("L")[1] in fait.keys()):
                                eq=eq.replace(f"L{elt.split('L')[1]}",fait[f"{elt.split('L')[1]}"])
                                
                
              
                        
                        
                eq=factorisation(eq)

                
                
                eq=arden(eq)
                
                
            
                fait[left.split("L")[1]]=eq.split("=")[1]
            
        
        return(eq.split("=")[1])
    
#verifies if an automata is complete
    
    def estComplet(self, nomCsv):
        transitions = {}
        etats = []
        alphabet = []

        with open("csv/"+nomCsv, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

     
            for _ in range(4):
                next(csv_reader)

            for row in csv_reader:
                premier_etat = row[0]
                entree = row[2]

                if premier_etat not in etats:
                    etats.append(premier_etat)

                if entree not in alphabet: 
                    alphabet.append(entree)

                if premier_etat not in transitions:
                    transitions[premier_etat] = []

                transitions[premier_etat].append(entree)

        for etat in etats:
            if etat not in transitions:
                return False
            if len(transitions[etat]) != len(alphabet):
                return False

        return True

#makes an automata complete
    def complet(self, nomCsv): # Création d'un état puit et rajout de ce dernier dans le fichier csv de l'automate pour le rendre complet.

        # On vérifie si l'automate est déjà complet.
        if self.estComplet(nomCsv):
            print("L'automate est déjà complet.") # Vérification peut être inutile car c'est le but de la fonction de rendre complet, à voir pour sup ou pas.

        transitions = {}
        etats = []
        alphabet = []

        # Lire le fichier CSV
        with open("csv/"+nomCsv, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Ignorer les quatre premières lignes
            for _ in range(4):
                next(csv_reader)

            # Parcourir les lignes du fichier CSV à partir de la ligne 5
            for row in csv_reader:
                premier_etat = row[0]
                entree = row[2]

                # Ajouter le premier état de la ligne à la liste des états en évitant les doublons avec la condition if
                if premier_etat not in etats:
                    etats.append(premier_etat)

                # Ajouter le symbole d'entrée à la liste de l'alphabet (sans doublons)
                if entree not in alphabet:
                    alphabet.append(entree)

                # Ajouter les transitions à la liste des transitions
                
                if premier_etat not in transitions:
                    transitions[premier_etat] = []
                
                transitions[premier_etat].append(entree)

        unique_transitions = set() # Là on créer un ensemble pour stocker les transitions de manière unique pour éviter les doublons

        # On ajoute un état puit spécifique pour chaque état qui en a besoin
        for etat in etats:
            if etat not in transitions:
                transitions[etat] = []

            # On vérifie les transitions manquantes pour chaque symbole
            for symbole in alphabet:
                # Si la transition n'existe pas, on ajoute une transition vers un état puit s^écifique
                if symbole not in transitions[etat]:
                    puit_numero = self.numero_puit(etat)
                    etat_puit = f"puit{puit_numero}"

                    if etat_puit not in etats:
                        etats.append(etat_puit)

                    if etat_puit not in transitions:
                        transitions[etat_puit] = []

                    # On ajoute la transition à l'ensemble des transitions uniques
                    if "puit" not in etat or ("puit" in etat and "puit" not in etat_puit): # On vérifie que l'état de départ ne soit pas un état puit
                        unique_transitions.add((etat, etat_puit, symbole))
        
        with open("csv/"+nomCsv, mode='a', newline='') as file: # On met en mode ajout pour éviter d'écraser le contenu et de devoir réécrire à chaque fois
            writer = csv.writer(file)
            for transition in unique_transitions:
                if not transition[0].startswith("puit"):
                    writer.writerow(transition)

#gives an only well number for transitions of a particular state

    def numero_puit(self, etat):
        return int(etat[1:]) + 1 if etat[0] == 'q' else 1                      
                        
    
 #product of two automaton
    def __mul__(self, automate2):
        i=0
        lst={}
        
        initial = (self.initial, automate2.initial)
        lst[initial]=f'S{i}'
        i+=1
        initial=lst[initial]

        final = []
        for f1 in self.final:
            for f2 in automate2.final:
                if lst.get((f1, f2),"nothing")== "nothing":
                        lst[(f1, f2)]=f'S{i}'
                        i+=1
                final.append(lst[(f1, f2)])

        transition = []
        for t1 in self.transition:
            for t2 in automate2.transition:
                if t1[2] == t2[2]:
                    if lst.get((t1[0], t2[0]),"nothing")== "nothing":
                        lst[(t1[0], t2[0])]=f'S{i}'
                        i+=1
                        
                    if lst.get((t1[1], t2[1]),"nothing")== "nothing":
                        lst[(t1[1], t2[1])]=f'S{i}'
                        i+=1
                    transition.append([lst[(t1[0], t2[0])],lst[(t1[1], t2[1])],t1[2]])
                
       

        automate_result = Automate()
        automate_result.initial = initial
        automate_result.final = final
        automate_result.transition = transition

        return automate_result
    

    #verify if the regular expressions of the two automaton are the same
    def equivalence(self,automate):
        return self.regex()==automate.regex()
    
    #display the automata selected
    
    def afficher(self):
        while True:
            
            fichierExistence()
        
            file_name = input("\nEnter the name of the file to display: ")
            if(file_name):
                csv_folder = "csv"
                csv_file_path = f"{csv_folder}/{file_name}"
            
                if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
                    print("\033[91mThis file doesn't exist. Please choose another file.\033[0m")
                    break

                G = nx.DiGraph()

                with open(csv_file_path, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  
                    for row in reader:
                        if len(row) == 3:
                            G.add_edge(row[0], row[1], label=row[2])

                with open(csv_file_path, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  
                    for row in reader:
                        if len(row) == 2:
                            if row[0] == 'Initial State':
                                G.nodes[row[1]]['initial'] = True
                            elif row[0] == 'Final State':
                                for i in range(len(row[1].split(' '))):
                                    G.nodes[row[1].split(' ')[i]]['final'] = True

                pos = nx.circular_layout(G)  
                labels = nx.get_edge_attributes(G, 'label')
                initial_states = [node for node, data in G.nodes(data=True) if 'initial' in data and data['initial']]
                final_states = [node for node, data in G.nodes(data=True) if 'final' in data and data['final']]

                nx.draw_networkx_nodes(G, pos, node_size=500,  nodelist=set(G.nodes) - set(initial_states + final_states))
                
                nx.draw_networkx_edges(G, pos)
                nx.draw_networkx_labels(G, pos)

                edge_labels = {(u, v): labels[(u, v)] for u, v in G.edges}
                edge_label_pos = {k: (v[0], v[1] + 0.1) for k, v in pos.items()}  
                nx.draw_networkx_edge_labels(G, edge_label_pos, edge_labels=edge_labels)

                plt.show()          
            else:
                break
            
            
        
            

