from createRoster import Roster
from wrestler import Wrestler  # Added import for Wrestler
import random
import time

class Tournament:
    def __init__(self, roster: object, participants: int):
        self.participants = participants
        if self.participants % 2 != 0 or self.participants < 4 :
            raise ValueError("number of participants must be at least 4 eg. 4,8,16,32,etc.")
        self.roster = roster
        self.wrestlers = []
        self.tournamentRoster()
        self.tournamentPool = self.createTournamentPool(self.wrestlers)
        self.round = 1

    def tournamentRoster(self):
        '''Generates the roster from the tournament
            Args:
                roster(object): a list containing a roster of wrestlers where the participants will be picked
                from
            Returns:
                    playing_roster(list): the list of wrestlers participating in the tournament
        '''
        playing_roster = []
        while len(playing_roster) != self.participants:
            player = random.choice(self.roster.roster)
            if player not in playing_roster:
                playing_roster.append(player)
        self.wrestlers = playing_roster

    def createTournamentPool(self, pool):
        '''pools the tournament participants
            Args: 
                pool(list): a list containing wrestlers that are in the tournament
            Returns:
                    main_pool(list): a list containing tuples of the competitors and their opponents 
        '''
        random.shuffle(pool)  # Shuffle the pool for random pairings
        wrestler_count = int(len(pool) / 2)
        pool1 = pool[:wrestler_count]
        pool2 = pool[wrestler_count:]
        main_pool = []
        for i in range(len(pool1)):
            main_pool.append((pool1[i], pool2[i]))
        return main_pool

    def match(self, player1: object, player2: object):
        '''creates the match simulation for the wrestlers
        they will start using their assortment of actions to try and encapacitate and defeat
        their opponent
            Args:
                player1(object): the first wrestler
                player2(object): the second wrestlers
            Returns:
                    winner(object): returns the winner of the fight

                '''
        state = True
        print(f"It's {player1.name} vs {player2.name}!!!")
        player1.reset()
        player2.reset()
        while state:
            player1.chooseAction(player2)
            if player2.is_defeated:
                print(f"{player1.name} Wins!!!!")
                state = False
            
                return player1  
            player2.chooseAction(player1)
            if player1.is_defeated:
                print(f"{player2.name} Wins!!!")
              
                return player2  
            player1.staminaRegen()
            player2.staminaRegen()
            player1.healthRegen()
            player2.healthRegen()
            if player1.is_defeated:
                print(f"{player2.name} Wins!!!")
                state = False
              
                return player2 

            elif player2.is_defeated:
                print(f"{player1.name} Wins!!!!")
                state = False
               
                return player1 

    def Round(self):
        print(f"------ Round {self.round} ------")
        winners = []
        for fighter1, fighter2 in self.tournamentPool:
            winner = self.match(fighter1, fighter2)
            winners.append(winner)
        self.round += 1
        if len(winners) > 1:
            self.tournamentPool = self.createTournamentPool(winners) # Create new pairings for next round
        elif len(winners) == 0:
            print(f"\n***** The Tournament Winner is: {winners[0].name} *****")
            self.tournamentPool = winners
            return

wwe = Roster(40)
royal = Tournament(wwe, 8)

while len(royal.tournamentPool) != 1:  
    royal.Round()