#!/usr/bin/env python3
"""
Roster Management Example

This example demonstrates how to create, save, and load wrestler rosters.
"""

from wrestling_simulator import Wrestler, Roster
import os


def main():
    """Demonstrate roster management features."""
    print("💾 Roster Management Example")
    print("=" * 40)
    
    # Create a new roster
    roster = Roster(auto_fill=False)
    
    # Add some custom wrestlers
    wrestlers = [
        Wrestler("The Rock", "male", 90, 80, 70, 160, 95, 15, 85),
        Wrestler("Stone Cold", "male", 85, 85, 75, 155, 90, 12, 80),
        Wrestler("Undertaker", "male", 95, 70, 65, 180, 100, 10, 75),
        Wrestler("Chyna", "female", 80, 90, 85, 150, 85, 18, 90),
        Wrestler("Trish Stratus", "female", 75, 95, 90, 140, 80, 20, 95),
    ]
    
    roster.roster = wrestlers
    
    print(f"Created roster with {len(roster.roster)} wrestlers:")
    for wrestler in roster.roster:
        print(f"- {wrestler.name}: {wrestler.showStats()}")
    
    # Save the roster
    filename = "example_roster.pickle"
    roster.save_roster(filename)
    print(f"\n💾 Saved roster to {filename}")
    
    # Create a new roster and load from file
    new_roster = Roster(file=filename)
    print(f"\n📂 Loaded roster with {len(new_roster.roster)} wrestlers:")
    for wrestler in new_roster.roster:
        print(f"- {wrestler.name}: {wrestler.showStats()}")
    
    # Demonstrate roster operations
    print("\n🔧 Roster Operations:")
    
    # Get wrestler by name
    rock = new_roster.get_wrestler("The Rock")
    print(f"Found wrestler: {rock.name}")
    
    # Get wrestler by index
    first_wrestler = new_roster.get_wrestler(0)
    print(f"First wrestler: {first_wrestler.name}")
    
    # Remove a wrestler
    new_roster.remove_wrestler("Undertaker")
    print(f"After removing Undertaker: {len(new_roster.roster)} wrestlers remain")
    
    # Clean up
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\n🧹 Cleaned up {filename}")
    
    print("\n✅ Roster management example complete!")


if __name__ == "__main__":
    main()
