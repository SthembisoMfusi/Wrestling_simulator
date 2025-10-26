from ...core.wrestler import Wrestler
from ...core.tournament import Tournament
from typing import Any
from create_all_rosters import load_wrestler_names_from_file, create_wrestler_data
import os
import json
from ...utils.file_utils import get_data_path, load_wrestler_names
from ...core.roster import Roster
import random as rdm
import os
import sys



class Wrestlers_Interactive:
    def __init__(self) -> None:
        self.players: list[Wrestler] = []
        self.bots: list[Wrestler] = []
        self.current_bot:Wrestler 
        self.current:Wrestler 

    def interactive_main(self) -> None:
        print("-" * 20)
        print("    Pick a Player")
        print("-" * 20)

        if not os.path.exists("game_data.json"):
            print("Available Players not found \nGenerating Players")
            self.generate_default_wrestlers()
        ply = self.load_players()
        self.display(ply)
        if (select := self.selection(ply)) != None:
            self.players = [ply[i - 1] for i in select]
            for selected in self.players:
                ply.remove(selected) 
            self.bots = [rdm.choice(ply) for i in range(len(self.players))]
            self.game_loop()

    def selection(self, plyrs: list[Wrestler]) -> list[int] | None:
        commands = {
            "pick": ["pick 3", "pick 1,2,4"],
            "view": ["view 3"],
            "compare": ["e.g compare 1,2"],
            "help": ["help prints this command"],
            "exit": ["exits the game"],
        }

        valid = False
        while not valid:
            req = input("\nselect => ").lower()
            self.display(plyrs)
            icmd = req.split(" ")[0]
            while icmd not in commands:
                print("invalid Usage please see help ")
                req = input("\nselect => ").lower()
                icmd = req.split(" ")[0]

            match icmd:
                case "pick":
                    try:
                        dirty_selection = req.split(" ")[1:][0]
                        values:list[Any] = dirty_selection.split(",")
                        values = [int(i) for i in values]
                        return values
                    except (IndexError, ValueError):
                        print("please refer to help command")

                case "view":
                    try:
                        val = int(req.split(" ")[1])
                        plyrs[val - 1].display_stats_table()
                    except (IndexError, ValueError):
                        print("please refer to help command")

                case "compare":
                    dirty_selection = req.split(" ")[1:][0]
                    values = dirty_selection.split(",")
                    if len(values) == 2:
                        values = [int(i) for i in values]
                        data = Wrestler.compare_wrestlers(
                            plyrs[values[0] - 1], plyrs[values[1] - 1]
                        )
                        print(data)
                    else:
                        print("invalid command usage please refer to help command")

                case "help":
                    for cmd in commands:
                        print(f"{cmd}        {', '.join(commands[cmd])}")
                case "exit":
                    sys.exit(0)
        return None

    def display(self, ply:list[Wrestler])->None:
        width = 10
        for i, p in enumerate(ply[:52]):
            print(f"[{i + 1}] {p}  {(width - len(p.name)) * ' '} ", end="\t\t")
            if (i + 1) % 4 == 0:
                print(" ")

    def generate_default_wrestlers(self) -> None:
        data = ("male", "female", "other")
        wres_types = [
            "balanced",
            "strength",
            "powerhouse",
            "speedster",
            "technician",
            "veteran",
            "rookie",
        ]
        players = []

        for group in data:
            names = load_wrestler_names(group)
            for player in names:
                players.append(
                    create_wrestler_data(player, group, rdm.choice(wres_types))
                )
        with open("game_data.json", "w") as file:
            json.dump(players, file, indent=4)

    def load_players(self) -> list[Wrestler]:
        list_of_availble_ply: list[Wrestler] = []
        with open("game_data.json", "r") as file:
            data = json.load(file)
            for p in data:
                list_of_availble_ply.append(Wrestler.load_from_Dict(p))

        return list_of_availble_ply

    def game_loop(self) -> None:
        print("\nAnd the match starts")

        self.current = self.players[0]
        self.current_bot = self.bots[0]

        Tournament.match(
             self.current, self.current_bot, self.player_action, False
        )

    def player_action(self) -> Wrestler:
        ingame_command = {
            "grapple": ["grapples current opponent"],
            "attack": ["attacks current opponent"],
            "pin": ["pins current opponent"],
            "defend": ["defends and heals health"],
            "stats": ["view current players strength"],
            "help": ["prints this help "],
            "compare": ["compare two given players"],
            "tag": ["tags in teamate\n[e.g] tag \n[e.g] tag 4"],
            "exit": ["quits the current game"],
        }
        while True:
            while (mov := input("its your turn =>").lower()) not in ingame_command:
                print("invalid action please refer to help command")

            match mov:
                case "attack":
                    self.current.attack(self.current_bot)
                    return self.current

                case "grapple":
                    self.current.grappleOpponent(self.current_bot)
                    return self.current

                case "defend":
                    return self.current

                case "pin":
                    self.current.pinOpponent(self.current_bot)
                    return self.current

                case "help":
                    for cmd in ingame_command:
                        print(f"{cmd}        {', '.join(ingame_command[cmd])}")

                case "stats":
                    self.current.display_stats_table()

                case "compare":
                    dirty_selection = mov.split(" ")[1:][0]
                    values:list[Any] = dirty_selection.split(",")
                    if len(values) == 2:
                        values = [int(i) for i in values]
                        data = Wrestler.compare_wrestlers(
                            self.players[values[0]], self.players[values[1]]
                        )
                        print(data)
                    else:
                        print("invalid command usage please refer to help command")

                case "tag":
                    bench_players = [
                        p
                        for i, p in enumerate(self.players)
                        if p.name != self.current.name
                    ]
                    if len(bench_players) == 0:
                        print("no one To tag")
                    else:
                        [print(f"[{i + 1}] {p}") for i, p in enumerate(bench_players)]

                    try:
                        index = int(input("tag =>"))
                        self.current = bench_players[index - 1]

                        print(f"{self.current.name} was tagged in")
                    except:
                        print("invalid Input please refer to help command")

                    # while (int(input("tag => "))>len(players))

                case "exit":
                    print("quiting the game")
                    sys.exit(0)


if __name__ == "__main__":
    Wrestlers_Interactive().interactive_main()
