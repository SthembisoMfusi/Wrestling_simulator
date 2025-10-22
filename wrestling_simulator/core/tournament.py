"""
Tournament class for the wrestling simulator.

This module contains the Tournament class which handles tournament creation,
match simulation, and winner determination.
"""

import random
import time
from typing import List, Tuple, Optional
from .roster import Roster
from .wrestler import Wrestler
from ..utils.validation import validate_tournament_size


class Tournament:
    def __init__(self, roster: Roster, participants: int) -> None:
        self.participants = participants
        validate_tournament_size(participants)
        self.roster = roster
        self.wrestlers: List[Wrestler] = []
        self.tournamentRoster()
        self.tournamentPool = self.createTournamentPool(self.wrestlers)
        self.round = 1

    def tournamentRoster(self) -> None:
        """Generates the roster from the tournament
        Args:
            roster(object): a list containing a roster of wrestlers where the participants will be picked
            from
        Returns:
                playing_roster(list): the list of wrestlers participating in the tournament
        """
        playing_roster: List[Wrestler] = []
        while len(playing_roster) != self.participants:
            player = random.choice(self.roster.roster)
            if player not in playing_roster:
                playing_roster.append(player)
        self.wrestlers = playing_roster

    def createTournamentPool(
        self, pool: List[Wrestler]
    ) -> List[Tuple[Wrestler, Wrestler]]:
        """pools the tournament participants
        Args:
            pool(list): a list containing wrestlers that are in the tournament
        Returns:
                main_pool(list): a list containing tuples of the competitors and their opponents
        """
        random.shuffle(pool)  # Shuffle the pool for random pairings
        wrestler_count = int(len(pool) / 2)
        pool1 = pool[:wrestler_count]
        pool2 = pool[wrestler_count:]
        main_pool = []
        for i in range(len(pool1)):
            main_pool.append((pool1[i], pool2[i]))
        return main_pool

    def match(self, player1: Wrestler, player2: Wrestler) -> Wrestler:
        """creates the match simulation for the wrestlers
        they will start using their assortment of actions to try and encapacitate and defeat
        their opponent
            Args:
                player1(object): the first wrestler
                player2(object): the second wrestlers
            Returns:
                    winner(object): returns the winner of the fight

        """
        state = True
        print(f"It's {player1.name} vs {player2.name}!!!")
        time.sleep(2)  # Give user time to see the match announcement
        player1.reset()
        player2.reset()
        while state:
            player1.chooseAction(player2)
            time.sleep(1.5)  # Delay after each action to let user read it
            if player2.is_defeated:
                state = False
                time.sleep(2)  # Delay after match ends to see winner
                return player1
            player2.chooseAction(player1)
            time.sleep(1.5)  # Delay after each action to let user read it
            if player1.is_defeated:
                state = False
                time.sleep(2)  # Delay after match ends to see winner
                return player2
            player1.staminaRegen()
            player2.staminaRegen()
            player1.healthRegen()
            player2.healthRegen()

        # This should never be reached due to the logic above, but mypy needs a return
        raise RuntimeError("Match ended without a winner")

    def Round(self) -> None:
        print(f"------ Round {self.round} ------")
        time.sleep(1.5)  # Give user time to see round announcement
        winners = []
        for fighter1, fighter2 in self.tournamentPool:
            winner = self.match(fighter1, fighter2)
            winners.append(winner)
            print()  # Add blank line between matches for clarity
            time.sleep(1)  # Brief pause between matches in the same round
        self.round += 1
        if len(winners) > 1:
            self.tournamentPool = self.createTournamentPool(
                winners
            )  # Create new pairings for next round
        if len(self.tournamentPool) == 1:
            grand_champ = self.match(
                self.tournamentPool[0][0], self.tournamentPool[0][1]
            )
            print(f"\n***** The Tournament Winner is:{grand_champ.name} *****")
            time.sleep(3)  # Give user time to see the tournament winner

    def tournamentPlay(self) -> None:
        while len(self.tournamentPool) > 1:
            self.Round()
