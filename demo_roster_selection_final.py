#!/usr/bin/env python3
"""
Final demo script showing the improved roster selection with wrestler counts.
"""

import os
import sys
import random
import pickle

# Add current directory to path
sys.path.insert(0, ".")


def create_demo_rosters():
    """Create demo rosters with different sizes."""
    print("Creating demo rosters...")

    # Create rosters directory if it doesn't exist
    if not os.path.exists("rosters"):
        os.makedirs("rosters")

    # Sample wrestler names
    male_names = [
        "Hulk Hogan",
        "Stone Cold Steve Austin",
        "The Rock",
        "John Cena",
        "Undertaker",
        "Shawn Michaels",
        "Triple H",
        "Bret Hart",
        "Randy Savage",
        "Ric Flair",
        "Roddy Piper",
        "Dusty Rhodes",
    ]

    female_names = [
        "Becky Lynch",
        "Charlotte Flair",
        "Sasha Banks",
        "Bayley",
        "Asuka",
        "Alexa Bliss",
        "Ronda Rousey",
        "Trish Stratus",
        "Lita",
        "Chyna",
        "Beth Phoenix",
        "Mickie James",
    ]

    def create_wrestler_data(name, gender):
        """Create wrestler data."""
        return {
            "name": name,
            "gender": gender,
            "strength": random.randint(60, 95),
            "power": random.randint(60, 95),
            "speed": random.randint(50, 90),
            "health": random.randint(120, 180),
            "stamina": random.randint(60, 100),
            "grapple": random.randint(5, 20),
            "technique": random.randint(60, 95),
        }

    # Create different sized rosters
    rosters_to_create = [
        ("small_roster.pickle", "Small Roster", male_names[:2], "male"),
        ("medium_roster.pickle", "Medium Roster", male_names[:4], "male"),
        ("large_roster.pickle", "Large Roster", male_names[:8], "male"),
        (
            "mixed_roster.pickle",
            "Mixed Roster",
            (male_names + female_names)[:6],
            "mixed",
        ),
        ("womens_roster.pickle", "Women's Roster", female_names[:5], "female"),
    ]

    for filename, description, names, gender in rosters_to_create:
        roster_data = [create_wrestler_data(name, gender) for name in names]

        filepath = os.path.join("rosters", filename)
        with open(filepath, "wb") as f:
            pickle.dump(roster_data, f)

        print(f"  ✓ Created {filename} with {len(roster_data)} wrestlers")

    print("Demo rosters created!")


def demonstrate_roster_selection():
    """Demonstrate the new roster selection feature."""
    print("\n" + "=" * 60)
    print("DEMO: Improved Roster Selection with Wrestler Counts")
    print("=" * 60)

    # Create demo rosters
    create_demo_rosters()

    # Show the new roster selection interface
    print("\n🎯 NEW FEATURE: Roster Selection with Wrestler Counts")
    print("-" * 50)

    # Simulate the roster listing functionality
    rosters_dir = "rosters"
    if not os.path.exists(rosters_dir):
        print("No roster files found in the 'rosters' folder.")
        return

    roster_files = [f for f in os.listdir(rosters_dir) if f.endswith(".pickle")]
    roster_info = []

    for roster_file in sorted(roster_files):
        try:
            file_path = os.path.join(rosters_dir, roster_file)
            with open(file_path, "rb") as f:
                roster_data = pickle.load(f)
                wrestler_count = (
                    len(roster_data) if isinstance(roster_data, list) else 0
                )
                roster_info.append((roster_file, wrestler_count))
        except (pickle.PickleError, FileNotFoundError, EOFError):
            roster_info.append((roster_file, 0))

    if not roster_info:
        print("No roster files found in the 'rosters' folder.")
        return

    print("Available rosters:")
    for i, (roster_file, wrestler_count) in enumerate(roster_info, 1):
        print(f"{i}. {roster_file} ({wrestler_count} wrestlers)")

    print(f"\nTotal rosters available: {len(roster_info)}")

    # Show what the user would see
    print("\n" + "=" * 60)
    print("WHAT THE USER SEES:")
    print("=" * 60)
    print(
        "Do you want to load a saved roster or create a new roster? [Create, Load]: Load"
    )
    print("Available rosters:")
    for i, (roster_file, wrestler_count) in enumerate(roster_info, 1):
        print(f"{i}. {roster_file} ({wrestler_count} wrestlers)")
    print(f"Please select a roster (1-{len(roster_info)}): 2")

    # Simulate loading the second roster
    if len(roster_info) >= 2:
        selected_roster, expected_count = roster_info[1]
        file_path = os.path.join("rosters", selected_roster)

        try:
            with open(file_path, "rb") as f:
                loaded_roster = pickle.load(f)
            actual_count = len(loaded_roster)

            print(f"Loaded {selected_roster} with {actual_count} wrestlers")

            print(f"\n✅ SUCCESS: Roster loaded with {actual_count} wrestlers!")
            print(f"   Expected: {expected_count}, Actual: {actual_count}")
            print(f"   Match: {expected_count == actual_count}")

            # Show some wrestler names
            print(f"\n📋 Wrestlers in {selected_roster}:")
            for i, wrestler in enumerate(loaded_roster[:3], 1):
                print(f"   {i}. {wrestler['name']} ({wrestler['gender']})")
            if len(loaded_roster) > 3:
                print(f"   ... and {len(loaded_roster) - 3} more wrestlers")

        except Exception as e:
            print(f"❌ Error loading roster: {e}")

    print("\n🎉 Demo completed successfully!")
    print("💡 This shows how the new roster selection feature works!")


if __name__ == "__main__":
    demonstrate_roster_selection()
