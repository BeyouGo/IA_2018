# Complete this class for all parts of the project
import sys

from pacman_module.game import Agent, random, Directions
from pacman_module.pacman import GameState
from pacman_module import util


# totExpandedStates=0
# sys.setrecursionlimit(1000)
class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        # self.args = args
        # self.pacmanIndex = 0
        # self.ghostIndex = 1
        #
        # self.agentCount = 2
        # self.depth = 3

        self.seen = []

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
        self.seen = []


        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]

        v = [self.value(nextGameState, 1, -1e80, 1e80) for nextGameState in succs]

        maxV = max(v)
        index = v.index(maxV)

        return moves[index]

    def value(self, gameState, agentIndex, alpha, beta):


        if self.already_seen_state(gameState,agentIndex):
            if agentIndex == 0:
                return -1e80
            else:
                return 1e80

        self.add_seen_state(gameState,agentIndex)

        if gameState.isLose() or gameState.isWin():
            # return self.scoreEvaluationFunction(gameState)
            return gameState.getScore()

        if agentIndex == 0:
            return self.max_value(gameState, alpha, beta)

        if agentIndex > 0:
            return self.min_value(gameState, agentIndex, alpha, beta)

    def max_value(self, gameState, alpha, beta):
        v = -1e80
        succsDirectionPair = gameState.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        for succ in succs:
            v=max([self.value(succ, 1, alpha, beta)])
            if v>=beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, gameState, agentIndex, alpha, beta):
        v = 1e80
        succsDirectionPair = gameState.generateGhostSuccessors(agentIndex)
        succs = [succ[0] for succ in succsDirectionPair]
        for succ in succs:
            v=min([self.value(succ, 0, alpha, beta)])
            if v<=alpha:
                return v
            beta=min(beta, v)
        return v

    def add_seen_state(self, game_state,agent_index):
        print((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],agent_index))
        self.seen.append((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],agent_index))

    def already_seen_state(self, game_state,agent_index):
        # print("Enter Already Seen State :")
        if (self.seen.count(
                (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],agent_index)) > 0):
            # print("\t" + str((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0])))
            # print("already seen ")
            return True
        else:
            return False

    def scoreEvaluationFunction(self, currentGameState):

        foodlist = currentGameState.getFood().asList()
        pos = currentGameState.getPacmanPosition()
        numfood = currentGameState.getNumFood()

        nearfooddist = 0
        if [util.manhattanDistance(pos, xy2) for xy2 in foodlist]:
            list = [util.manhattanDistance(currentGameState.getPacmanPosition(), xy2) for xy2 in foodlist]
            nearfooddist = min(list)

        posghost = currentGameState.getGhostPosition(1)
        if util.manhattanDistance(pos, posghost) == 0:
            distghost = -99
        else:
            distghost = util.manhattanDistance(pos, posghost)

        evfun = - nearfooddist * 1.5 - numfood * 10
        return evfun