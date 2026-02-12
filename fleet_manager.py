def init_database(): #fn1 (Database)
#Data-points
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Acting Ensign"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = [1, 2, 3, 4, 5]
    return names, ranks, divs, ids

def display_menu(): #fn2 (Interface)
    print("\n---Initilising Fleet Manager---")
    print("   Welcome to Fleet Manager   ")
    
    print("=========================")
#Login    
    login = input("Enter Full Name: ").strip().title()
    print(f"Logged in as: {login}")
    
    print("=========================") 
#Interface
    print("\n----- Options -----")
    print("1. Add Members")
    print("2. Remove Members")
    print("3. Update Ranks")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Diviosn")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit & logout")
#input choice
    choice = input("\nChoose an option: ")
    return choice

def add_member(names, ranks, divs, ids): #fn3 (opt 1)
#New members inputs
    name = input("Enter name: ").strip().title()
    rank = input("Enter rank: ").strip().title()
    division = input("Enter Divison (Command/Operations/Sciences): ").strip().title()
    new_id = int(input("Enter crew ID: ").strip())
#validations
    valid_ranks = [ 
         "Captain", "Commander", "Lieutenant Commander", 
        "Lieutenant", "Acting Ensign"
    ]
    valid_divisions = [
        "Command","Operations","Sciences"
        ]
#Statements
    if rank not in valid_ranks:
        print("Invalid Rank. Please choose from; Captain, Commander," \
        " Lieutentant Commander, Lieutenant, Acting Ensign.")
        return
    
    if division not in valid_divisions:
        print("invalid Divison. Choose from; Command, Operations, Sciences.")
        return
    
    if new_id in ids:
        print("ID already exists.")
        return
#Appends    
    names.append(name)
    ranks.append(rank)
    divs.append(division)
    ids.append(new_id)

    print(f"{rank} {name} added to crew.")

def remove_member(names, ranks, divs, ids): #fn4 (opt 2)
#Attempt to Convert input into an interger    
    try: 
        sel_id = int(input("Enter ID to remove: ").strip())
#Runs of conversion fails, Stops programme termination        
    except ValueError: 
        print("ID must be a number.")
        return
#Checks if selected ID is in datapoint, ids   
    if sel_id not in ids: 
        print("ID entered was not found.")
        return
#Finds postion of selected ID, links all parrallel lists    
    idx = ids.index(sel_id) 
    removed_crew = names[idx] 
#Removes all data corressponding to the selected remove ID
#Keep datapoint order synced
    names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)

    print(f"{removed_crew} was removed from crew.")

def update_rank(names, ranks, ids): #fn5 (opt 3)
    valid_ranks = [ 
         "Captain", "Commander", "Lieutenant Commander", 
        "Lieutenant", "Acting Ensign"
    ]    
#Attempt to Convert input into an interger    
    try: 
        sel_id = int(input("Enter ID: ").strip())
#Runs of conversion fails, Stops programme termination        
    except ValueError: 
        print("ID must be a number")
        return
#Checks if selected ID is in datapoint, ids   
    if sel_id not in ids: 
        print("ID entered was not found.")
        return
#Links selected ID to all lists in database
    idx = ids.index(sel_id)
    new_rank = input("Enter new rank: ").strip().title()

    if new_rank not in valid_ranks:
        print("Invalid Rank. Please choose from; Captain, Commander," \
        " Lieutentant Commander, Lieutenant, Acting Ensign.")
        return
  #Assigns new rank to selected ID, replaces old rank  
    old_rank = ranks[idx]
    ranks[idx] = new_rank

    print(f"{names[idx]}'s rank successfully updated from {old_rank} to {new_rank}.")
    
def display_roster(names, ranks, divs, ids): #Fn6 (Opt 4)
    if len(names) == 0:
#Displays info text instead of table
        print("Roster is empty.")
        return
#Table format for Roster
    print("\n-------------------- Crew Roster --------------------")
    print(f"{'ID':<5} {'NAME':<12} {'RANK':<22} {'DIVISON':<12}")
    print("-----------------------------------------------------")

    for i in range(len(names)):
        print(f"{ids[i]:<5} {names[i]:<12} {ranks[i]:<22} {divs[i]:<12}")

    print("-----------------------------------------------------")

def search_crew(names, ranks, divs, ids): #Fn7 (Opt 5)
    



    

    





