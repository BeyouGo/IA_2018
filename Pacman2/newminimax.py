# Complete this class for all parts of the project
import sys

from pacman_module.game import Agent, random, Directions
from pacman_module.pacman import GameState
from pacman_module import util

numOfExpandedStates = 0


# totExpandedStates=0
# sys.setrecursionlimit(1000)
class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.pacmanIndex = 0
        self.ghostIndex = 1

        self.agentCount = 2
        self.depth = 3

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
        # trueDepth = self.agentCount * self.depth

        # Get first pacman successors
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]

        v = [self.value(nextGameState, 1) for nextGameState in succs]

        maxV = max(v)
        index = v.index(maxV)
        return moves[index]

    def value(self, gameState, agentIndex):


        if gameState.isLose() or gameState.isWin():
            return gameState.getScore()

        if agentIndex == 0:
            return self.max_value(gameState)

        if agentIndex > 0:
            return self.min_value(gameState, agentIndex)

    def max_value(self, gameState):
        v = -1e80

        succsDirectionPair = gameState.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        v = max([self.value(succ, 1) for succ in succs])
        return v

    def min_value(self, gameState, agentIndex):
        v = 1e80
        succsDirectionPair = gameState.generateGhostSuccessors(agentIndex)
        succs = [succ[0] for succ in succsDirectionPair]
        v = min([self.value(succ, 0) for succ in succs])
        return v


