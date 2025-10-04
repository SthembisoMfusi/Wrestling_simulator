import unittest
from wrestling_simulator.core.tournament import Tournament
from wrestling_simulator.core.roster import Roster
from wrestling_simulator.core.wrestler import Wrestler


class TestTournament(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a test roster with 8 wrestlers
        self.roster = Roster(8, auto_fill=False)
        # Mock the fillRoster method to avoid user input
        self.roster.roster = [
            Wrestler("Wrestler1", "male", 80, 70, 60, 150, 90, 10, 75),
            Wrestler("Wrestler2", "female", 75, 80, 85, 140, 85, 15, 80),
            Wrestler("Wrestler3", "male", 85, 65, 70, 160, 95, 12, 70),
            Wrestler("Wrestler4", "female", 70, 90, 80, 130, 80, 18, 85),
            Wrestler("Wrestler5", "male", 90, 60, 65, 170, 100, 8, 65),
            Wrestler("Wrestler6", "female", 65, 95, 90, 120, 75, 20, 90),
            Wrestler("Wrestler7", "male", 95, 55, 60, 180, 100, 6, 60),
            Wrestler("Wrestler8", "female", 60, 100, 95, 110, 70, 20, 95),
        ]

    def test_tournament_creation_valid_participants(self):
        """Test tournament creation with valid number of participants."""
        tournament = Tournament(self.roster, 8)
        self.assertEqual(tournament.participants, 8)
        self.assertEqual(len(tournament.wrestlers), 8)
        self.assertEqual(len(tournament.tournamentPool), 4)  # 8 wrestlers = 4 matches

    def test_tournament_creation_invalid_participants(self):
        """Test tournament creation with invalid number of participants."""
        with self.assertRaises(ValueError):
            Tournament(self.roster, 3)  # Not divisible by 2

    def test_tournament_creation_too_few_participants(self):
        """Test tournament creation with too few participants."""
        with self.assertRaises(ValueError):
            Tournament(self.roster, 2)  # Less than 4

    def test_create_tournament_pool(self):
        """Test tournament pool creation."""
        tournament = Tournament(self.roster, 8)
        pool = tournament.createTournamentPool(tournament.wrestlers)
        self.assertEqual(len(pool), 4)  # 8 wrestlers = 4 matches
        for match in pool:
            self.assertIsInstance(match, tuple)
            self.assertEqual(len(match), 2)  # Each match has 2 wrestlers

    def test_tournament_roster_selection(self):
        """Test that tournament selects unique wrestlers."""
        tournament = Tournament(self.roster, 4)
        selected_names = [wrestler.name for wrestler in tournament.wrestlers]
        self.assertEqual(len(selected_names), len(set(selected_names)))  # All unique

    def test_match_simulation(self):
        """Test that a match can be simulated and returns a winner."""
        tournament = Tournament(self.roster, 4)
        wrestler1 = tournament.wrestlers[0]
        wrestler2 = tournament.wrestlers[1]
        
        winner = tournament.match(wrestler1, wrestler2)
        self.assertIsInstance(winner, Wrestler)
        self.assertIn(winner, [wrestler1, wrestler2])

    def test_round_simulation(self):
        """Test that a round can be simulated."""
        tournament = Tournament(self.roster, 8)
        initial_pool_size = len(tournament.tournamentPool)
        tournament.Round()
        # After one round, we should have half as many matches
        self.assertEqual(len(tournament.tournamentPool), initial_pool_size // 2)

    def test_tournament_play_completes(self):
        """Test that a full tournament can be played to completion."""
        tournament = Tournament(self.roster, 4)  # Smaller tournament for faster testing
        # This should complete without errors
        tournament.tournamentPlay()
        # Tournament should be complete (winner determined)
        # The tournament pool might still have 1 entry representing the final match
        self.assertLessEqual(len(tournament.tournamentPool), 1)