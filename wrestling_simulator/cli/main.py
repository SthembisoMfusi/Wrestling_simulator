"""
Main CLI interface for the Wrestling Simulator.
"""

import os
from typing import Optional

from ..core.roster import Roster
from ..core.tournament import Tournament


def get_valid_wrestler_count() -> int:
    """Gets a valid number of wrestlers from the user (between 11 and 75)."""
    while True:
        try:
            num = int(
                input(
                    "Please enter the number of wrestlers in the roster? [min = 11, max = 75]: "
                )
            )
            if 11 <= num <= 75:
                return num
            else:
                print("Number out of range. Please enter a value between 11 and 75.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_tournament_size(max_participants: int) -> int:
    """Gets a valid tournament size from the user (divisible by 4, positive, and not exceeding max_participants)."""
    while True:
        try:
            roster_num = int(
                input(
                    f"How many tournament participants do you want there to be? (max: {max_participants}, divisible by 4): "
                )
            )
            if (
                roster_num % 4 == 0
                and roster_num > 0
                and roster_num <= max_participants
            ):
                return roster_num
            else:
                print(
                    f"Invalid choice. The number should be positive, divisible by 4, and not exceed {max_participants}."
                )
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main() -> None:
    """Main function to run the wrestling simulator."""
    print("Welcome to the Wrestling Simulator!")
    print("=" * 40)

    # Get user choice for roster creation/loading
    ans = input(
        "Do you want to load a saved roster or create a new roster? [Create, Load]: "
    )
    options = ["create", "load"]
    while ans.lower() not in options:
        ans = input(f"Invalid option, these are your options: {options}: ")

    if ans.lower() == "load":
        available_rosters = Roster.list_available_rosters()

        if not available_rosters:
            print("No roster files found in the 'rosters' folder.")
            print(
                "Please create a roster first or place roster files in the 'rosters' folder."
            )
            return

        print("Available rosters:")
        for i, (roster_file, wrestler_count) in enumerate(available_rosters, 1):
            print(f"{i}. {roster_file} ({wrestler_count} wrestlers)")

        while True:
            try:
                choice = int(
                    input(f"Please select a roster (1-{len(available_rosters)}): ")
                )
                if 1 <= choice <= len(available_rosters):
                    selected_roster, wrestler_count = available_rosters[choice - 1]
                    file_path = os.path.join("rosters", selected_roster)
                    wwe = Roster(contestants=None, file=file_path)
                    num = len(wwe.roster)
                    print(f"Loaded {selected_roster} with {num} wrestlers")
                    break
                else:
                    print(
                        f"Please enter a number between 1 and {len(available_rosters)}"
                    )
            except ValueError:
                print("Please enter a valid number.")

    elif ans.lower() == "create":
        num = get_valid_wrestler_count()
        wwe = Roster(contestants=num)
        save = input("Would you like to save this roster? [Yes/No] ")
        opt = ["yes", "no", "y", "n"]
        while save.lower() not in opt:
            save = input(
                "Invalid response, would you like to save this roster? [Yes/No] "
            )
        if save.lower() == "yes" or save.lower() == "y":
            fileName = input(
                "Please enter the name of the file you want to save it to: "
            )

            if not fileName.endswith(".pickle"):
                fileName += ".pickle"

            wwe.save_roster(fileName)
            print(f"Roster saved to rosters/{fileName}")

    # Get valid tournament size
    roster_num = get_valid_tournament_size(num)

    # Create and run the tournament
    battle = Tournament(wwe, roster_num)
    battle.tournamentPlay()


if __name__ == "__main__":
    main()
