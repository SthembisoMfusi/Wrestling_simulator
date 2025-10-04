#!/usr/bin/env python3
"""
Roster Creator for Wrestling Simulator

This script creates roster files using wrestler names from text files.
You can either use the built-in wrestler names or provide your own text file.

Usage:
    python3 create_all_rosters.py                    # Create all themed rosters
    python3 create_all_rosters.py --file my_names.txt # Create roster from custom file
    python3 create_all_rosters.py --help             # Show help
"""

import os
import random
import pickle
import argparse
import sys

def load_wrestler_names_from_file(file_path):
    """Load wrestler names from a text file."""
    names = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                name = line.strip()
                if name and not name.startswith('#'):  # Skip empty lines and comments
                    names.append(name)
        print(f"✓ Loaded {len(names)} names from {file_path}")
        return names
    except FileNotFoundError:
        print(f"❌ Error: Could not find file {file_path}")
        return []
    except Exception as e:
        print(f"❌ Error reading file {file_path}: {e}")
        return []

def create_roster_files():
    """Create roster files using wrestler names from the data folder."""
    
    # Ensure rosters directory exists
    os.makedirs("rosters", exist_ok=True)
    
    # Wrestler names from the data files
    male_names = [
        "'Ravishing' Rick Rude", '"Ace" Cowboy Bob Orton', '"Bad Ass" Billy Gunn', '"Hacksaw" Jim Duggan',
        '"Leaping" Lanny Poffo', '"Macho Man" Randy Savage', '"Million Dollar Man" Ted DiBiase', '"Mr. Perfect" Curt Hennig',
        '"Nature Boy" Buddy Rogers', '"Nature Boy" Ric Flair', '"Rowdy" Roddy Piper', '"Superstar" Billy Graham',
        '"The American Dream" Dusty Rhodes', '1-2-3 Kid (X-Pac)', '2 Cold Scorpio', 'A-Train (Albert)',
        'Abdullah the Butcher', 'Adam Bomb', 'Adam Rose', 'Adrian Adonis', 'AJ Styles', 'Alberto Del Rio',
        'Alex Riley', 'Andre the Giant', 'Antonio Cesaro', 'Bam Bam Bigelow', 'Batista', 'Big Boss Man',
        'Big Show', 'Bobby Lashley', 'Booker T', 'Bray Wyatt', 'Brock Lesnar', 'Bruno Sammartino',
        'Chris Jericho', 'Christian', 'CM Punk', 'Cody Rhodes', 'Daniel Bryan', 'Dean Ambrose',
        'Dolph Ziggler', 'Edge', 'Finn Balor', 'Goldberg', 'Jeff Hardy', 'John Cena', 'Kane',
        'Kevin Owens', 'Kurt Angle', 'Mark Henry', 'Mick Foley', 'Randy Orton', 'Roman Reigns',
        'Seth Rollins', 'Sheamus', 'Stone Cold Steve Austin', 'The Rock', 'The Undertaker', 'Triple H'
    ]
    
    female_names = [
        'Aja Kong', 'AJ Lee', 'Akira Hokuto', 'Alba', 'Alexa Bliss', 'Alicia Fox', 'Alundra Blayze', 'Ashley',
        'Ashley Massaro', 'Asuka', 'Aurora', 'Ava', 'Axiom', 'Bayley', 'Becky Lynch', 'Beth Phoenix',
        'B.B.', 'Bianca Belair', 'Billie Kay', 'Blair Davenport', 'Candice LeRae', 'Carmella', 'Charlotte Flair',
        'Chyna', 'Dana Brooke', 'Ember Moon', 'Eve Torres', 'Ivory', 'Jacqueline', 'Kelly Kelly', 'Lita',
        'Mickie James', 'Molly Holly', 'Naomi', 'Natalya', 'Nia Jax', 'Paige', 'Rhea Ripley', 'Ronda Rousey',
        'Sasha Banks', 'Shayna Baszler', 'Stephanie McMahon', 'Tamina', 'Trish Stratus', 'Victoria'
    ]
    
    other_names = [
        'Nyla Rose', 'Ashton Greymoore', 'Candy Lee', 'Gisele Shaw', 'Mike Parrow', 'Kidd Bandit',
        'Jamie Senegal', 'AC Mack', 'Ace Austin', 'Diamante', 'Dark Sheik', 'Edith Surreal',
        'Billy Dixon', 'Max The Impaler', 'Gabby Ortiz', 'Parrow', 'Effy', 'Sonny Kiss',
        'Veda Scott', 'Leyla Hirsch', 'Allie', 'Abadon', 'Anna Jay', 'Brandi Rhodes'
    ]
    
    def create_wrestler_data(name, gender, wrestler_type="balanced"):
        """Create wrestler data with different stat distributions."""
        base_stats = {
            "balanced": {"strength": (60, 90), "power": (60, 90), "speed": (50, 80), "technique": (60, 90)},
            "powerhouse": {"strength": (80, 100), "power": (80, 100), "speed": (30, 60), "technique": (50, 80)},
            "speedster": {"strength": (50, 80), "power": (50, 80), "speed": (80, 100), "technique": (70, 95)},
            "technician": {"strength": (60, 85), "power": (60, 85), "speed": (60, 85), "technique": (80, 100)},
            "veteran": {"strength": (70, 95), "power": (70, 95), "speed": (40, 70), "technique": (75, 95)},
            "rookie": {"strength": (50, 75), "power": (50, 75), "speed": (50, 80), "technique": (40, 70)}
        }
        
        stats = base_stats.get(wrestler_type, base_stats["balanced"])
        
        return {
            'name': name,
            'gender': gender,
            'strength': random.randint(*stats["strength"]),
            'power': random.randint(*stats["power"]),
            'speed': random.randint(*stats["speed"]),
            'health': random.randint(120, 180),
            'stamina': random.randint(60, 100),
            'grapple': random.randint(5, 20),
            'technique': random.randint(*stats["technique"])
        }
    
    # Create various themed rosters
    rosters_to_create = [
        # (filename, description, names, gender, count, wrestler_type)
        ("legendary_males.pickle", "Legendary Male Wrestlers", male_names[:8], "male", 8, "veteran"),
        ("legendary_females.pickle", "Legendary Female Wrestlers", female_names[:8], "female", 8, "veteran"),
        ("modern_males.pickle", "Modern Male Wrestlers", male_names[4:10], "male", 6, "balanced"),
        ("modern_females.pickle", "Modern Female Wrestlers", female_names[4:10], "female", 6, "balanced"),
        ("powerhouse_division.pickle", "Powerhouse Division", male_names[:4], "male", 4, "powerhouse"),
        ("speed_demons.pickle", "Speed Demons", female_names[:4], "female", 4, "speedster"),
        ("technical_masters.pickle", "Technical Masters", (male_names + female_names)[:6], "mixed", 6, "technician"),
        ("rookie_class.pickle", "Rookie Class", (male_names + female_names)[6:14], "mixed", 8, "rookie"),
        ("mixed_legends.pickle", "Mixed Legends", (male_names + female_names)[:12], "mixed", 12, "veteran"),
        ("indie_stars.pickle", "Independent Stars", other_names, "mixed", 6, "balanced"),
        ("championship_roster_large.pickle", "Championship Roster", (male_names + female_names)[:16], "mixed", 16, "balanced"),
        ("womens_division.pickle", "Women's Division", female_names, "female", 10, "balanced"),
        ("hall_of_fame.pickle", "Hall of Fame", (male_names + female_names)[:20], "mixed", 20, "veteran"),
        ("tag_teams.pickle", "Tag Team Specialists", male_names[:4], "male", 4, "balanced"),
        ("rising_stars.pickle", "Rising Stars", (male_names + female_names)[10:18], "mixed", 8, "rookie"),
    ]
    
    created_rosters = []
    
    for filename, description, names, gender, count, wrestler_type in rosters_to_create:
        # Select the specified number of names
        selected_names = names[:count] if len(names) >= count else names
        
        # Create wrestler data
        roster_data = [create_wrestler_data(name, gender, wrestler_type) for name in selected_names]
        
        # Save to rosters directory
        filepath = os.path.join("rosters", filename)
        with open(filepath, 'wb') as f:
            pickle.dump(roster_data, f)
        
        print(f"✓ Created {filename} - {description} ({len(roster_data)} wrestlers)")
        created_rosters.append((filename, len(roster_data)))
    
    return created_rosters

def create_custom_roster(names_file, output_name, wrestler_type="balanced", count=8, gender="mixed"):
    """Create a single roster from a custom names file."""
    print(f"🎯 Creating custom roster from {names_file}...")
    
    # Load names from file
    names = load_wrestler_names_from_file(names_file)
    if not names:
        return False
    
    # Ensure rosters directory exists
    os.makedirs("rosters", exist_ok=True)
    
    # Select names
    selected_names = names[:count] if len(names) >= count else names
    if len(selected_names) < count:
        print(f"⚠️  Warning: Only {len(selected_names)} names available, requested {count}")
    
    # Create wrestler data
    roster_data = [create_wrestler_data(name, gender, wrestler_type) for name in selected_names]
    
    # Save roster
    filename = f"{output_name}.pickle"
    filepath = os.path.join("rosters", filename)
    with open(filepath, 'wb') as f:
        pickle.dump(roster_data, f)
    
    print(f"✓ Created {filename} with {len(roster_data)} wrestlers")
    print(f"  Type: {wrestler_type}, Gender: {gender}")
    return True

def main():
    """Main function to create roster files."""
    parser = argparse.ArgumentParser(
        description="Create roster files for the wrestling simulator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 create_all_rosters.py                           # Create all themed rosters
  python3 create_all_rosters.py --file my_names.txt       # Create roster from custom file
  python3 create_all_rosters.py --file names.txt --count 12 --type powerhouse
  python3 create_all_rosters.py --file names.txt --output my_roster --gender male
        """
    )
    
    parser.add_argument('--file', '-f', 
                       help='Text file containing wrestler names (one per line)')
    parser.add_argument('--output', '-o', 
                       default='custom_roster',
                       help='Output roster name (default: custom_roster)')
    parser.add_argument('--count', '-c', 
                       type=int, default=8,
                       help='Number of wrestlers in roster (default: 8)')
    parser.add_argument('--type', '-t',
                       choices=['balanced', 'powerhouse', 'speedster', 'technician', 'veteran', 'rookie'],
                       default='balanced',
                       help='Wrestler type (default: balanced)')
    parser.add_argument('--gender', '-g',
                       choices=['male', 'female', 'mixed'],
                       default='mixed',
                       help='Wrestler gender (default: mixed)')
    
    args = parser.parse_args()
    
    if args.file:
        # Create custom roster from file
        print("🎯 Creating custom roster from file...")
        print("="*60)
        
        success = create_custom_roster(
            args.file, 
            args.output, 
            args.type, 
            args.count, 
            args.gender
        )
        
        if success:
            print("\n✅ Custom roster created successfully!")
            print(f"📂 Saved to: rosters/{args.output}.pickle")
        else:
            print("\n❌ Failed to create custom roster")
            sys.exit(1)
    else:
        # Create all themed rosters
        print("🎯 Creating all themed roster files...")
        print("="*60)
        
        created_rosters = create_roster_files()
        
        print("\n" + "="*60)
        print("📁 ROSTER CREATION SUMMARY")
        print("="*60)
        
        for filename, count in created_rosters:
            print(f"📋 {filename:<35} | {count:>2} wrestlers")
        
        print(f"\n✅ Successfully created {len(created_rosters)} roster files")
        print(f"📂 All rosters saved to: rosters/")
    
    # List all roster files
    if os.path.exists("rosters"):
        all_files = [f for f in os.listdir("rosters") if f.endswith('.pickle')]
        print(f"\n📊 Total roster files available: {len(all_files)}")
        
        print("\n🎯 All available rosters:")
        for i, roster_file in enumerate(sorted(all_files), 1):
            # Get wrestler count
            filepath = os.path.join("rosters", roster_file)
            try:
                with open(filepath, 'rb') as f:
                    roster_data = pickle.load(f)
                    wrestler_count = len(roster_data) if isinstance(roster_data, list) else 0
            except:
                wrestler_count = 0
            
            print(f"  {i:>2}. {roster_file:<35} ({wrestler_count:>2} wrestlers)")
    
    print("\n🎉 Roster creation complete!")
    print("💡 You can now use these rosters in the wrestling simulator!")

if __name__ == "__main__":
    main()
