import re
import csv
# ==========================
# FILE I/O
# ==========================
class FileManager:
    FILE = "players.csv"

    @staticmethod
    def save(players):
        with open(FileManager.FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "position", "nationality", "value"])
            writer.writeheader()
            for p in players:
                writer.writerow(p.to_dict())

    @staticmethod
    def load():
        players = []
        try:
            with open(FileManager.FILE, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    players.append(Player(row["name"], row["position"], row["nationality"], int(row["value"])))
        except FileNotFoundError:
            pass
        return players
# ==========================
# OOP SECTION
# ==========================
class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Player(Person):
    def __init__(self, name, position, nationality, value):
        super().__init__(name, nationality)
        self.position = position
        self.value = value
    
    def is_world_class(self):
        return self.value >= 60
    
    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "nationality": self.nationality,
            "value": self.value
        }
    
    def __str__(self):
        return f"{self.name} - {self.position} - {self.nationality} (£{self.value}m)"

# ==========================
# CUSTOM UTILS (LIBRARY)
# ==========================
class Utils:
    @staticmethod
    def validate_name(name):
        return bool(re.match(r"^[A-Za-z ]+$", name))

    @staticmethod
    def validate_position(position):
        return bool(re.match(r"^(GK|CB|LB|RB|LM|RM|CM|CAM|CDM|LW|RW|ST)$", position))

    @staticmethod
    def validate_value(value):
        return value.isdigit() and int(value) > 0
    
# ==========================
# MAIN SYSTEM CLASS
# ==========================
class FootballSystem:
    def __init__(self):
        self.players = FileManager.load()
        self.lineup = []

        # preload if empty
        if not self.players:
            self.players = [
                Player("Messi", "RW", "Argentina", 80),
                Player("Ronaldo", "ST", "Portugal", 75),
                Player("Mbappe", "ST", "France", 90),
                Player("Neymar", "LW", "Brazil", 70),
                Player("De Bruyne", "CM", "Belgium", 65),
                Player("Van Dijk", "CB", "Netherlands", 60),
                Player("Alisson", "GK", "Brazil", 55),
                Player("Salah", "RW", "Egypt", 65),
                Player("Kane", "ST", "England", 70),
                Player("Modric", "CM", "Croatia", 50),
                Player("Lewandowski", "ST", "Poland", 75)
                Player("Hazard", "LW", "Belgium", 60)
                Player("Griezmann", "CF", "France", 65)
                Player("Kante", "CDM", "France", 55)
                Player("Aubameyang", "ST", "Gabon", 50)
                Player("Sane", "LW", "Germany", 45)
                Player("Sterling", "RW", "England", 60)
                Player("Mane", "LW", "Senegal", 65)
                Player("Ramos", "CB", "Spain", 50)
                Player("Kroos", "CM", "Germany", 55)
                Player("Dybala", "CF", "Argentina", 50)
                Player("Foden", "CM", "England", 45)
                Player("Sancho", "RW", "England", 50)
                Player("Verratti", "CM", "Italy", 55)
                Player("Insigne", "LW", "Italy", 50)
                Player("Grealish", "LM", "England", 45)
                Player("Zlatan", "ST", "Sweden", 40)
                Player("Pogba", "CM", "France", 55)
                Player("Rashford", "ST", "England", 50)
                Player("Muller", "CF", "Germany", 60)
                Player("Kimmich", "CDM", "Germany", 55)
                Player("Benzema", "ST", "France", 65)
                Player("Erling", "ST", "Norway", 70)
                Player("De Gea", "GK", "Spain", 50)
                Player("Carvajal", "RB", "Spain", 45)
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

    def remove(self):
        name = input("Name: ")
        self.players = [p for p in self.players if p.name != name]

    def search(self):
        name = input("Search: ")
        for p in self.players:
            if p.name.lower() == name.lower():
                print(p)

    def filter_nation(self):
        nat = input("Nationality: ")
        for p in self.players:
            if p.nationality.lower() == nat.lower():
                print(p)

    def total_value(self):
        print(sum(p.value for p in self.players))

    def count_world_class(self):
        print(sum(1 for p in self.players if p.is_world_class()))

    def one_on_one(self):
        player1 = input("Player 1: ")
        player2 = input("Player 2: ")

        player1 = next((p for p in self.players if p.name == player1), None)
        player2 = next((p for p in self.players if p.name == player2), None)

        if player1 and player2:
            winner = player1 if player1.value > player2.value else player2
            print(f"{winner.name} wins!")

    def create_lineup(self):
        self.lineup = []
        for _ in range(11):
            name = input("Player: ")
            if any(p.name == name for p in self.players):
                self.lineup.append(name)

    def view_lineup(self):
        for name in self.lineup:
            p = next(p for p in self.players if p.name == name)
            print(p)

    def save(self):
        FileManager.save(self.players)

# ==========================
# TESTING
# ==========================
def run_tests():
    assert Utils.validate_name("Messi")
    assert not Utils.validate_name("Messi123")

    assert Utils.validate_position("ST")
    assert not Utils.validate_position("XYZ")

    testplayer = Player("Test", "ST", "Test", 70)
    assert testplayer.is_world_class()

    system = FootballSystem()
    system.players.append(testplayer)
    system.save()

    print("Tests passed")
# ==========================
# CLI
# ==========================
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