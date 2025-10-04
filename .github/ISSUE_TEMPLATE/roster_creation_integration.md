---
name: Integrate Roster Creation into Main CLI
about: Allow users to create rosters from text files directly in the wrestling simulator
title: "[GOOD FIRST ISSUE] Integrate roster creation from text files into main CLI"
labels: ["good first issue", "enhancement", "cli", "beginner-friendly"]
assignees: []
---

## 🎯 Problem

Currently, users must run a separate script (`create_all_rosters.py`) to create rosters from text files. This creates a poor user experience as users have to exit the wrestling simulator, run another script, then return to the simulator.

## ✨ Solution

Integrate the roster creation functionality directly into the main wrestling simulator CLI so users can create rosters from text files without leaving the application.

## 🔧 Current Behavior

```
Do you want to load a saved roster or create a new roster? [Create, Load]: Create
Please enter the number of wrestlers you want in your roster: 8
[Creates random wrestlers with random names]
```

## 🎯 Desired Behavior

```
Do you want to load a saved roster or create a new roster? [Create, Load]: Create

How would you like to create the roster?
1. Random wrestlers (current method)
2. From text file (new method)
Please select an option (1-2): 2

📁 Creating roster from text file...
Enter the path to your wrestler names file: my_wrestlers.txt
✓ Loaded 12 wrestler names

Choose wrestler type:
1. Balanced
2. Powerhouse
3. Speedster
4. Technician
5. Veteran
6. Rookie
Select type (1-6): 1

Choose gender:
1. Male
2. Female
3. Mixed
Select gender (1-3): 3

Enter the number of wrestlers (1-12): 8
Enter a name for your roster: my_custom_roster
✅ Roster 'my_custom_roster' created successfully!
```

## 📁 Files to Modify

- `wrestling_simulator/cli/main.py` - Add new roster creation flow
- `wrestling_simulator/utils/file_utils.py` - Add text file loading function

## 🛠️ Implementation Steps

### 1. Add Text File Loading Function

Create `load_wrestler_names_from_file()` in `wrestling_simulator/utils/file_utils.py`:

```python
def load_wrestler_names_from_file(file_path):
    """Load wrestler names from a text file."""
    names = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                name = line.strip()
                if name and not name.startswith('#'):
                    names.append(name)
        return names
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []
```

### 2. Add Roster Creation Menu

Add this function to `wrestling_simulator/cli/main.py`:

```python
def get_roster_creation_method():
    """Get user's choice for roster creation method."""
    print("\nHow would you like to create the roster?")
    print("1. Random wrestlers (current method)")
    print("2. From text file (new method)")
    
    while True:
        choice = input("Please select an option (1-2): ").strip()
        if choice in ['1', '2']:
            return choice
        print("Please enter 1 or 2")
```

### 3. Add Text File Roster Creation

Add this function to `wrestling_simulator/cli/main.py`:

```python
def create_roster_from_text_file():
    """Create a roster from a text file with wrestler names."""
    print("\n📁 Creating roster from text file...")
    
    # Get file path
    while True:
        file_path = input("Enter the path to your wrestler names file: ").strip()
        if os.path.exists(file_path):
            break
        print(f"❌ File not found: {file_path}")
        retry = input("Try again? (y/n): ").lower()
        if retry != 'y':
            return None
    
    # Load names
    names = load_wrestler_names_from_file(file_path)
    if not names:
        return None
    
    print(f"✓ Loaded {len(names)} wrestler names")
    
    # Get roster name
    roster_name = input("Enter a name for your roster: ").strip()
    if not roster_name:
        roster_name = "custom_roster"
    
    # Get number of wrestlers
    while True:
        try:
            count = int(input(f"Enter the number of wrestlers (1-{len(names)}): "))
            if 1 <= count <= len(names):
                break
        except ValueError:
            pass
        print("Please enter a valid number")
    
    # Create roster using existing functionality
    # (You'll need to adapt the create_custom_roster function)
    return create_custom_roster_internal(names, roster_name, count)
```

### 4. Update Main Create Logic

Modify the create roster section in the main function:

```python
elif ans.lower() == "create":
    method = get_roster_creation_method()
    
    if method == '1':
        # Current random method
        num = get_valid_wrestler_count()
        wwe = Roster(contestants=num)
    elif method == '2':
        # New text file method
        result = create_roster_from_text_file()
        if not result:
            return
        # Load the created roster
        file_path = os.path.join("rosters", f"{result}.pickle")
        wwe = Roster(contestants=None, file=file_path)
        num = len(wwe.roster)
    
    # Continue with existing save logic...
```

## 🧪 Testing

1. Create a test text file with wrestler names
2. Test the new roster creation flow
3. Verify the created roster appears in the load roster list
4. Test error handling for invalid files
5. Test with different numbers of wrestlers

## 💡 Tips

- Use the existing `create_custom_roster` function from `create_all_rosters.py` as reference
- Handle file errors gracefully with helpful messages
- Use consistent UI patterns with the existing CLI
- Test with various text file formats

## 🎯 Success Criteria

- [ ] Users can choose between random and text file roster creation
- [ ] Text file input is validated with helpful error messages
- [ ] Users can name their custom rosters
- [ ] Created rosters are saved and can be loaded
- [ ] Error handling for invalid files and inputs
- [ ] Consistent UI with existing CLI design

## 📚 Learning Opportunities

- File I/O operations
- User input validation
- CLI design
- Error handling
- Code integration

## 🏷️ Priority: Medium
## ⏱️ Estimated Time: 3-4 hours
## 👥 Difficulty: Beginner to Intermediate
