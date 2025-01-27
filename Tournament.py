from createRoster import Roster
from wrestler import random
class Tournament:
    def __init__(self,roster:object,participants:int):
        self.participants = participants
        if self.participants % 4 != 0:
            raise ValueError("number of participants must be at least 4 eg. 4,8,16,32,etc.")
        self.roster = roster
        self.wrestlers = []
        self.tournamentRoster()
        self.tournamentPool = self.createTournamentPool(self.wrestlers)
        
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
    def createTournamentPool(self,pool):
        '''pools the tournament participants
            Args: 
                pool(list): a list containing wrestlers that are in the tournament
            Returns:
                    main_pool(list): a list containing tuples of the competitors and their opponents 
        '''
        wrestler_count = int(len(self.wrestlers)/2)
        pool1 = pool[:wrestler_count]
        pool2 = pool[wrestler_count:]
        main_pool = []
        for i in range(len(pool1)):
            main_pool.append((pool1[i], pool2[i]))
        return main_pool
    
wwe = Roster(40)
royal = Tournament(wwe,8)
print(royal.tournamentPool)
