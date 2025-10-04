---
name: Integrate Roster Creation into Main CLI
about: Allow users to create rosters directly from the wrestling simulator interface
title: "[FEATURE] Integrate roster creation into main CLI with text file input"
labels: ["enhancement", "good first issue", "cli", "user experience"]
assignees: []
---

## 🎯 Feature Request

Integrate the roster creation functionality into the main wrestling simulator CLI so users can create rosters directly from the interface without needing to run separate scripts.

## 📋 Current Behavior

Currently, users must:
1. Run the wrestling simulator: `python -m wrestling_simulator.main`
2. Choose "Create" to create a roster
3. Enter the number of wrestlers
4. The system generates random wrestlers with random names

## ✨ Desired Behavior

Users should be able to:
1. Run the wrestling simulator: `python -m wrestling_simulator.main`
2. Choose "Create" to create a roster
3. **NEW**: Choose between "Random" or "From File" roster creation
4. **NEW**: If "From File" is chosen:
   - Prompt for text file path
   - Validate the file exists and contains wrestler names
   - Allow user to choose wrestler type (balanced, powerhouse, etc.)
   - Allow user to choose gender (male, female, mixed)
   - Allow user to set the number of wrestlers
   - Allow user to name the roster
   - Create the roster and save it to the rosters folder
   - Confirm successful creation

## 🛠️ Implementation Tasks

### 1. Update CLI Menu (in `wrestling_simulator/cli/main.py`)

Add a new menu option for roster creation:

```python
def get_roster_creation_choice():
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

### 2. Add Text File Roster Creation Function

```python
def create_roster_from_file():
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
    
    # Load names from file
    names = load_wrestler_names_from_file(file_path)
    if not names:
        print("❌ No valid wrestler names found in file")
        return None
    
    print(f"✓ Loaded {len(names)} wrestler names")
    
    # Get roster configuration
    wrestler_type = get_wrestler_type()
    gender = get_gender_choice()
    count = get_wrestler_count(len(names))
    roster_name = get_roster_name()
    
    # Create roster
    success = create_custom_roster(file_path, roster_name, wrestler_type, count, gender)
    
    if success:
        print(f"✅ Roster '{roster_name}' created successfully!")
        return roster_name
    else:
        print("❌ Failed to create roster")
        return None
```

### 3. Add Helper Functions

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
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []

def get_wrestler_type():
    """Get wrestler type from user."""
    types = ['balanced', 'powerhouse', 'speedster', 'technician', 'veteran', 'rookie']
    print("\nChoose wrestler type:")
    for i, t in enumerate(types, 1):
        print(f"{i}. {t.title()}")
    
    while True:
        try:
            choice = int(input(f"Select type (1-{len(types)}): "))
            if 1 <= choice <= len(types):
                return types[choice - 1]
        except ValueError:
            pass
        print("Please enter a valid number")

def get_gender_choice():
    """Get gender choice from user."""
    print("\nChoose gender:")
    print("1. Male")
    print("2. Female") 
    print("3. Mixed")
    
    while True:
        choice = input("Select gender (1-3): ").strip()
        if choice == '1':
            return 'male'
        elif choice == '2':
            return 'female'
        elif choice == '3':
            return 'mixed'
        print("Please enter 1, 2, or 3")

def get_roster_name():
    """Get roster name from user."""
    while True:
        name = input("Enter a name for your roster: ").strip()
        if name:
            return name
        print("Please enter a valid roster name")
```

### 4. Update Main Create Roster Logic

Modify the existing create roster section in `main()`:

```python
elif ans.lower() == "create":
    # Get creation method
    creation_method = get_roster_creation_choice()
    
    if creation_method == '1':
        # Current random method
        num = get_valid_wrestler_count()
        wwe = Roster(contestants=num)
    elif creation_method == '2':
        # New file method
        roster_name = create_roster_from_file()
        if not roster_name:
            return
        # Load the created roster
        file_path = os.path.join("rosters", f"{roster_name}.pickle")
        wwe = Roster(contestants=None, file=file_path)
        num = len(wwe.roster)
    
    # Continue with existing save logic...
```

### 5. Import Required Functions

Add imports at the top of `wrestling_simulator/cli/main.py`:

```python
from ..utils.file_utils import load_wrestler_names
from ..core.roster import Roster
import os
```

## 🧪 Testing Requirements

1. **Test file input validation**:
   - Valid file with wrestler names
   - Non-existent file
   - Empty file
   - File with only comments

2. **Test roster creation flow**:
   - Complete flow from file selection to roster creation
   - Different wrestler types and genders
   - Different roster sizes
   - Custom roster names

3. **Test integration**:
   - Ensure created rosters appear in the load roster list
   - Verify roster can be loaded and used in tournaments
   - Test error handling for invalid inputs

## 💡 Implementation Hints

- Use the existing `create_custom_roster` function from `create_all_rosters.py`
- Reuse validation logic from the standalone script
- Provide clear error messages for invalid inputs
- Use consistent UI patterns with the existing CLI
- Handle file encoding issues gracefully

## 🎯 Success Criteria

- [ ] Users can choose between random and file-based roster creation
- [ ] File input is validated with helpful error messages
- [ ] Users can configure wrestler type, gender, and count
- [ ] Users can name their custom rosters
- [ ] Created rosters are saved to the rosters folder
- [ ] Created rosters appear in the load roster list
- [ ] Error handling for invalid files and inputs
- [ ] Consistent UI with existing CLI design

## 📚 Learning Opportunities

- File I/O operations and validation
- User input handling and validation
- CLI design and user experience
- Error handling and user feedback
- Code integration and refactoring
- Function organization and modularity

## 🏷️ Priority: Medium
## ⏱️ Estimated Time: 4-6 hours
## 👥 Difficulty: Intermediate
