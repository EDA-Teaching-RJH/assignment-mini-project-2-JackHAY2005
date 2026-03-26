i = ["Messi", "Ronaldo", "Neymar", "Bale", "Suarez", "Mbappe", "Lewandowski", "Kane", "Salah", "De Bruyne"]
p = ["RW", "ST", "LW", "LM", "ST", "ST", "ST", "ST", "RW", "CAM"]
n = ["Argentina", "Portugal", "Brazil", "Wales", "Uruguay", "France", "Poland", "England", "Egypt", "Belgium"]
v = [80, 75, 70, 65, 60, 90, 85, 80, 75, 70]
l = []

def display_menu():
    print("\n--- MENU ---")
    print("1. View Database")
    print("2. Add Player")
    print("3. Remove Player")
    print("4. Update Position")
    print("5. Search Player")
    print("6. Filter by Nationality")
    print("7. Calculate Total Value")
    print("8. Count World-Class Players")
    print("9. One on One")
    print("10. Create Starting Lineup")
    print("11. View Starting Lineup")
    print("12. Exit")

def display_roster(i, p, n):
        print("Viewing Database...")
        for j in range(len(i)):
            print(i[j] + " - " + p[j] + " - " + n[j])

def add_player(i, p, n):
    print("Adding Player...")
    new_name = input("Name: ")
    new_position = input("Position: ")
    new_nationality = input("Nationality: ")
    new_value = int(input("Value (in million pounds): "))
    i.append(new_name)
    p.append(new_position)
    n.append(new_nationality)
    v.append(new_value)

def remove_player(i, p, n):
    print("Removing Player...")
    name_to_remove = input("Name: ")
    if name_to_remove in i:
        index = i.index(name_to_remove)
        i.pop(index)
        p.pop(index)
        n.pop(index)
        v.pop(index)
    else:
        print("Player not found.")

def update_position(i, p):
    print("Updating Position...")
    name_to_update = input("Name: ")
    if name_to_update in i:
        index = i.index(name_to_update)
        new_position = input("New Position: ")
        p[index] = new_position
        print("Position updated for " + i[index] + " to " + p[index])
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

def filter_by_nationality(i, p, n):
    print("Filtering by Nationality...") 
    nationality = input("Nationality: ")

    print("Players  from " + nationality + ":")
    for j in range(len(i)):
        if n[j] == nationality:
            print(i[j] + " - " + p[j]) 

def calculate_total_value(i):
    print("Calculating Total Value...")
    total_value = 0
    for value in v:
        total_value += value
    print("Total Value: " + str(total_value) + " million pounds")

def count_World_Class_Players(i, v):
    print("Counting World-Class Players...")
    count = 0
    for j in range(len(i)):
        if v[j] >= 60:
            count += 1
    print("Number of World-Class Players: " + str(count))

def one_on_one(i, p, n):
    print("One on One...")
    player1 = input("Player 1 Name: ")
    player2 = input("Player 2 Name: ")

    if player1 in i and player2 in i:
        index1 = i.index(player1)
        index2 = i.index(player2)

        if v[index1] > v[index2]:
            print(player1 + " dribbles past " + player2 + " and scores!")
        elif v[index1] < v[index2]:
            print(player2 + " dribbles past " + player1 + " and scores!")
    else:
        print("One or both players not found.")

def create_starting_lineup(i, p, n):
    print("Creating Starting Lineup...")
    for j in range(11):
        player_name = input("Player " + str(j+1) + " Name: ")
        if player_name in i:
            l.append(player_name)
        else:
            print("Player not found. Please try again.")
            return

def View_starting_lineup(l, p, n):
    print("Starting Lineup:")
    for player in l:
        index = i.index(player)
        print(player + " - " + p[index] + " - " + n[index])

def run_system():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO THE FOOTBALL PLAYER DATABASE SYSTEM!")

    loading = 0
    while loading < 12:
        loading += 1 # loop was not finished
        print("Loading module " + str(loading))

    while True:
        display_menu()
        opt = input("Select option: ")
        if opt == "1": 
            display_roster(i, p, n)
        elif opt == "2":
            add_player(i, p, n)
        elif opt == "3":
            remove_player(i, p, n)
        elif opt == "4":
            update_position(i, p)
        elif opt == "5":
            search_player(i, p, n)
        elif opt == "6":
            filter_by_nationality(i, p, n)
        elif opt == "7":
            calculate_total_value(i)
        elif opt == "8":
            count_World_Class_Players(i, v)
        elif opt == "9":
            one_on_one(i, p, n)
        elif opt == "10":
            create_starting_lineup(i, p, n)
        elif opt == "11":
            View_starting_lineup(l, p, n)
        elif opt == "12":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Please try again.")
run_system()
