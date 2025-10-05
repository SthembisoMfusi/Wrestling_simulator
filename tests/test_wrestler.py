import unittest
from wrestling_simulator.core.wrestler import Wrestler


class TestWrestler(unittest.TestCase):
    def test_create_valid_wrestler(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.assertEqual(wrestler.name, "Test Wrestler")
        self.assertEqual(wrestler.gender, "male")
        self.assertEqual(wrestler.strength, 80)
        self.assertEqual(wrestler.speed, 70)
        self.assertEqual(wrestler.agility, 60)
        self.assertEqual(wrestler.health, 150)
        self.assertEqual(wrestler.power, 90)
        self.assertEqual(wrestler.grapple, 10)
        self.assertEqual(wrestler.stamina, 75)

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Wrestler(123, "male", 80, 70, 60, 150, 90, 10, 75)

    def test_invalid_gender(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "robot", 80, 70, 60, 150, 90, 10, 75)

    def test_invalid_strength_low(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 39, 70, 60, 150, 90, 10, 75)

    def test_invalid_strength_high(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 101, 70, 60, 150, 90, 10, 75)

    def test_invalid_speed_low(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 29, 60, 150, 90, 10, 75)

    def test_invalid_speed_high(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 101, 60, 150, 90, 10, 75)

    def test_invalid_agility_low(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 9, 150, 90, 10, 75)

    def test_invalid_agility_high(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 101, 150, 90, 10, 75)

    def test_invalid_health_low(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 79, 90, 10, 75)

    def test_invalid_health_high(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 201, 90, 10, 75)

    def test_invalid_power_low(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 49, 10, 75)

    def test_invalid_power_high(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 101, 10, 75)

    def test_invalid_grapple_low(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 0, 75)

    def test_invalid_grapple_high(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 21, 75)

    def test_invalid_stamina_low(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 29)

    def test_invalid_stamina_high(self):
        with self.assertRaises(ValueError):
            Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 101)

    def test_get_overall_rating(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        self.assertAlmostEqual(wrestler.get_overall_rating(), 77.0)

    def test_train(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.train("strength", 5)
        self.assertEqual(wrestler.strength, 85)

    def test_train_invalid_stat(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        with self.assertRaises(ValueError):
            wrestler.train("invalid_stat", 5)

    def test_train_untrainable_stat(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        with self.assertRaises(ValueError):
            wrestler.train("name", 5)

    def test_train_max_limit(self):
        wrestler = Wrestler("Test Wrestler", "male", 98, 70, 60, 150, 90, 10, 75)
        wrestler.train("strength", 5)
        self.assertEqual(wrestler.strength, 100)

    def test_takeDamage(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.takeDamage(20)
        self.assertEqual(wrestler.health, 130)

    def test_takeDamage_zero_health(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.takeDamage(160)
        self.assertEqual(wrestler.health, 0)

    def test_attack(self):
        wrestler1 = Wrestler("Wrestler 1", "male", 90, 70, 60, 150, 90, 10, 75)
        wrestler2 = Wrestler("Wrestler 2", "male", 80, 70, 60, 150, 80, 10, 75)
        wrestler1.attack(wrestler2)
        self.assertLess(wrestler2.health, 150)

    def test_stamina_regen(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.stamina_level = 50
        wrestler.staminaRegen()
        self.assertEqual(wrestler.stamina_level, 65)

    def test_health_regen(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.health = 100
        wrestler.healthRegen()
        self.assertEqual(wrestler.health, 107)

    def test_pin_opponent_low_health_success(self):
        wrestler1 = Wrestler("Wrestler 1", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler2 = Wrestler("Wrestler 2", "male", 80, 70, 60, 150, 80, 10, 75)
        wrestler2.health = 30  # Very low health
        result = wrestler1.pinOpponent(wrestler2)
        self.assertTrue(result)  # Pin should succeed
        self.assertTrue(wrestler2.is_defeated)

    def test_pin_opponent_mid_health_mixed(self):
        # This test depends on randomness, so we run it a few times
        success_count = 0
        for _ in range(10):
            wrestler1 = Wrestler("Wrestler 1", "male", 80, 70, 60, 150, 90, 10, 75)
            wrestler2 = Wrestler("Wrestler 2", "male", 80, 70, 60, 150, 80, 10, 75)
            wrestler2.reset()
            wrestler2.health = 75  # Around half health
            if wrestler1.pinOpponent(wrestler2):
                success_count += 1
        # We expect some successes and some failures due to the random nature
        self.assertGreater(success_count, 0)
        self.assertLessEqual(success_count, 10)

    def test_defeat(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.defeat()
        self.assertTrue(wrestler.is_defeated)

    def test_reset(self):
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.defeat()
        wrestler.reset()
        self.assertFalse(wrestler.is_defeated)


if __name__ == "__main__":
    unittest.main()
