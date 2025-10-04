# 🎯 Roster Creation Guide

This guide explains how to create roster files using the wrestler names from the data folder or your own custom text files.

## 📁 Available Scripts

### 1. `create_all_rosters.py` - Main Roster Creation Script
This is the main script that creates roster files using wrestler names from the data folder or your own custom text files.

**Features:**
- Creates 15 different themed rosters using built-in names
- Can create custom rosters from your own text files
- Different wrestler types (balanced, powerhouse, speedster, technician, veteran, rookie)
- Various roster sizes (4-20 wrestlers)
- Command-line interface with options

**Usage:**
```bash
# Create all themed rosters
python3 create_all_rosters.py

# Create custom roster from your text file
python3 create_all_rosters.py --file my_names.txt

# Create custom roster with specific options
python3 create_all_rosters.py --file names.txt --count 12 --type powerhouse --output my_roster
```

### 2. `demo_roster_selection_final.py` - Demo Script
This script demonstrates the new roster selection feature with wrestler counts.

**Features:**
- Creates sample rosters of different sizes
- Shows how the new roster selection interface works
- Demonstrates the wrestler count display

**Usage:**
```bash
python3 demo_roster_selection_final.py
```

## 🎯 Roster Types Created

The main script creates these themed rosters:

1. **legendary_males.pickle** - 8 legendary male wrestlers (veteran stats)
2. **legendary_females.pickle** - 8 legendary female wrestlers (veteran stats)
3. **modern_males.pickle** - 6 modern male wrestlers (balanced stats)
4. **modern_females.pickle** - 6 modern female wrestlers (balanced stats)
5. **powerhouse_division.pickle** - 4 powerhouse male wrestlers (high strength/power)
6. **speed_demons.pickle** - 4 speedster female wrestlers (high speed)
7. **technical_masters.pickle** - 6 mixed technical wrestlers (high technique)
8. **rookie_class.pickle** - 8 mixed rookie wrestlers (lower stats)
9. **mixed_legends.pickle** - 12 mixed legendary wrestlers (veteran stats)
10. **indie_stars.pickle** - 6 independent wrestlers (balanced stats)
11. **championship_roster_large.pickle** - 16 mixed championship wrestlers
12. **womens_division.pickle** - 10 female wrestlers
13. **hall_of_fame.pickle** - 20 mixed hall of fame wrestlers
14. **tag_teams.pickle** - 4 male tag team specialists
15. **rising_stars.pickle** - 8 mixed rising stars (rookie stats)

## 🎮 How to Use the New Roster Selection Feature

After creating roster files, you can use the improved roster selection in the wrestling simulator:

1. **Run the simulator:**
   ```bash
   python -m wrestling_simulator.main
   ```

2. **Choose "Load" when prompted**

3. **See the new interface:**
   ```
   Available rosters:
   1. championship_roster_large.pickle (16 wrestlers)
   2. hall_of_fame.pickle (20 wrestlers)
   3. legendary_females.pickle (8 wrestlers)
   4. legendary_males.pickle (8 wrestlers)
   5. mixed_legends.pickle (12 wrestlers)
   Please select a roster (1-5): 3
   Loaded legendary_females.pickle with 8 wrestlers
   ```

## 🛠️ Creating Custom Rosters from Text Files

You can create rosters from your own text files containing wrestler names:

### Text File Format
Create a text file with one wrestler name per line:
```
Hulk Hogan
Stone Cold Steve Austin
The Rock
John Cena
Undertaker
# This is a comment line (ignored)
Shawn Michaels
Triple H
```

### Command Line Options
```bash
# Basic usage - create roster from text file
python3 create_all_rosters.py --file my_names.txt

# Specify output name
python3 create_all_rosters.py --file my_names.txt --output my_roster

# Set number of wrestlers
python3 create_all_rosters.py --file my_names.txt --count 12

# Choose wrestler type
python3 create_all_rosters.py --file my_names.txt --type powerhouse

# Set gender
python3 create_all_rosters.py --file my_names.txt --gender male

# Combine options
python3 create_all_rosters.py --file my_names.txt --output championship --count 16 --type veteran --gender mixed
```

### Available Options
- `--file, -f`: Text file containing wrestler names (required for custom rosters)
- `--output, -o`: Output roster name (default: custom_roster)
- `--count, -c`: Number of wrestlers in roster (default: 8)
- `--type, -t`: Wrestler type - balanced, powerhouse, speedster, technician, veteran, rookie (default: balanced)
- `--gender, -g`: Wrestler gender - male, female, mixed (default: mixed)

### Examples
```bash
# Create a powerhouse roster with 12 male wrestlers
python3 create_all_rosters.py --file strong_guys.txt --count 12 --type powerhouse --gender male --output powerhouse_roster

# Create a balanced mixed roster with 8 wrestlers
python3 create_all_rosters.py --file all_wrestlers.txt --type balanced --gender mixed --output balanced_roster

# Create a veteran roster with 20 wrestlers
python3 create_all_rosters.py --file legends.txt --count 20 --type veteran --output hall_of_fame
```

## 📊 Roster File Structure

Each roster file contains a list of wrestler dictionaries:

```python
[
    {
        'name': 'Hulk Hogan',
        'gender': 'male',
        'strength': 95,
        'power': 90,
        'speed': 60,
        'health': 180,
        'stamina': 85,
        'grapple': 15,
        'technique': 80
    },
    # ... more wrestlers
]
```

## 🎯 Benefits of the New System

1. **User-Friendly**: No more typing file paths
2. **Informative**: Shows wrestler counts before selection
3. **Organized**: All rosters in dedicated folder
4. **Flexible**: Easy to add new rosters
5. **Error-Resistant**: Handles corrupted files gracefully

## 🚀 Next Steps

1. Run `create_all_rosters.py` to create roster files
2. Test the new roster selection feature
3. Create custom rosters for your needs
4. Share your custom rosters with the community!

## 💡 Tips

- Use descriptive filenames for your rosters
- Create rosters of different sizes for different tournament types
- Mix wrestler types for balanced competition
- Save your favorite rosters for quick access

Happy wrestling! 🎉
