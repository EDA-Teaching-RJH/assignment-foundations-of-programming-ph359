def init_database(): #1
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Acting Ensign"]
    divs = ["Command", "Science", "Operations", "Operations", "Operations"]
    ids = ["001", "002", "003", "004", "005"]
    return names, ranks, divs, ids

init_database()

def display_menu(): #2
    print("\n---Initilising Fleet Manager---")
    print("   Welcome to Fleet Manager   ")
    
    print("=========================")
    
    login = input("Enter Full Name: ").title().strip()
    print(f"Logged in as: {login}")
    
    print("=========================") 

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

    choice = input("\nChoose an option: ")
    return choice

display_menu()

def add_member(names, ranks, divs, ids):
    name = input("Enter name: ").title().strip()
    rank = input("Enter rank: ").title().strip()
    division = input("Enter Divison (Command/Operations/Sciences): ").title().strip()
    new_id = input(int("Enter crew ID: ")).strip()

    valid_ranks = [
        "Captain", "Commander", "Lieutenant Commander", 
        "Lieutenant", "Acting Ensign"
    ]
    valid_divisions = [
        "Command","Operations","Sciences"
        ]

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
    
    names.append(name)
    ranks.append(rank)
    divs.append(division)
    ids.append(new_id)

    print(f"{name} added to crew")

add_member()
                


