"""
Test script to demonstrate improved error messages.
Run this to see the new, more helpful error messages in action!
"""

from wrestling_simulator.core.wrestler import Wrestler
from wrestling_simulator.core.roster import Roster
from wrestling_simulator.utils.validation import validate_tournament_size

print("=" * 60)
print("Testing Improved Error Messages")
print("=" * 60)

# Test 1: Invalid power value
print("\n1. Testing invalid power value (too high):")
try:
    wrestler = Wrestler("Test Wrestler", "male", 70, 65, 50, 120, 105, 10, 60)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 2: Invalid strength value (too low)
print("\n2. Testing invalid strength value (too low):")
try:
    wrestler = Wrestler("Test Wrestler", "male", 30, 65, 50, 120, 75, 10, 60)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 3: Invalid gender
print("\n3. Testing invalid gender:")
try:
    wrestler = Wrestler("Test Wrestler", "alien", 70, 65, 50, 120, 75, 10, 60)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 4: Invalid grapple value
print("\n4. Testing invalid grapple value (too high):")
try:
    wrestler = Wrestler("Test Wrestler", "male", 70, 65, 50, 120, 75, 25, 60)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 5: Invalid health value
print("\n5. Testing invalid health value (too low):")
try:
    wrestler = Wrestler("Test Wrestler", "female", 70, 65, 50, 50, 75, 10, 60)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 6: Invalid tournament size (not power of 2)
print("\n6. Testing invalid tournament size (not power of 2):")
try:
    validate_tournament_size(12)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 7: Invalid tournament size (too small)
print("\n7. Testing invalid tournament size (too small):")
try:
    validate_tournament_size(2)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 8: Invalid tournament size (odd number)
print("\n8. Testing invalid tournament size (odd number):")
try:
    validate_tournament_size(7)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 9: Try to train an invalid stat
print("\n9. Testing training an invalid stat:")
try:
    wrestler = Wrestler("Valid Wrestler", "male", 70, 65, 50, 120, 75, 10, 60)
    wrestler.train("name", 10)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

# Test 10: Try to set invalid attribute
print("\n10. Testing setting invalid attribute:")
try:
    wrestler = Wrestler("Valid Wrestler", "male", 70, 65, 50, 120, 75, 10, 60)
    wrestler.invalid_stat = 100
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

print("\n" + "=" * 60)
print("All error messages are now more helpful and user-friendly! ✓")
print("=" * 60)
