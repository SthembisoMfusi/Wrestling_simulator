#!/usr/bin/env python3
"""
Main CLI interface for the Wrestling Simulator.
"""

import os
from typing import Optional

from ..core.roster import Roster
from ..core.tournament import Tournament
from ..utils.file_utils import load_wrestler_names_from_file


def get_valid_wrestler_count(max_count: int = 75) -> int:
    """Gets a valid number of wrestlers from the user (between 1 and max_count)."""
    while True:
        try:
            num = int(input(f"Enter number of wrestlers (1-{max_count}): "))
            if 1 <= num <= max_count:
                return num
            print(f"Number out of range. Must be between 1 and {max_count}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_tournament_size(max_participants: int) -> int:
    """Gets a valid tournament size (divisible by 4, positive, not exceeding max_participants)."""
    while True:
        try:
            roster_num = int(
                input(
                    f"How many tournament participants? (max: {max_participants}, divisible by 4): "
                )
            )
            if (
                roster_num % 4 == 0
                and roster_num > 0
                and roster_num <= max_participants
            ):
                return roster_num
            print("Invalid choice. Must be positive, divisible by 4, and not exceed max.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def create_roster_from_file() -> Optional[Roster]:
    """Handles creating a roster from a text file."""
    print("\n📁 Creating roster from text file...")

    path = input("Enter the path to your wrestler names file: ").strip()
    try:
        names = load_wrestler_names_from_file(path)
        print(f"✓ Loaded {len(names)} wrestler names\n")
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ Error: {e}")
        return None

    print("Choose wrestler type:")
    types = ["Balanced", "Powerhouse", "Speedster", "Technician", "Veteran", "Rookie"]
    for i, t in enumerate(types, 1):
        print(f"  {i}. {t}")
    while True:
        try:
            t_choice = int(input("Select type (1-6): "))
            if 1 <= t_choice <= len(types):
                wrestler_type = types[t_choice - 1]
                break
            print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    print("\nChoose gender:")
    genders = ["Male", "Female", "Mixed"]
    for i, g in enumerate(genders, 1):
        print(f"  {i}. {g}")
    while True:
        try:
            g_choice = int(input("Select gender (1-3): "))
            if 1 <= g_choice <= len(genders):
                gender = genders[g_choice - 1]
                break
            print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    num = get_valid_wrestler_count(len(names))
    roster_name = input("Enter a name for your roster: ").strip()

    wwe = Roster.from_names(names[:num], wrestler_type, gender)
    wwe.save_roster(f"{roster_name}.pickle")

    print(f"✅ Roster '{roster_name}' created successfully!")
    return wwe


def view_wrestler_stats(roster: Roster) -> None:
    """Displays stats for a specific wrestler from the current roster."""
    print("\n📊 View Wrestler Stats")
    for i, wrestler in enumerate(roster.roster, 1):
        print(f"{i}. {wrestler.name}")
    try:
        choice = int(input("Select a wrestler number to view: "))
        if 1 <= choice <= len(roster.roster):
            wrestler = roster.roster[choice - 1]
            wrestler.display_stats_table()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


def main() -> None:
    """Main function to run the wrestling simulator."""
    print("Welcome to the Wrestling Simulator!")
    print("=" * 40)

    ans = input("Do you want to load a saved roster or create a new roster? [Create, Load]: ")
    while ans.lower() not in ["create", "load"]:
        ans = input("Invalid option. Please choose [Create, Load]: ")

    if ans.lower() == "load":
        available_rosters = Roster.list_available_rosters()

        if not available_rosters:
            print("No roster files found. Please create a roster first.")
            return

        print("Available rosters:")
        for i, (roster_file, wrestler_count) in enumerate(available_rosters, 1):
            print(f"{i}. {roster_file} ({wrestler_count} wrestlers)")

        while True:
            try:
                choice = int(input(f"Select a roster (1-{len(available_rosters)}): "))
                if 1 <= choice <= len(available_rosters):
                    selected_roster, _ = available_rosters[choice - 1]
                    file_path = os.path.join("rosters", selected_roster)
                    wwe = Roster(contestants=None, file=file_path)
                    print(f"Loaded {selected_roster} with {len(wwe.roster)} wrestlers")
                    break
                print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

    else:  # Create new roster
        print("\nHow would you like to create the roster?\n")
        print("  1. Random wrestlers (current method)")
        print("  2. From text file (new method)")

        while True:
            try:
                method = int(input("Please select an option (1-2): "))
                if method in (1, 2):
                    break
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Please enter a valid number.")

        if method == 1:
            num = get_valid_wrestler_count()
            wwe = Roster(contestants=num)
            save = input("Would you like to save this roster? [Yes/No]: ").lower()
            if save in ("yes", "y"):
                fileName = input("Enter filename to save: ").strip()
                if not fileName.endswith(".pickle"):
                    fileName += ".pickle"
                wwe.save_roster(fileName)
                print(f"Roster saved to rosters/{fileName}")
        else:
            wwe = create_roster_from_file()
            if not wwe:
                return

    while True:
        print("\nMain Menu:")
        print("1. Run Tournament")
        print("2. View Wrestler Stats")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            roster_num = get_valid_tournament_size(len(wwe.roster))
            battle = Tournament(wwe, roster_num)
            battle.tournamentPlay()
        elif choice == "2":
            view_wrestler_stats(wwe)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1-3.")


if __name__ == "__main__":
    main()
