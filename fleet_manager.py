def init_database(): #1
    names = ["Pike", "Spock", "Scott", "Uhura", "Chekov"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    divs = ["Command", "Science", "Operations", "Operations", "Operations"]
    ids = ["001", "002", "003", "004", "005"]
    return names, ranks, divs, ids
init_database()

def display_menu():
    print("\n---Initilising Fleet Manager---")
    print("   Welcome to Fleet Manager   ")

    print("\n=========================")
    login = input("Enter Full Name: ").title().strip()
    print(f"Logged in as: {login}")
    print("=========================") 

    




display_menu()



