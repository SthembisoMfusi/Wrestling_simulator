from ...core.wrestler import Wrestler
from ...core.tournament import Tournament
from create_all_rosters import load_wrestler_names_from_file,create_wrestler_data
import os
import json
from ...utils.file_utils import get_data_path,load_wrestler_names
import random as rdm
import os 
import sys

def interactive_main():
    print("-"*20)
    print("    Pick a Player")
    print("-"*20)
  
    if not os.path.exists("game_data.json"):
        print("Available Players not found \nGenerating Players")
        generate_default_wrestlers()
    ply=load_players()
    display(ply)
    selected_players :list[Wrestler]=[ply[i-1] for i in selection(ply)]
    game_loop(selected_players)
    
def selection(plyrs):
    commands={
        "pick":["pick 3","pick 1,2,4"],
        "view":["view 3"],
        "help":["help prints this command"],
        "exit":["exits the game"]
        }
   
  
    valid=False
    while not valid:
       
        req=input("\nselect => ").lower()
        display(plyrs)
        icmd=req.split(" ")[0]
        while icmd not in commands:

            print("invalid Usage please see help ")
            req=input("\nselect => ").lower()
            icmd=req.split(" ")[0]
        
        match icmd:
            case "pick":
                try:
                    dirty_selection=req.split(" ")[1:][0]
                    values=dirty_selection.split(",")
                    values=[int(i) for i in values]
                    return values
                except (IndexError,ValueError):
                    print("please refer to help command")
            
            case "view":
                try:
                    val=int(req.split(" ")[1])
                    print(plyrs[val-1].showStats())
                except (IndexError,ValueError):
                    print("please refer to help command")
            
            
            case "help":
                for cmd in commands:
                    print(f"{cmd}        {", ".join(commands[cmd])}")
            case "exit":
                sys.exit(0)

def display(ply):
    width=10
    for i,p in enumerate(ply[:52]):
        print(f"[{i+1}] {p}  {((width-len(p.name)))*" "} ",end="\t\t")
        if (i+1)%4==0:
            print(" ")
            
def generate_default_wrestlers()->None:

    data=("male","female","other")
    wres_types=["balanced","strength","powerhouse","speedster",
                "technician","veteran","rookie"]
    players=[]

    for group in data:
        names=load_wrestler_names(group)
        for player in names:
            players.append(create_wrestler_data(player,group,rdm.choice(wres_types)))
    with open ("game_data.json","w") as file:
        json.dump(players,file,indent=4)
   
def load_players()->list[Wrestler]:
    list_of_availble_ply:list[Wrestler]=[]
    with open("game_data.json","r") as file:
        data=json.load(file)
        for p in data:
            list_of_availble_ply.append(Wrestler.load_from_Dict(p))

    return list_of_availble_ply

def game_loop(players:list[Wrestler]):
    print("\nAnd the match starts")
    ingame_command=["grapple","attack","pin","defend","stats","tag","exit"]
    in_match=True
    current=players[0]

    while in_match:
        while (mov:=input("its your turn =>")) not in ingame_command:
            print("invalid action please refer to help command")
        
        match mov:
            case "attack":
                print("attacked")

            case "grapple":
                print("grapple")

            case "defend":
                print("defend")

            case "pin":
                print("pin")

            case "stats":
                print(current.showStats())

            case "tag":
                [print(f"[{i}] {p}") for i,p in enumerate(players) if p.name != current.name]
                while thrp(int(input("tag => "))>len(players))

            case "exit":
                print("quiting the game")
                sys.exit(0)

            


if __name__=="__main__":
    interactive_main()