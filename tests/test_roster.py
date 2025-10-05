import unittest
from wrestling_simulator.core.roster import Roster
from wrestling_simulator.core.wrestler import Wrestler
import os
from unittest import mock


class TestRoster(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        os.makedirs("temp_test_dir", exist_ok=True)

        # Create dummy wrestler name files for testing
        os.makedirs("temp_test_dir/wrestler_names", exist_ok=True)
        with open("temp_test_dir/wrestler_names/Male wrestlers.txt", "w") as f:
            f.write("TestMan1\nTestMan2\nTestMan3")
        with open("temp_test_dir/wrestler_names/Female wrestlers.txt", "w") as f:
            f.write("TestWoman1\nTestWoman2\nTestWoman3")
        with open("temp_test_dir/wrestler_names/Other wrestlers.txt", "w") as f:
            f.write("TestOther1\nTestOther2\nTestOther3")

        # Create a Roster instance for testing
        self.roster = Roster(5, auto_fill=False)

    def tearDown(self):
        # Clean up the temporary directory
        for root, dirs, files in os.walk("temp_test_dir", topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir("temp_test_dir")

    @mock.patch("wrestling_simulator.core.roster.load_wrestler_names")
    def test_auto_create_male(self, mock_load_names):
        mock_load_names.return_value = ["TestMan1", "TestMan2", "TestMan3"]
        wrestler = self.roster.autoCreate("male")
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.gender, "male")
        self.assertIn(wrestler.name, ["TestMan1", "TestMan2", "TestMan3"])
        # Verify the mock was called
        mock_load_names.assert_called_once_with("male")

    @mock.patch("wrestling_simulator.core.roster.load_wrestler_names")
    def test_auto_create_female(self, mock_load_names):
        mock_load_names.return_value = ["TestWoman1", "TestWoman2", "TestWoman3"]
        wrestler = self.roster.autoCreate("female")
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.gender, "female")
        self.assertIn(wrestler.name, ["TestWoman1", "TestWoman2", "TestWoman3"])

    @mock.patch("wrestling_simulator.core.roster.load_wrestler_names")
    def test_auto_create_other(self, mock_load_names):
        mock_load_names.return_value = ["TestOther1", "TestOther2", "TestOther3"]
        wrestler = self.roster.autoCreate("other")
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.gender, "other")
        self.assertIn(wrestler.name, ["TestOther1", "TestOther2", "TestOther3"])

    def test_auto_create_invalid_gender(self):
        with self.assertRaises(ValueError):
            self.roster.autoCreate("invalid")

    @mock.patch(
        "builtins.input",
        side_effect=["male", "TestMan", "80", "70", "60", "150", "90", "10", "75"],
    )
    def test_manual_create_male(self, mocked_input):
        wrestler = self.roster.manualCreate()
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.name, "TestMan")
        self.assertEqual(wrestler.gender, "male")

    @mock.patch(
        "builtins.input",
        side_effect=["female", "TestWoman", "80", "70", "60", "150", "90", "10", "75"],
    )
    def test_manual_create_female(self, mocked_input):
        wrestler = self.roster.manualCreate()
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.name, "TestWoman")
        self.assertEqual(wrestler.gender, "female")

    @mock.patch(
        "builtins.input",
        side_effect=["TestOther", "80", "70", "60", "150", "90", "10", "75"],
    )
    def test_manual_create_other(self, mocked_input):
        wrestler = self.roster.manualCreate(sex="other")
        self.assertIsInstance(wrestler, Wrestler)
        self.assertEqual(wrestler.name, "TestOther")
        self.assertEqual(wrestler.gender, "other")

    def test_remove_wrestler_by_index(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        self.roster.remove_wrestler(0)
        self.assertEqual(len(self.roster.roster), 0)

    def test_remove_wrestler_by_name(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        self.roster.remove_wrestler("Test Wrestler")
        self.assertEqual(len(self.roster.roster), 0)

    def test_remove_wrestler_invalid_index(self):
        with self.assertRaises(ValueError):
            self.roster.remove_wrestler(10)

    def test_remove_wrestler_invalid_name(self):
        with self.assertRaises(ValueError):
            self.roster.remove_wrestler("Nonexistent Wrestler")

    def test_get_wrestler_by_index(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        retrieved_wrestler = self.roster.get_wrestler(0)
        self.assertEqual(retrieved_wrestler, wrestler)

    def test_get_wrestler_by_name(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.roster.roster.append(wrestler)
        retrieved_wrestler = self.roster.get_wrestler("Test Wrestler")
        self.assertEqual(retrieved_wrestler, wrestler)

    def test_get_wrestler_invalid_index(self):
        with self.assertRaises(ValueError):
            self.roster.get_wrestler(10)

    def test_get_wrestler_invalid_name(self):
        with self.assertRaises(ValueError):
            self.roster.get_wrestler("Nonexistent Wrestler")

    def test_save_and_load_roster(self):
        wrestler1 = Wrestler("Test Wrestler 1", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler2 = Wrestler("Test Wrestler 2", "female", 75, 80, 85, 140, 85, 15, 80)
        self.roster.roster.extend([wrestler1, wrestler2])

        # Use the temporary directory for saving
        save_path = os.path.join("temp_test_dir", "test_roster.pkl")
        self.roster.save_roster(save_path)

        new_roster = Roster()
        new_roster.load_roster(save_path)

        self.assertEqual(len(new_roster.roster), 2)
        self.assertEqual(new_roster.roster[0].name, "Test Wrestler 1")
        self.assertEqual(new_roster.roster[1].name, "Test Wrestler 2")


if __name__ == "__main__":
    unittest.main()
