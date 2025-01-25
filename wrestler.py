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
        self.strength = strength
        self.speed = speed
        self.agility = agility
        self.health = health
        self.power = power
        self.grapple = grapple
        self.stamina = stamina
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

    def __str__(self):
        return f"name: {self.name}, gender: {self.gender}, strength: {self.strength}, speed: {self.speed}, agility: {self.agility}, health: {self.health}, power: {self.power}, grapple: {self.grapple}, stamina: {self.stamina}"

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
        if stat == "name" or stat == "gender":
            raise ValueError("Cannot train this stat")
        current_value = getattr(self, stat)
        # Example limitation: prevent stats from exceeding a maximum
        max_value = 100 if stat != "health" else 200
        if stat != "grapple":
            new_value = min(current_value + amount, max_value)
        else:
            new_value = min(current_value + amount, 20)
        setattr(self, stat, new_value)

    def take_damage(self, damage):
        self.health -= int(damage)
        if self.health < 0:
            self.health = 0  # Prevent negative health

    def attack(self, opponent):
        # Basic attack calculation 
        damage = self.power * (1 - opponent.strength / 200)  # Example: strength reduces damage
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")


# de = Wrestler("Test Wrestler", "male", 80, 70, 60, 150, 90, 10, 75)
# print(de.get_overall_rating())