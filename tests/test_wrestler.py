import unittest
from wrestler import Wrestler

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

    def test_take_damage(self):
      
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.take_damage(20)
        self.assertEqual(wrestler.health, 130)

    def test_take_damage_zero_health(self):
       
        wrestler = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
        wrestler.take_damage(160)
        self.assertEqual(wrestler.health, 0)

    def test_attack(self):
      
        wrestler1 = Wrestler("Wrestler 1", "male", 90, 70, 60, 150, 90, 10, 75)
        wrestler2 = Wrestler("Wrestler 2", "male", 80, 70, 60, 150, 80, 10, 75)
        wrestler1.attack(wrestler2)
        self.assertLess(wrestler2.health, 150)  

if __name__ == "__main__":
    unittest.main()