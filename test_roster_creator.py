#!/usr/bin/env python3
"""
Test script to verify the enhanced roster creation functionality.
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, '.')

def test_roster_creation():
    """Test the roster creation functionality."""
    print("🧪 Testing roster creation functionality...")
    
    try:
        # Import the roster creation functions
        from create_all_rosters import load_wrestler_names_from_file, create_custom_roster
        
        # Test loading names from file
        print("\n1. Testing name loading from file...")
        names = load_wrestler_names_from_file('sample_wrestlers.txt')
        print(f"   ✓ Loaded {len(names)} names from sample_wrestlers.txt")
        print(f"   ✓ First 3 names: {names[:3]}")
        
        # Test creating a custom roster
        print("\n2. Testing custom roster creation...")
        success = create_custom_roster(
            'sample_wrestlers.txt',
            'test_roster',
            'balanced',
            6,
            'mixed'
        )
        
        if success:
            print("   ✓ Custom roster created successfully!")
            
            # Check if the file was created
            roster_file = "rosters/test_roster.pickle"
            if os.path.exists(roster_file):
                print(f"   ✓ Roster file exists: {roster_file}")
                
                # Test loading the roster
                import pickle
                with open(roster_file, 'rb') as f:
                    roster_data = pickle.load(f)
                print(f"   ✓ Roster contains {len(roster_data)} wrestlers")
                print(f"   ✓ First wrestler: {roster_data[0]['name']}")
            else:
                print("   ❌ Roster file was not created")
        else:
            print("   ❌ Failed to create custom roster")
        
        print("\n✅ All tests completed!")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    test_roster_creation()
