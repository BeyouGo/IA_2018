# Complete this class for all parts of the project
import sys

from pacman_module.game import Agent, random, Directions
from pacman_module.pacman import GameState
from pacman_module import util


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.pacmanIndex = 0
        self.ghostIndex = 1
        self.seen = []
        self.infinity = float("inf")

    def get_action(self, s):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """

        # Clear seen list and add current state to new seen list
        self.seen = []
        self.add_seen_state(s, 0)

        # Generate pacman successor
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]

        # Compute value for each of the pacman moves
        v = [self.min_value(succ) for succ in succs]

        # return best one
        maxV = max(v)
        index = v.index(maxV)
        return moves[index]

    def max_value(self, game_state):

        # Check if game ended or max depth occures
        if game_state.isLose() or game_state.isWin():
            return self.scoreEvaluationFunction(game_state)

        # Avoid loops
        if self.already_seen_state(game_state, self.pacmanIndex):
            return -self.infinity
        self.add_seen_state(game_state, self.pacmanIndex)

        # Apply minimax (Min)
        v = - self.infinity
        for (succ, move) in game_state.generatePacmanSuccessors():
            v = max((self.min_value(succ), v))

        return v

    def min_value(self, game_state):

        # Check if game ended or max depth occures
        if game_state.isLose() or game_state.isWin():
            return game_state.getScore()
            # return self.scoreEvaluationFunction(game_state)

        # Avoid loops
        if self.already_seen_state(game_state, self.ghostIndex):
            return self.infinity
        self.add_seen_state(game_state, self.ghostIndex)

        # Apply minimax (Max)
        v = self.infinity
        for (succ, move) in game_state.generateGhostSuccessors(1):
            v = min(self.max_value(succ), v)
        return v

    def add_seen_state(self, game_state, agent_index):
        self.seen.append(
            (game_state.getFood(), game_state.getPacmanPosition(), game_state.getGhostPositions()[0],
             agent_index))

    def already_seen_state(self, game_state, agent_index):
        return (self.seen.count(
            (game_state.getFood(), game_state.getPacmanPosition(), game_state.getGhostPositions()[0],
             agent_index)) > 0)
