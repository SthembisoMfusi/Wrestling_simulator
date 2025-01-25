import unittest
from createRoster import Roster
from wrestler import Wrestler
import os

class TestRoster(unittest.TestCase):
    def setUp(self):
        # Create a Roster instance for testing
        self.roster = Roster(5)  # Roster with capacity for 5 wrestlers

        # Create dummy wrestler name files for testing
        os.makedirs("wrestler_names", exist_ok=True)
        with open("wrestler_names/Male wrestlers.txt", "w") as f:
            f.write("TestMan1\nTestMan2\nTestMan3")
        with open("wrestler_names/Female wrestlers.txt", "w") as f:
            f.write("TestWoman1\nTestWoman2\nTestWoman3")

    def tearDown(self):
        # Clean up dummy wrestler name files after testing
        os.remove("wrestler_names/Male wrestlers.txt")
        os.remove("wrestler_names/Female wrestlers.txt")
        os.rmdir("wrestler_names")

    def test_auto_create_male(self):
        # Test auto-creation of a male wrestler
        wrestler = self.roster.autoCreate("male")
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.gender, "male")
        self.assertIn(wrestler.name, ["TestMan1", "TestMan2", "TestMan3"])

    def test_auto_create_female(self):
        # Test auto-creation of a female wrestler
        wrestler = self.roster.autoCreate("female")
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.gender, "female")
        self.assertIn(wrestler.name, ["TestWoman1", "TestWoman2", "TestWoman3"])

    def test_auto_create_invalid_gender(self):
        # Test auto-creation with an invalid gender
        with self.assertRaises(ValueError):
            self.roster.autoCreate("invalid")

    # def test_manual_create(self):
    #     # Test manual creation of a wrestler (requires mocking input)
    #     # This is more complex and often not ideal for unit testing
    #     # You might consider integration testing for this instead

    def test_open_file_valid(self):
        # Test opening a valid file
        content = self.roster.openFile("wrestler_names/Male wrestlers.txt")
        self.assertEqual(content, ["TestMan1\n", "TestMan2\n", "TestMan3"])

    def test_open_file_invalid(self):
        # Test opening a non-existent file
        content = self.roster.openFile("nonexistent_file.txt")
        self.assertEqual(content, [])  # Should return an empty list

    def test_fill_roster_manually(self):
        # Test filling the roster manually (requires mocking input)
        # Similar to manualCreate, this is better suited for integration testing

        # Example of how you might mock input for a simple case:
        with unittest.mock.patch("builtins.input", side_effect=["TestMan", "male", "80", "70", "60", "150", "90", "10", "75"]):
            self.roster.fillRoster()
            self.assertEqual(len(self.roster.roster), 5)
            self.assertEqual(self.roster.roster[0].name, "TestMan")

    def test_fill_roster_automatically_male(self):
        # Test filling the roster automatically with male wrestlers
        with unittest.mock.patch("builtins.input", return_value="automatically"):
            with unittest.mock.patch("roster.Roster.autoCreate", side_effect=self.roster.autoCreate):
                self.roster.fillRoster()
                self.assertEqual(len(self.roster.roster), 5)
                for wrestler in self.roster.roster:
                    self.assertEqual(wrestler.gender, "male")

    def test_fill_roster_automatically_female(self):
        # Test filling the roster automatically with female wrestlers
        with unittest.mock.patch("builtins.input", return_value="automatically"):
            with unittest.mock.patch("roster.Roster.autoCreate", side_effect=self.roster.autoCreate):
                self.roster.fillRoster()
                self.assertEqual(len(self.roster.roster), 5)
                for wrestler in self.roster.roster:
                    self.assertEqual(wrestler.gender, "female")

    def test_fill_roster_both(self):
        # Test filling the roster with both automatic and manual entries (requires mocking input)
        # This is also better suited for integration testing

        # Example of mocking input for a mixed case:
        with unittest.mock.patch(
            "builtins.input",
            side_effect=[
                "both",
                "male",
                "automatic",
                "manual",
                "TestMan",
                "male",
                "80",
                "70",
                "60",
                "150",
                "90",
                "10",
                "75",
                "automatic",
                "automatic",
                "automatic",
            ],
        ):
            with unittest.mock.patch("roster.Roster.autoCreate", side_effect=self.roster.autoCreate):
                self.roster.fillRoster()
                self.assertEqual(len(self.roster.roster), 5)

    def test_remove_wrestler_by_index(self):
        # Test removing a wrestler by index
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        self.roster.remove_wrestler(0)
        self.assertEqual(len(self.roster.roster), 0)

    def test_remove_wrestler_by_name(self):
        # Test removing a wrestler by name
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        self.roster.remove_wrestler("Test Wrestler")
        self.assertEqual(len(self.roster.roster), 0)

    def test_remove_wrestler_invalid_index(self):
        # Test removing a wrestler with an invalid index
        with self.assertRaises(ValueError):
            self.roster.remove_wrestler(10)  # Index out of range

    def test_remove_wrestler_invalid_name(self):
        # Test removing a wrestler with an invalid name
        with self.assertRaises(ValueError):
            self.roster.remove_wrestler("Nonexistent Wrestler")

    def test_get_wrestler_by_index(self):
        # Test getting a wrestler by index
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        retrieved_wrestler = self.roster.get_wrestler(0)
        self.assertEqual(retrieved_wrestler, wrestler)

    def test_get_wrestler_by_name(self):
        # Test getting a wrestler by name
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        retrieved_wrestler = self.roster.get_wrestler("Test Wrestler")
        self.assertEqual(retrieved_wrestler, wrestler)

    def test_get_wrestler_invalid_index(self):
        # Test getting a wrestler with an invalid index
        with self.assertRaises(ValueError):
            self.roster.get_wrestler(10)  # Index out of range

    def test_get_wrestler_invalid_name(self):
        # Test getting a wrestler with an invalid name
        with self.assertRaises(ValueError):
            self.roster.get_wrestler("Nonexistent Wrestler")

    def test_save_and_load_roster(self):
        # Test saving and loading the roster
        wrestler1 = Wrestler("Test Wrestler 1", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler2 = Wrestler("Test Wrestler 2", "female", 75, 80, 85, 140, 85, 15, 80)
        self.roster.roster.extend([wrestler1, wrestler2])

        self.roster.save_roster("test_roster.pkl")

        new_roster = Roster(0)  # Create a new empty roster
        new_roster.load_roster("test_roster.pkl")

        self.assertEqual(len(new_roster.roster), 2)
        self.assertEqual(new_roster.roster[0].name, "Test Wrestler 1")
        self.assertEqual(new_roster.roster[1].name, "Test Wrestler 2")

        # Clean up the saved file
        os.remove("test_roster.pkl")

if __name__ == "__main__":
    unittest.main()