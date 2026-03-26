i = ["Messi", "Ronaldo", "Neymar", "Bale", "Suarez"]
p = ["RW", "ST", "LW", "CM", "CAM", "GK", "CB", "LB", "RB", "CDM"]
n = ["Argentina", "Portugal", "Brazil", "Wales", "Uruguay"]

def display_menu():
    print("\n--- MENU ---")
    print("1. View Database")
    print("2. Add Player")
    print("3. Remove Player")
    print("4. Update Position")
    print("5. Search Player")
    print("6. Filter by Nationality")
    print("7. Calculate Total Value")
    print("8. Exit")
display_menu()

def display_roster(i, p, n):
        print("Viewing Database...")
        for j in range(len(i)):
            print(i[j] + " - " + p[j] + " - " + n[j])

def add_player(i, p, n):
    print("Adding Player...")
    new_name = input("Name: ")
    new_position = input("Position: ")
    new_nationality = input("Nationality: ")
    i.append(new_name)
    p.append(new_position)
    n.append(new_nationality)

def remove_player(i, p, n):
    print("Removing Player...")
    name_to_remove = input("Name: ")
    if name_to_remove in i:
        index = i.index(name_to_remove)
        i.pop(index)
        p.pop(index)
        n.pop(index)
    else:
        print("Player not found.")

def update_position(i, p):
    print("Updating Position...")
    name_to_update = input("Name: ")
    if name_to_update in i:
        index = i.index(name_to_update)
        new_position = input("New Position: ")
        p[index] = new_position
    else:
        print("Player not found.") 

def search_player(i, p, n):
    print("Searching Player...")
    name_to_search = input("Name: ")
    if name_to_search in i:
        index = i.index(name_to_search)
        print(i[index] + " - " + p[index] + " - " + n[index])
    else:
        print("Player not found.")


