def init_database(): #1
#Data-points
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Acting Ensign"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = ["1", "2", "3" ,"4", "5"]
    return names, ranks, divs, ids

def display_menu(): #2
    print("\n---Initilising Fleet Manager---")
    print("   Welcome to Fleet Manager   ")
    
    print("=========================")
#Login    
    login = input("Enter Full Name: ").strip().title()
    print(f"Logged in as: {login}")
    
    print("=========================") 
#Interface
    print("\n-----Options-----")
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

def add_member(names, ranks, divs, ids): #3 (opt 1)
#New members inputs
    name = input("Enter name: ").strip().title()
    rank = input("Enter rank: ").strip().title()
    division = input("Enter Divison (Command/Operations/Sciences): ").strip().title()
    new_id = int(input("Enter crew ID: "))
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
        " Lieutentant Commander, Lieutenant, Acting Ensign")
        return
    
    if division not in valid_divisions:
        print("invalid Divison. Choose from; Command, Operations, Sciences")
        return
    
    if new_id in ids:
        print("ID already exists.")
        return
#Appends    
    names.append(name)
    ranks.append(rank)
    divs.append(division)
    ids.append(new_id)

    print(f"{name} added to crew")


                


