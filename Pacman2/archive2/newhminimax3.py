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
        self.depth = 5

        self.seen = []
        self.seenGlobal = []

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



        v = [self.value(nextGameState, 1, self.depth) for nextGameState in succs]


        maxV = max(v)
        print(maxV)
        index = v.index(maxV)

        return moves[index]

    def value(self, gameState, agentIndex, depth):

        if gameState.isLose() or gameState.isWin() or depth == 0:
            return self.scoreEvaluationFunction(gameState)
            # return gameState.getScore()

        if self.already_seen_state(gameState, agentIndex, depth):
            if agentIndex == 0:
                return 1e80
            else:
                return -1e80

        self.add_seen_state(gameState, agentIndex, depth)

        if agentIndex == 0:
            return self.max_value(gameState, agentIndex, depth - 1)

        if agentIndex > 0:
            return self.min_value(gameState, agentIndex, depth - 1)

    def max_value(self, game_state, agent_index, depth):
        # print("enter to max")

        succs_direction_pair = game_state.generatePacmanSuccessors()
        succs = [succ[0] for succ in succs_direction_pair]

        v = max([self.value(succ, 1, depth) for succ in succs])

        # print("Max with agent " + str(agent_index) + " <-> " + str(v))
        return v

    def min_value(self, game_state, agent_index, depth):
        # print("enter to min")

        succs_direction_pair = game_state.generateGhostSuccessors(1)
        # print(succs_direction_pair)
        succs = [succ[0] for succ in succs_direction_pair]

        v = min([self.value(succ, 0, depth) for succ in succs])

        # print("Min with agent " + str(agent_index) + " <-> " + str(v))
        return v

    # def max_value(self, game_state, depth):
    #     # print("enter to max")
    #
    #
    #     succs_direction_pair = game_state.generatePacmanSuccessors()
    #     succs = [succ[0] for succ in succs_direction_pair]
    #
    #     v = max([self.value(succ, 1, depth) for succ in succs])
    #
    #     return v
    #
    # def min_value(self, game_state, agent_index, depth):
    #     # print("enter to min")
    #
    #
    #     succs_direction_pair = game_state.generateGhostSuccessors(agent_index)
    #     succs = [succ[0] for succ in succs_direction_pair]
    #
    #     v = min([self.value(succ, 0, depth) for succ in succs])
    #
    #     return v

    def add_seen_state(self, game_state, agent_index, depth):
        # print((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],agent_index))
        self.seen.append(
            (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0], agent_index,
             depth))

    def already_seen_state(self, game_state, agent_index, depth):
        # print("Enter Already Seen State :")
        return (self.seen.count(
            (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],
             agent_index, depth)) > 0)
        # print("\t" + str((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0])))
        # print("already seen ")

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
            distghost = 0.000000000001
        else:
            distghost = util.manhattanDistance(pos, posghost)
        print("dist" + str(2./distghost))

        evfun = - numfood * 4. - nearfooddist * 1.5 + current_game_state.getScore() - (2. / distghost)
        return evfun


        # def heuristic(self, state):
        #
        #     foods = []
        #     for i in range(0, state.getFood().width - 1):
        #         for j in range(0, state.getFood().height - 1):
        #             if state.getFood().data[i][j]:
        #                 foods.append((i, j))
        #
        #     node = state.getPacmanPosition()
        #     heuristic = 0
        #
        #     while foods:
        #         distance, food = min([(util.manhattanDistance(node, food), food) for food in foods])
        #         heuristic += distance
        #         node = food
        #         foods.remove(food)
        #
        #     return heuristic
