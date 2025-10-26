"""
Roster class for the wrestling simulator.

This module contains the Roster class which manages a collection of wrestlers,
handles creation, loading, saving, and manipulation of wrestler rosters.
"""

import random
import pickle
import os
from typing import List, Union, Optional
from .wrestler import Wrestler
from ..utils.file_utils import load_wrestler_names
from ..constants import VALID_GENDERS, PICKLE_EXTENSION


class Roster:
    def __init__(
        self,
        contestants: Optional[int] = None,
        file: Optional[str] = None,
        auto_fill: bool = True,
    ) -> None:
        self.contestants = contestants
        self.roster: List[Wrestler] = []
        self.file = file
        if contestants is None and file is not None:
            self.load_roster(file)
        elif contestants is not None and file is None and auto_fill:
            self.fillRoster()

    def autoCreate(self, sex: str) -> Wrestler:
        """
        Automatically assigns values for a new wrestler object.

        Args:
            sex (str): Used to determine which gender to use and which name file to select from.

        Returns:
            Wrestler: A wrestler object with its stats.
        """
        if sex.lower() not in VALID_GENDERS:
            raise ValueError(
                f"Invalid gender: '{sex}'. Gender must be one of {VALID_GENDERS}. "
                f"Please use 'male', 'female', or 'other'."
            )

        gender = sex.lower()
        names = load_wrestler_names(gender)

        name = random.choice(names)
        strength = random.randint(40, 100)
        speed = random.randint(30, 100)
        agility = random.randint(10, 100)
        health = random.randint(80, 200)
        power = random.randint(50, 100)
        grapple = random.randint(1, 20)
        stamina = random.randint(30, 100)

        new = Wrestler(
            name, gender, strength, speed, agility, health, power, grapple, stamina
        )
        return new

    def manualCreate(self, sex: Optional[str] = None) -> Wrestler:
        """
        Manually assigns values for a new wrestler object.

        Args:
            sex(str): the gender of the wrestler object to be created

        Returns:
            Wrestler: A wrestler object with its stats.
        """
        if sex is not None:
            while True:
                sex = sex.lower()
                if sex not in VALID_GENDERS:
                    print(f"gender must be one of {VALID_GENDERS}")
                    sex = input("please enter the wrestler's gender: ")
                else:
                    break
        else:
            while True:
                sex = input(
                    f"enter the wrestler's gender ({', '.join(VALID_GENDERS)}):"
                ).lower()
                if sex not in VALID_GENDERS:
                    print(f"gender must be one of {VALID_GENDERS}")
                else:
                    break

        name = input("enter the wrestler's name:").strip()

        while True:
            try:
                strength = int(input("enter the wrestler's strength(min:40,max:100):"))
                if strength < 40 or strength > 100:
                    raise ValueError
                break
            except ValueError:
                print(
                    "❌ Invalid strength! Please enter a number between 40-100 (e.g., 70 or 85)."
                )
        while True:
            try:
                speed = int(input("enter the wrestler's speed(min:30,max:100):"))
                if speed < 30 or speed > 100:
                    raise ValueError
                break
            except ValueError:
                print(
                    "❌ Invalid speed! Please enter a number between 30-100 (e.g., 65 or 80)."
                )
        while True:
            try:
                agility = int(input("enter the wrestler's agility(min:10,max:100):"))
                if agility < 10 or agility > 100:
                    raise ValueError
                break
            except ValueError:
                print(
                    "❌ Invalid agility! Please enter a number between 10-100 (e.g., 50 or 75)."
                )

        while True:
            try:
                health = int(input("enter the wrestler's health(min:80,max:200):"))
                if health < 80 or health > 200:
                    raise ValueError
                break
            except ValueError:
                print(
                    "❌ Invalid health! Please enter a number between 80-200 (e.g., 120 or 160)."
                )

        while True:
            try:
                power = int(input("enter the wrestler's power(min:50,max:100):"))
                if power < 50 or power > 100:
                    raise ValueError
                break
            except ValueError:
                print(
                    "❌ Invalid power! Please enter a number between 50-100 (e.g., 75 or 90)."
                )

        while True:
            try:
                grapple = int(input("enter the wrestler's grapple(min:1,max:20):"))
                if grapple < 1 or grapple > 20:
                    raise ValueError
                break
            except ValueError:
                print(
                    "❌ Invalid grapple! Please enter a number between 1-20 (e.g., 10 or 15)."
                )
        while True:
            try:
                stamina = int(input("enter the wrestler's stamina(min:30,max:100):"))
                if stamina < 30 or stamina > 100:
                    raise ValueError
                break
            except ValueError:
                print(
                    "❌ Invalid stamina! Please enter a number between 30-100 (e.g., 60 or 80)."
                )

        new = Wrestler(
            name, sex, strength, speed, agility, health, power, grapple, stamina
        )
        return new

    def fillRoster(self) -> None:
        """
        Fills the roster with wrestlers, either manually, automatically, or both.
        """
        while True:
            auto = input(
                "Do you want to fill the roster manually, automatically, or both? [manually/automatically/both]: "
            ).lower()
            if auto not in [
                "manually",
                "automatically",
                "both",
                "m",
                "a",
                "auto",
                "man",
            ]:
                print("invalid choice")
            else:
                break
        if auto in ["manually", "m", "man"]:
            if self.contestants is not None:
                for _ in range(self.contestants):
                    player = self.manualCreate()
                    self.roster.append(player)
        elif auto in ["automatically", "auto", "a"]:
            while True:
                sex = input(
                    "please enter the gender of the roster['male'/'female'/'other']:"
                )
                if sex not in ["male", "female", "other"]:
                    print("invalid input")
                else:
                    break
            if self.contestants is not None:
                for _ in range(self.contestants):
                    player = self.autoCreate(sex)
                    self.roster.append(player)
        elif auto == "both":
            if self.contestants is not None:
                for _ in range(self.contestants):
                    while True:
                        choice = input(
                            "automatic or manual entry?[automatic/manual]:"
                        ).lower()
                        if choice not in ["automatic", "manual", "a", "m"]:
                            print("invalid input")
                        else:
                            break
                    if choice in ["automatic", "a"]:
                        while True:
                            sex = input(
                                "please enter the gender of the roster['male'/'female'/'other]:"
                            )
                            if sex not in ["male", "female", "other"]:
                                print("invalid input")
                            else:
                                break
                        player = self.autoCreate(sex)
                        self.roster.append(player)
                    elif choice in ["manual", "m"]:
                        player = self.manualCreate()
                        self.roster.append(player)

    def remove_wrestler(self, identifier: Union[int, str]) -> None:
        """
        Removes a wrestler from the roster.

        Args:
            identifier: Either the index (int) of the wrestler or the name (str) of the wrestler.
        """
        if isinstance(identifier, int):
            # Remove by index
            if 0 <= identifier < len(self.roster):
                del self.roster[identifier]
            else:
                raise ValueError(
                    f"Invalid wrestler index: {identifier}. "
                    f"Please use an index between 0 and {len(self.roster) - 1}. "
                    f"The roster currently has {len(self.roster)} wrestler(s)."
                )
        elif isinstance(identifier, str):
            # Remove by name
            for i, wrestler in enumerate(self.roster):
                if wrestler.name == identifier:
                    del self.roster[i]
                    return
            raise ValueError(
                f"Wrestler '{identifier}' not found in roster. "
                f"Check the spelling or use list_wrestlers() to see all available wrestlers."
            )
        else:
            raise TypeError("Identifier must be an integer (index) or a string (name).")

    def get_wrestler(self, identifier: Union[int, str]) -> Wrestler:
        """
        Gets a wrestler from the roster.

        Args:
            identifier: Either the index (int) of the wrestler or the name (str) of the wrestler.

        Returns:
            Wrestler: The wrestler object.
        """
        if isinstance(identifier, int):
            # Get by index
            if 0 <= identifier < len(self.roster):
                wrestler = self.roster[identifier]
                return wrestler
            else:
                raise ValueError(
                    f"Invalid wrestler index: {identifier}. "
                    f"Please use an index between 0 and {len(self.roster) - 1}. "
                    f"The roster currently has {len(self.roster)} wrestler(s)."
                )
        elif isinstance(identifier, str):
            # Get by name
            for wrestler in self.roster:
                if wrestler.name == identifier:
                    return wrestler
            raise ValueError(
                f"Wrestler '{identifier}' not found in roster. "
                f"Check the spelling or use list_wrestlers() to see all available wrestlers."
            )
        else:
            raise TypeError("Identifier must be an integer (index) or a string (name).")

    def save_roster(self, filename: str) -> None:
        """
        Saves the roster to a file using pickle.

        Args:
            filename (str): The name of the file to save to.
        """
        # If no directory specified, save to rosters folder
        if "/" not in filename and "\\" not in filename:
            rosters_dir = "rosters"
            if not os.path.exists(rosters_dir):
                os.makedirs(rosters_dir)
            filename = os.path.join(rosters_dir, filename)

        with open(filename, "wb") as f:
            pickle.dump(self.roster, f)

    def load_roster(self, filename: str) -> None:
        """
        Loads the roster from a file using pickle.

        Args:
            filename (str): The name of the file to load from.
        """
        with open(filename, "rb") as f:
            self.roster = pickle.load(f)

    @staticmethod
    def list_available_rosters() -> list[tuple[str, int]]:
        """
        List all available roster files in the rosters directory with wrestler counts.

        Returns:
            List of tuples containing (filename, wrestler_count)
        """
        rosters_dir = "rosters"
        if not os.path.exists(rosters_dir):
            os.makedirs(rosters_dir)
            return []

        roster_files = [
            f for f in os.listdir(rosters_dir) if f.endswith(PICKLE_EXTENSION)
        ]
        roster_info = []

        for roster_file in sorted(roster_files):
            try:
                file_path = os.path.join(rosters_dir, roster_file)
                with open(file_path, "rb") as f:
                    roster_data = pickle.load(f)
                    wrestler_count = (
                        len(roster_data) if isinstance(roster_data, list) else 0
                    )
                    roster_info.append((roster_file, wrestler_count))
            except (pickle.PickleError, FileNotFoundError, EOFError):
                roster_info.append((roster_file, 0))

        return roster_info

    @classmethod
    def from_names(cls, names: list[str], wrestler_type: str, gender: str) -> "Roster":
        """
        Create a Roster from a list of names, assigning the same type and gender.

        Args:
            names: List of wrestler names
            wrestler_type: Type for all wrestlers
            gender: Gender for all wrestlers

        Returns:
            Roster object
        """
        roster = cls(auto_fill=False)
        for name in names:
            # We'll assume Wrestler can take 'type' as a stat if relevant
            strength = random.randint(40, 100)
            speed = random.randint(30, 100)
            agility = random.randint(10, 100)
            health = random.randint
