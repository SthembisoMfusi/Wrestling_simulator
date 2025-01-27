import random
class Wrestler:
    statList = [
        "name",
        "gender",
        "strength",
        "speed",
        "agility",
        "health",
        "power",
        "grapple",
        "stamina",
    ]
    genders = ["male", "female", "other"] 

    def __init__(
        self,
        name: str,
        gender: str,
        strength: int,
        speed: int,
        agility: int,
        health: int,
        power: int,
        grapple: int,
        stamina: int,
    ):
        self.name = name
        self.gender = gender
        self.strength = strength #how restistant they are to damage
        self.speed = speed  #how quickly they can react to attacks and how quickly they can issue attacks
        self.agility = agility  # how well they can break out of grapples  and pins
        self.max_health = health    # how much damage they can take
        self.health = health
        self.power = power      # how much damage they can deal
        self.grapple = grapple  # how well they can grapple
        self.stamina = stamina  # how often they can use different moves
        self.stamina_level = 100
        if self.health < 80 or self.health > 200:
            raise ValueError 

    def __setattr__(self, name, value):
        match name:
            case "name":
                if not isinstance(value, str):
                    raise ValueError("name must be a string value")
            case "gender":
                if not isinstance(value, str) or value not in self.genders:
                    raise ValueError(
                        "gender must be a str value and should be either 'male' or 'female' "
                    )
            case "strength":
                if not isinstance(value, int) or value < 40 or value > 100:
                    raise ValueError("Strength value is invalid, it should be between 40 and 100")
            case "speed":
                if not isinstance(value, int) or value < 30 or value > 100:
                    raise ValueError("Speed value is invalid, it should be between 30 and 100")
            case "agility":
                if not isinstance(value, int) or value < 10 or value > 100:
                    raise ValueError("Agility value is invalid, it should be between 10 and 100")
            case "health":
                if not isinstance(value, int) :
                    raise ValueError("Health value is invalid, it should be an integer")
            case "power":
                if not isinstance(value, int) or value < 50 or value > 100:
                    raise ValueError("Power value is invalid, it should be between 50 and 100")
            case "grapple":
                if not isinstance(value, int) or value < 1 or value > 20:
                    raise ValueError("Grapple value is invalid, it should be between 1 and 20")
            case "stamina":
                if not isinstance(value, int) or value < 30 or value > 100:
                    raise ValueError("Stamina value is invalid, it should be between 30 and 100")
        if name not in self.statList:
            raise ValueError(f"only these stats can be changed : {self.statList}")
        self.__dict__[name] = value
    def showStats(self):
        return f"name: {self.name}, gender: {self.gender}, strength: {self.strength}, speed: {self.speed}, agility: {self.agility}, health: {self.health}, power: {self.power}, grapple: {self.grapple}, stamina: {self.stamina}"
    def __str__(self):
        return f"name: {self.name}"

    def __repr__(self):
        return str(self)

    def get_overall_rating(self):
        weights = {
            "strength": 0.2,
            "speed": 0.15,
            "agility": 0.15,
            "health": 0.1,
            "power": 0.2,
            "grapple": 0.1,
            "stamina": 0.1,
        }
        overall = 0
        for stat, weight in weights.items():
            overall += getattr(self, stat) * weight
        return overall

    def train(self, stat, amount):
        if stat not in self.statList:
            raise ValueError("Invalid stat to train.")
        if stat == "name" or stat == "gender" or stat == "health":
            raise ValueError("Cannot train this stat")
        current_value = getattr(self, stat)
        # Example limitation: prevent stats from exceeding a maximum
        max_value = 100 if stat != "max_health" else 200
        if stat != "grapple":
            new_value = min(current_value + amount, max_value)
        else:
            new_value = min(current_value + amount, 20)
        setattr(self, stat, new_value)

    def takeDamage(self, damage):
        '''Used to inflict the damage taken by a wrestler
            Args:
                damage(int|float): the amount of damage the wrestler will take
            Returns:
                    None, it only applies the damage to the wrestler's health
        '''
        self.health -= int(damage)
        if self.health < 0:
            self.health = 0  # Prevent negative health
    def staminaRegen(self):
        ''' used to calculate the amount of stamina a wrestler regenerates
            Args:
                None
            Returns:
                None

        '''
        rate  = (self.stamina/100) * 20
        self.stamina_level + int(rate) 
    def healthRegen(self):
        ''' Used to calculate the amount of health a wrestler regenerates
            Args: 
                None
            Returns:
                None
        '''
        regen = (self.max_health/ 200) * 10
        self.health += regen
        if self.health > self.max_health:
            self.health = self.max_health

    def attack(self, opponent):
        ''' Basic attack move that can be used by a wrestler
            Args: 
                opponent(wrestler): the target who is being attacked
            Returns:
                    None, at the end the opponent's name and the damage they took is displayed
        ''' 
        damage = self.power * (1 - opponent.strength / 200)  # Example: strength reduces damage
        opponent.takeDamage(damage)
        self.stamina_level -= 10
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
    def grapple(self,opponent):
        '''Used to handle the grapple move used by a wrestler
            Args:
                opponent(wrestler): the target of the grapple
            Returns:
                None
        '''
        grapple_chance = self.grapple * 7.5
        escape_chance = opponent.agility * 1.5
        chances = [grapple_chance,escape_chance]
        outcome = [True,False]
        calc = random.choices(outcome,chances)
        if calc == True:
            print(f"{self.name} grapples {opponent.name}!")
            damage = (self.grapple * 8) * (1 - opponent.strength / 200)
            opponent.takeDamage(damage)
            print(f"{opponent.name} takes {damage} damage from the grapple.")
            self.stamina_level -= 30
        else:
            print(f"{opponent.name} escapes the grapple!")
            self.stamina_level -= 20
    def pinOpponent(self,opponent):
        '''Used to detemine the success of a pin manuver
            Args:
                opponent(wrestler): the target of the pin
            Returns:
                    True or False(boolean): this will be used to end a match. if true is returned,
                    the match will the end and self will be declared the winner 

        '''
        chance = ["self", "opponent"]
        if (self.stamina_level + self.health)/ (opponent.stamina_level + opponent.health) >= 1.5:
            possibilities = [random.choices(chance,[2,1],k = 3)]
            if possibilities.count("self") >= 2:
                for i in range(1,4):
                    print(f"{i}...")
                print(f"The winner is {self.name}!!!")
                return True
            elif possibilities.count("opponent") >= 2:
                for i in range(1,3):
                    print(f"{i}...")
                print(f'{opponent.name} kicks out!!')
                self.stamina_level -=20
                return False
        elif (opponent.stamina_level + opponent.health)/ (self.stamina_level + self.health)  >= 1.5:
            possibilities = [random.choices(chance,[1,2],k = 3)]
            if possibilities.count('self') == 3:
                for i in range(1,4):
                    print(f"{i}...")
                print(f"The winner is {self.name}!!! In an unlikely turn of events!")
                return True
            elif possibilities.count("opponent") >= 2:
                count = random.choice(1,2)
                for i in range(1,count):
                    print(f"{i}...")
                print(f"{opponent.name} kicks out!!")
                self.stamina_level -= 20
                return False
        else:
            possibilities = [random.choices(chance,k = 3)]
            if possibilities.count("self") ==3:
                for i in range(1,4):
                    print(f"{i}...")
                print(f"{self.name} wins with a quick pin!!!")
                return True
            else:
                print(f"1...")
                print(f'{opponent.name}quickly kicks out')
                return False


# de = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
# print(de.get_overall_rating())