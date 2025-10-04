#!/usr/bin/env python3
"""
Quick Tournament Example

This example demonstrates how to create a simple tournament with auto-generated wrestlers.
"""

from wrestling_simulator import Wrestler, Roster, Tournament


def main():
    """Run a quick tournament example."""
    print("🥊 Quick Tournament Example")
    print("=" * 40)
    
    # Create a roster with 8 wrestlers
    roster = Roster(8, auto_fill=False)
    
    # Auto-generate wrestlers (this would normally require user input)
    # For this example, we'll manually create some wrestlers
    wrestlers = [
        Wrestler("Thunder", "male", 85, 75, 70, 160, 90, 12, 80),
        Wrestler("Lightning", "female", 80, 90, 85, 150, 85, 15, 85),
        Wrestler("Storm", "male", 90, 70, 65, 170, 95, 10, 75),
        Wrestler("Blaze", "female", 75, 95, 90, 140, 80, 18, 90),
        Wrestler("Titan", "male", 95, 60, 60, 180, 100, 8, 70),
        Wrestler("Phoenix", "female", 70, 100, 95, 130, 75, 20, 95),
        Wrestler("Crusher", "male", 100, 55, 55, 190, 100, 6, 65),
        Wrestler("Shadow", "other", 65, 100, 100, 120, 70, 20, 100),
    ]
    
    roster.roster = wrestlers
    
    print(f"Created roster with {len(roster.roster)} wrestlers:")
    for i, wrestler in enumerate(roster.roster, 1):
        print(f"{i}. {wrestler.name} - Overall Rating: {wrestler.get_overall_rating():.1f}")
    
    print("\n🏆 Starting Tournament!")
    print("=" * 40)
    
    # Create and run tournament
    tournament = Tournament(roster, 8)
    tournament.tournamentPlay()
    
    print("\n✅ Tournament Complete!")


if __name__ == "__main__":
    main()
