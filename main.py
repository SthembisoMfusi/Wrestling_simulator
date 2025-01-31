from Tournament import Tournament
from createRoster import Roster
import os

def get_valid_wrestler_count():
    """Gets a valid number of wrestlers from the user (between 11 and 75)."""
    while True:
        try:
            num = int(input("Please enter the number of wrestlers in the roster? [min = 11, max = 75]: "))
            if 11 <= num <= 75:
                return num
            else:
                print("Number out of range. Please enter a value between 11 and 75.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_tournament_size(max_participants):
    """Gets a valid tournament size from the user (divisible by 4, positive, and not exceeding max_participants)."""
    while True:
        try:
            roster_num = int(input(f"How many tournament participants do you want there to be? (max: {max_participants}, divisible by 4): "))
            if roster_num % 4 == 0 and roster_num > 0 and roster_num <= max_participants:
                return roster_num
            else:
                print(f"Invalid choice. The number should be positive, divisible by 4, and not exceed {max_participants}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


ans = input("Do you want to load a saved roster or create a new roster? [Create, Load]: ")
options = ["create", "load"]
while ans.lower() not in options:
    ans = input(f"Invalid option, these are your options: {options}: ")

if ans.lower() == "load":
    file = input("Please enter the file path of the roster you want to load: ")
    while not os.path.exists(file):
        file = input("Please enter a valid file path: ")
    wwe = Roster(contestants=None, file=file)

    
    num = len(wwe.roster)

elif ans.lower() == "create":
    num = get_valid_wrestler_count()
    wwe = Roster(contestants=num)

# Get valid tournament size
roster_num = get_valid_tournament_size(num)

# Create and run the tournament
battle = Tournament(wwe, roster_num)
battle.tournamentPlay()