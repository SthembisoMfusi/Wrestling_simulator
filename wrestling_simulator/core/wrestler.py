"""
Wrestler class for the wrestling simulator.

This module contains the Wrestler class which represents a single wrestler
with their attributes and combat actions.
"""
"""
Constants for the wrestling simulator.
"""

import random
from typing import Union

from ..constants import (
    MIN_STRENGTH,
    MAX_STRENGTH,
    MIN_SPEED,
    MAX_SPEED,
    MIN_AGILITY,
    MAX_AGILITY,
    MIN_HEALTH,
    MAX_HEALTH,
    MIN_POWER,
    MAX_POWER,
    MIN_GRAPPLE,
    MAX_GRAPPLE,
    MIN_STAMINA,
    MAX_STAMINA,
    VALID_GENDERS,
    DEFAULT_STAMINA_LEVEL,
)



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
        "max_health",
        "is_defeated",
        "stamina_level",
    ]
    genders = VALID_GENDERS

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
    ) -> None:
        self.name = name
        self.gender = gender
        self.strength = strength  # how resistant they are to damage
        self.speed = speed  # how quickly they can react to attacks and how quickly they can issue attacks
        self.agility = agility  # how well they can break out of grapples and pins
        self.max_health = health  # how much damage they can take
        self.health = health
        self.power = power  # how much damage they can deal
        self.grapple = grapple  # how well they can grapple
        self.stamina = stamina  # how often they can use different moves
        self.stamina_level = DEFAULT_STAMINA_LEVEL
        if self.health < MIN_HEALTH or self.health > MAX_HEALTH:
            raise ValueError(
                f"Invalid health value: {health}. Health must be between {MIN_HEALTH}-{MAX_HEALTH}. "
                f"Try a value like {(MIN_HEALTH + MAX_HEALTH) // 2} or {MAX_HEALTH - 20}."
            )
        self.is_defeated = False

    def __setattr__(self, name: str, value: Union[str, int, bool]) -> None:
        match name:
            case "name":
                if not isinstance(value, str):
                    raise ValueError(
                        f"Invalid name type: {type(value).__name__}. Name must be a string. "
                        f"Example: 'The Rock' or 'John Cena'."
                    )
            case "gender":
                if not isinstance(value, str) or value not in self.genders:
                    raise ValueError(
                        f"Invalid gender: '{value}'. Gender must be one of {self.genders}. "
                        f"Please use 'male', 'female', or 'other'."
                    )
            case "strength":
                if (
                    not isinstance(value, int)
                    or value < MIN_STRENGTH
                    or value > MAX_STRENGTH
                ):
                    raise ValueError(
                        f"Invalid strength value: {value}. Strength must be between {MIN_STRENGTH}-{MAX_STRENGTH}. "
                        f"This determines damage resistance. Try a value like 70 or 85."
                    )
            case "speed":
                if not isinstance(value, int) or value < MIN_SPEED or value > MAX_SPEED:
                    raise ValueError(
                        f"Invalid speed value: {value}. Speed must be between {MIN_SPEED}-{MAX_SPEED}. "
                        f"This affects attack and reaction speed. Try a value like 65 or 80."
                    )
            case "agility":
                if (
                    not isinstance(value, int)
                    or value < MIN_AGILITY
                    or value > MAX_AGILITY
                ):
                    raise ValueError(
                        f"Invalid agility value: {value}. Agility must be between {MIN_AGILITY}-{MAX_AGILITY}. "
                        f"This helps escape grapples and pins. Try a value like 50 or 75."
                    )
            case "health":
                if not isinstance(value, int):
                    raise ValueError(
                        f"Invalid health type: {type(value).__name__}. Health must be an integer. "
                        f"Try a value between {MIN_HEALTH} and {MAX_HEALTH}, like 120 or 160."
                    )
            case "power":
                if not isinstance(value, int) or value < MIN_POWER or value > MAX_POWER:
                    raise ValueError(
                        f"Invalid power value: {value}. Power must be between {MIN_POWER}-{MAX_POWER}. "
                        f"This determines attack damage. Try a value like 75 or 90."
                    )
            case "grapple":
                if (
                    not isinstance(value, int)
                    or value < MIN_GRAPPLE
                    or value > MAX_GRAPPLE
                ):
                    raise ValueError(
                        f"Invalid grapple value: {value}. Grapple must be between {MIN_GRAPPLE}-{MAX_GRAPPLE}. "
                        f"This affects grappling success. Try a value like 10 or 15."
                    )
            case "stamina":
                if (
                    not isinstance(value, int)
                    or value < MIN_STAMINA
                    or value > MAX_STAMINA
                ):
                    raise ValueError(
                        f"Invalid stamina value: {value}. Stamina must be between {MIN_STAMINA}-{MAX_STAMINA}. "
                        f"This controls special move frequency. Try a value like 60 or 80."
                    )
            case "is_defeated":
                if not isinstance(value, bool):
                    raise ValueError(
                        f"Invalid is_defeated value: {value}. This can only be True or False."
                    )
        if name not in self.statList:
            raise ValueError(
                f"Cannot set attribute '{name}'. Only these stats can be changed: {', '.join(self.statList)}"
            )
        self.__dict__[name] = value

    def showStats(self) -> str:
        return f"name: {self.name}, gender: {self.gender}, strength: {self.strength}, speed: {self.speed}, agility: {self.agility}, health: {self.health}, power: {self.power}, grapple: {self.grapple}, stamina: {self.stamina}"

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return str(self)

    def get_overall_rating(self) -> float:
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

    def train(self, stat: str, amount: int) -> None:
        if stat not in self.statList:
            raise ValueError(
                f"Cannot train '{stat}'. Valid stats to train are: {', '.join(self.statList)}. "
                f"Try 'strength', 'speed', or 'power'."
            )
        if stat == "name" or stat == "gender" or stat == "health":
            raise ValueError(
                f"Cannot train '{stat}'. This stat cannot be improved through training. "
                f"Try training 'strength', 'speed', 'agility', 'power', 'grapple', or 'stamina' instead."
            )
        current_value = getattr(self, stat)
        # Example limitation: prevent stats from exceeding a maximum
        max_value = 100 if stat != "max_health" else 200
        if stat != "grapple":
            new_value = min(current_value + amount, max_value)
        else:
            new_value = min(current_value + amount, 20)
        setattr(self, stat, new_value)

    def takeDamage(self, damage: Union[int, float]) -> None:
        """Used to inflict the damage taken by a wrestler
        Args:
            damage(int|float): the amount of damage the wrestler will take
        Returns:
                None, it only applies the damage to the wrestler's health
        """
        self.health -= int(damage)
        if self.health < 0:
            self.health = 0  # Prevent negative health

    def staminaRegen(self) -> None:
        """used to calculate the amount of stamina a wrestler regenerates
        Args:
            None
        Returns:
            None

        """
        rate = (self.stamina / 100) * 20
        self.stamina_level += int(rate)
        if self.stamina_level > 100:
            self.stamina_level = 100

    def healthRegen(self) -> None:
        """Used to calculate the amount of health a wrestler regenerates
        Args:
            None
        Returns:
            None
        """
        regen = (self.max_health / 200) * 10
        self.health += int(regen)
        if self.health > self.max_health:
            self.health = self.max_health

    def attack(self, opponent: "Wrestler") -> None:
        """Basic attack move that can be used by a wrestler
        Args:
            opponent(wrestler): the target who is being attacked
        Returns:
                None, at the end the opponent's name and the damage they took is displayed
        """
        damage = self.power * (1 - opponent.strength / 200)  # strength reduces damage
        opponent.takeDamage(damage)
        self.stamina_level -= 30
        if self.stamina_level < 0:
            self.stamina_level = 0
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def grappleOpponent(self, opponent: "Wrestler") -> None:
        """Used to handle the grapple move used by a wrestler
        Args:
            opponent(wrestler): the target of the grapple
        Returns:
            None
        """
        grapple_chance = self.grapple * 7.5
        escape_chance = opponent.agility
        chances = [grapple_chance, escape_chance]
        outcome = [True, False]
        calc = random.choices(outcome, chances, k=1)[0]  # Ensure a boolean result
        print(f"{self.name} attempts to grapple {opponent.name}!")
        if calc:
            print(f"{self.name} successfully grapples {opponent.name}!")
            damage = (self.grapple * 8) * (1 - opponent.strength / 200)
            opponent.takeDamage(damage)
            print(f"{opponent.name} takes {damage} damage from the grapple.")
            self.stamina_level -= 70
        else:
            print(f"{opponent.name} escapes the grapple!")
            self.stamina_level -= 45

        if self.stamina_level < 0:
            self.stamina_level = 0

    def pinOpponent(self, opponent: "Wrestler") -> bool:
        """Used to detemine the success of a pin manuver
        Args:
            opponent(wrestler): the target of the pin
        Returns:
                True or False(boolean): this will be used to end a match. if true is returned,
                the match will the end and self will be declared the winner

        """
        chance = ["self", "opponent"]
        if opponent.health == opponent.max_health:
            possibilities = random.choices(chance, [2, 1], k=3)
            if possibilities.count("self") >= 2:
                for i in range(1, 4):
                    print(f"{i}...")
                print(
                    f"The winner is {self.name}! With a quick pin to end the match quickly"
                )
                opponent.defeat()
                return True  # Indicate successful pin
        elif opponent.health <= opponent.max_health // 4:
            possibilities = random.choices(chance, [5, 1], k=3)
            if possibilities.count("self") >= 1:
                for i in range(1, 4):
                    print(f"{i}...")
                print(f"The winner is {self.name}!!!")
                opponent.defeat()
                return True  # Indicate successful pin
            elif possibilities.count("opponent") == 3:
                for i in range(1, 3):
                    print(f"{i}...")
                print(f"{opponent.name} kicks out!!")
                self.stamina_level -= 40
        else:
            if opponent.health >= opponent.max_health // 2:
                possibilities = random.choices(chance, [2, 1], k=3)
                if possibilities.count("self") >= 1:
                    for i in range(1, 4):
                        print(f"{i}...")
                    print(f"The winner is {self.name}!!!")
                    opponent.defeat()
                    return True  # Indicate successful pin
                elif possibilities.count("opponent") >= 2:
                    for i in range(1, 3):
                        print(f"{i}...")
                    print(f"{opponent.name} kicks out!!")
                    opponent.stamina_level -= 40

            elif opponent.health <= opponent.max_health // 3:
                possibilities = random.choices(chance, [3, 1], k=3)
                if possibilities.count("self") >= 2:
                    for i in range(1, 4):
                        print(f"{i}...")
                    print(
                        f"The winner is {self.name}!!! In an unlikely turn of events!"
                    )
                    opponent.defeat()
                    return True  # Indicate successful pin
                elif possibilities.count("opponent") >= 3:

                    for i in range(1, 3):
                        print(f"{i}...")
                    print(f"{opponent.name} kicks out!!")
                    self.stamina_level -= 40

            else:
                possibilities = random.choices(chance, k=3)
                if possibilities.count("self") >= 1:
                    for i in range(1, 4):
                        print(f"{i}...")
                    print(f"{self.name} wins with a quick pin!!!")
                    opponent.defeat()
                    return True  # Indicate successful pin
                else:
                    print(f"1...")
                    print(f"{opponent.name} quickly kicks out")

        if self.stamina_level < 0:
            self.stamina_level = 0
        return False  # Indicate unsuccessful pin

    def defeat(self) -> bool:
        self.is_defeated = True
        return self.is_defeated

    def reset(self) -> bool:
        self.is_defeated = False
        return self.is_defeated

    def chooseAction(self, opponent: "Wrestler") -> None:
        func_list = [self.attack, self.grappleOpponent, self.pinOpponent]
        if opponent.health <= (opponent.max_health // 2):
            # Opponent is at half health or below - more aggressive tactics
            weights = [0.4, 0.7, 1.5]
            ans = random.choices(func_list, weights=weights, k=1)[0]
        else:
            # Opponent is above half health - more conservative tactics
            weights = [1.9, 1.5, 0.3]
            ans = random.choices(func_list, weights=weights, k=1)[0]
        ans(opponent)

   


    @classmethod
    def compare_wrestlers(val,wrestler1, wrestler2)->str:
        wres_properties=["strength","speed", "agility", "health","power", "grapple","stamina" ]
        border=len(wrestler1.name+wrestler2.name)
        print(f' {"--"*border}')
        print(f"| Stat       | {wrestler1.name} | {wrestler2.name}| ")
        print(f' {"--"*border}')
        
        for prop in  vars(wrestler1):
            if prop in wres_properties:
                print(f"|  "+prop+((10-len(prop))*" ")+"|",end="")
                wres1_attrib=getattr(wrestler1,prop)
                wres2_attrib=getattr(wrestler2,prop)
                if type(wres1_attrib) == int and type(wres2_attrib)==int:
                    if wres1_attrib>wres2_attrib:
                        wres1_attrib=highlight(wres1_attrib)
                        wres2_attrib="    "+str(wres2_attrib)
                    elif wres2_attrib>wres1_attrib:
                        wres2_attrib=highlight(wres2_attrib)
                        wres1_attrib="    "+str(wres1_attrib)
                    else:
                        wres1_attrib="    "+str(wres1_attrib)
                        wres2_attrib="    "+str(wres2_attrib)
                    print(f"{wres1_attrib}{(((len(wrestler1.name))+1)-len(str(wres1_attrib)))*" "}|{wres2_attrib}{((len(wrestler2.name)+1)-len(str(wres2_attrib)))*" "}",sep="|",end="|\n")
                    
        print(f' {"--"*border}')
        print(f"|  Overall   |  {wrestler1.get_overall_rating()}{(((len(wrestler1.name))+1)-len(str(wres1_attrib)))*" "}|  {wrestler2.get_overall_rating()}{((len(wrestler2.name)-1)-len(str(wrestler2.get_overall_rating())))*" "}",end="|\n")
                 
        print(f' {"--"*border}')
    def display_stats_table(self) -> None:
        """
        Display this wrestler's stats in a formatted table for the CLI.
        Prints name, gender, core attributes, and overall rating.
        """
        stats = [
            ("Strength", self.strength),
            ("Speed", self.speed),
            ("Agility", self.agility),
            ("Health", self.health),
            ("Power", self.power),
            ("Grapple", self.grapple),
            ("Stamina", self.stamina),
        ]

        name_len = len(self.name)
        col_width = max(10, name_len + 2)
        border = "-" * (col_width + 16)

        print(border)
        print(f"| Wrestler: {self.name:<{col_width}} | Gender: {self.gender:<7} |")
        print(border)
        print(f"| {'Stat':<10} | {'Value':<6} |")
        print(border)

        for stat, value in stats:
            print(f"| {stat:<10} | {value:<6} |")

        print(border)
        overall = round(self.get_overall_rating(), 2)
        print(f"| {'Overall':<10} | {overall:<6} |")
        print(border)

def highlight(data):
    return f"\033[47m    {data}   \033[00m"

