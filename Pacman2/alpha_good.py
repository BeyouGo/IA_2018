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
        self.pacmanIndex = 0
        self.ghostIndex = 1
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
        # Get first pacman successors
        self.seen = []
        self.add_seen_state(s,0)
        ## simulate pacman turn
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]
        # Compute value for each of the pacman moves
        v = [self.min_value(succ, 1, -1e80, 1e80) for succ in succs]
        # return best one
        maxV = max(v)
        #print(str(moves) + " - " + str(v) + " <-> " + str(maxV))
        index = v.index(maxV)
        return moves[index]

    def max_value(self, game_state, agent_index, alpha, beta):
        # print("enter to max")
        if game_state.isLose() or game_state.isWin():
            return self.scoreEvaluationFunction(game_state)
        if self.already_seen_state(game_state, agent_index):
            if agent_index == self.pacmanIndex:
                return -1e80
            else:
                return 1e80
        v = - 1e80
        self.add_seen_state(game_state, agent_index)
        for (succ, move) in game_state.generatePacmanSuccessors():
            v = max((self.min_value(succ, (agent_index + 1) % 2, alpha, beta), v))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        #print("Max with agent " + str(agent_index)+ " <-> "+str(v))
        return v

    def min_value(self, game_state, agent_index, alpha, beta):
        # print("enter to min")
        if game_state.isLose() or game_state.isWin():
            return self.scoreEvaluationFunction(game_state)
        if self.already_seen_state(game_state, agent_index):
            if agent_index == self.pacmanIndex:
                return -1e80
            else:
                return 1e80
        v = 1e80
        self.add_seen_state(game_state, agent_index)
        for (succ, move) in game_state.generateGhostSuccessors(1):
            v = min(self.max_value(succ, (agent_index + 1) % 2, alpha, beta), v)
            if v <= alpha:
                return v
            beta = min(beta, v)
        #print("Min with agent " + str(agent_index) + " <-> "+str(v))
        return v

    def add_seen_state(self, game_state, agent_index):
        # print((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],agent_index))
        self.seen.append(
            (game_state.getFood(), game_state.getPacmanPosition(), game_state.getGhostPositions()[0],
                 agent_index))

    def already_seen_state(self, game_state, agent_index):
        # print("Enter Already Seen State :", game_state)
        if (self.seen.count(
                (game_state.getFood(), game_state.getPacmanPosition(), game_state.getGhostPositions()[0],
                 agent_index)) > 0):
            # print("\t" + str((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0])))
            # print("already seen ")
            return True
        else:
            return False

    def scoreEvaluationFunction(self, current_game_state):
        foodlist = current_game_state.getFood().asList()
        pos = current_game_state.getPacmanPosition()
        numfood = current_game_state.getNumFood()

        nearfooddist = 0
        if [util.manhattanDistance(pos, xy2) for xy2 in foodlist]:
            foodlist = [util.manhattanDistance(current_game_state.getPacmanPosition(), xy2) for xy2 in foodlist]
            nearfooddist = min(foodlist)

        posghost = current_game_state.getGhostPosition(1)
        distghost = 0
        if util.manhattanDistance(pos, posghost) == 0:
            distghost = 1e80
        else:
             distghost = util.manhattanDistance(pos, posghost)

        evfun =  - numfood * 10 - nearfooddist * 2  + current_game_state.getScore() - (distghost)
        # evfun = self.heuristic(current_game_state)
        return evfun
