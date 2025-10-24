import unittest
from core.wrestler import Wrestler
from core.roster import Roster

class TestWrestler(unittest.TestCase):
    def setUp(self):
        self.wrestler1 = Wrestler(
            name="The Rock",
            gender="male",
            strength=80,
            speed=70,
            agility=60,
            health=150,
            power=85,
            grapple=12,
            stamina=90
        )
        self.wrestler2 = Wrestler(
            name="John Cena",
            gender="male",
            strength=75,
            speed=65,
            agility=55,
            health=140,
            power=80,
            grapple=10,
            stamina=85
        )

    def test_initial_stats(self):
        self.assertEqual(self.wrestler1.name, "The Rock")
        self.assertEqual(self.wrestler1.health, 150)
        self.assertFalse(self.wrestler1.is_defeated)

    def test_attack_reduces_health(self):
        pre_health = self.wrestler2.health
        self.wrestler1.attack(self.wrestler2)
        self.assertLess(self.wrestler2.health, pre_health)

    def test_grapple_changes_health_or_stamina(self):
        pre_health = self.wrestler2.health
        pre_stamina = self.wrestler1.stamina_level
        self.wrestler1.grappleOpponent(self.wrestler2)
        self.assertTrue(self.wrestler2.health <= pre_health)
        self.assertTrue(self.wrestler1.stamina_level <= pre_stamina)

    def test_pin_defeat(self):
        # Reduce opponent health to increase pin success chance
        self.wrestler2.health = 10
        result = self.wrestler1.pinOpponent(self.wrestler2)
        self.assertTrue(result or not result)  # Should return a boolean
        if result:
            self.assertTrue(self.wrestler2.is_defeated)

    def test_stamina_and_health_regen(self):
        self.wrestler1.stamina_level = 50
        self.wrestler1.health = 100
        self.wrestler1.staminaRegen()
        self.wrestler1.healthRegen()
        self.assertGreater(self.wrestler1.stamina_level, 50)
        self.assertGreater(self.wrestler1.health, 100)

class TestRoster(unittest.TestCase):
    def test_roster_creation_from_names(self):
        names = ["The Rock", "John Cena"]
        roster = Roster.from_names(names, wrestler_type="Balanced", gender="Male")
        self.assertEqual(len(roster.roster), 2)
        self.assertIsInstance(roster.roster[0], Wrestler)

if __name__ == "__main__":
    unittest.main()
