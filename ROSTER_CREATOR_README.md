# 🎯 Roster Creator for Wrestling Simulator

The enhanced roster creator allows you to create roster files using wrestler names from text files or the built-in wrestler database.

## 🚀 Quick Start

### Create All Themed Rosters
```bash
python3 create_all_rosters.py
```
This creates 15 different themed rosters using built-in wrestler names.

### Create Custom Roster from Text File
```bash
python3 create_all_rosters.py --file my_wrestlers.txt
```
This creates a roster using names from your text file.

## 📝 Text File Format

Create a text file with one wrestler name per line:
```
Hulk Hogan
Stone Cold Steve Austin
The Rock
John Cena
# This is a comment (ignored)
Undertaker
Shawn Michaels
```

## 🛠️ Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--file` | `-f` | Text file with wrestler names | None |
| `--output` | `-o` | Output roster name | `custom_roster` |
| `--count` | `-c` | Number of wrestlers | `8` |
| `--type` | `-t` | Wrestler type | `balanced` |
| `--gender` | `-g` | Wrestler gender | `mixed` |

### Wrestler Types
- `balanced` - Well-rounded stats
- `powerhouse` - High strength and power
- `speedster` - High speed and technique
- `technician` - High technique and grapple
- `veteran` - High overall stats
- `rookie` - Lower overall stats

### Gender Options
- `male` - Male wrestlers only
- `female` - Female wrestlers only
- `mixed` - Mixed gender roster

## 📋 Examples

### Basic Usage
```bash
# Create roster from text file
python3 create_all_rosters.py --file my_names.txt

# Create roster with specific name
python3 create_all_rosters.py --file my_names.txt --output my_roster

# Create roster with 12 wrestlers
python3 create_all_rosters.py --file my_names.txt --count 12
```

### Advanced Usage
```bash
# Create powerhouse roster with 16 male wrestlers
python3 create_all_rosters.py --file strong_guys.txt --count 16 --type powerhouse --gender male --output powerhouse_roster

# Create veteran roster with 20 mixed wrestlers
python3 create_all_rosters.py --file legends.txt --count 20 --type veteran --gender mixed --output hall_of_fame

# Create speedster roster with 8 female wrestlers
python3 create_all_rosters.py --file fast_women.txt --count 8 --type speedster --gender female --output speed_demons
```

## 🎮 Using Created Rosters

After creating rosters, you can use them in the wrestling simulator:

```bash
python -m wrestling_simulator.main
```

When prompted to load a roster, you'll see:
```
Available rosters:
1. custom_roster.pickle (8 wrestlers)
2. powerhouse_roster.pickle (16 wrestlers)
3. hall_of_fame.pickle (20 wrestlers)
Please select a roster (1-3): 2
Loaded powerhouse_roster.pickle with 16 wrestlers
```

## 📁 File Structure

Created rosters are saved in the `rosters/` directory:
```
rosters/
├── custom_roster.pickle
├── powerhouse_roster.pickle
├── hall_of_fame.pickle
└── ...
```

## 🧪 Testing

Test the roster creation functionality:
```bash
python3 test_roster_creator.py
```

## 🎯 Built-in Rosters

When you run without the `--file` option, the script creates these themed rosters:

1. **legendary_males.pickle** - 8 legendary male wrestlers
2. **legendary_females.pickle** - 8 legendary female wrestlers
3. **modern_males.pickle** - 6 modern male wrestlers
4. **modern_females.pickle** - 6 modern female wrestlers
5. **powerhouse_division.pickle** - 4 powerhouse wrestlers
6. **speed_demons.pickle** - 4 speedster wrestlers
7. **technical_masters.pickle** - 6 technical wrestlers
8. **rookie_class.pickle** - 8 rookie wrestlers
9. **mixed_legends.pickle** - 12 mixed legendary wrestlers
10. **indie_stars.pickle** - 6 independent wrestlers
11. **championship_roster_large.pickle** - 16 championship wrestlers
12. **womens_division.pickle** - 10 female wrestlers
13. **hall_of_fame.pickle** - 20 hall of fame wrestlers
14. **tag_teams.pickle** - 4 tag team specialists
15. **rising_stars.pickle** - 8 rising star wrestlers

## 💡 Tips

- Use descriptive output names for easy identification
- Create rosters of different sizes for different tournament types
- Mix wrestler types for balanced competition
- Save your favorite rosters for quick access
- Use comments in text files to organize wrestler names

## 🎉 Happy Wrestling!

Create your dream rosters and enjoy the wrestling simulator! 🥊
