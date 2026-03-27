def __init__(self):
        self.players = FileManager.load()
        self.lineup = []

        # preload if empty
        if not self.players:
            self.players = [
                Player("Messi", "RW", "Argentina", 80),
                Player("Ronaldo", "ST", "Portugal", 75),
                Player("Mbappe", "ST", "France", 90)
            ]

    def view(self):
        for p in self.players:
            print(p)
        
    def add(self):
        name = input("Name: ")
        position = input("Position: ")
        nationality = input("Nationality: ")
        value = input("Value: ")

        if not Utils.validate_name(name):
            print("Invalid name")
            return
        if not Utils.validate_position(position):
            print("Invalid position")
            return
        if not Utils.validate_value(value):
            print("Invalid value")
            return

        self.players.append(Player(name, position, nationality, int(value)))

def run():
    system = FootballSystem()

    while True:
        print("\n1.View 2.Add 3.Remove 4.Search 5.Filter 6.Total 7.WorldClass 8.1v1 9.Lineup 10.ViewLineup 11.Save 12.Tests 13.Exit")
        choice = input("Choice: ")

        if choice == "1": system.view()
        elif choice == "2": system.add()
        elif choice == "3": system.remove()
        elif choice == "4": system.search()
        elif choice == "5": system.filter_nation()
        elif choice == "6": system.total_value()
        elif choice == "7": system.count_world_class()
        elif choice == "8": system.one_on_one()
        elif choice == "9": system.create_lineup()
        elif choice == "10": system.view_lineup()
        elif choice == "11": system.save()
        elif choice == "12": run_tests()
        elif choice == "13": break

run()