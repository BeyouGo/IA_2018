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
        self.args = args
        self.pacmanIndex = 0
        self.ghostIndex = 1

        self.agentCount = 2
        self.depth = 3

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
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]

        v = [self.value(nextGameState, 0, 0) for nextGameState in succs]

        maxV = max(v)
        index = v.index(maxV)
        return moves[index]

    def value(self, gameState, agentIndex, depth):
        # print("enter to value")
        # print("Depth = " + str(depth))
        # print("Agent Index = " + str(agentIndex))
        # print("\n\n")




        if self.already_seen_state(gameState):
            if agentIndex == 0:
                return -1e80
            else:
                return 1e80

        self.add_seen_state(gameState)

        if gameState.isLose() or gameState.isWin():
            return gameState.getScore()

        if agentIndex == 0:
            return self.max_value(gameState, depth + 1)

        if agentIndex > 0:
            return self.min_value(gameState, agentIndex, depth + 1)

    def max_value(self, game_state, depth):
        # print("enter to max")


        succs_direction_pair = game_state.generatePacmanSuccessors()
        succs = [succ[0] for succ in succs_direction_pair]

        v = max([self.value(succ, 1, depth) for succ in succs])

        return v

    def min_value(self, game_state, agent_index, depth):
        # print("enter to min")


        succs_direction_pair = game_state.generateGhostSuccessors(agent_index)
        succs = [succ[0] for succ in succs_direction_pair]

        v = min([self.value(succ, 0, depth) for succ in succs])

        return v

    def add_seen_state(self, game_state):
        print((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0]))
        self.seen.append((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0]))

    def already_seen_state(self, game_state):
        # print("Enter Already Seen State :")
        if (self.seen.count(
                (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0])) > 0):
            # print("\t" + str((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0])))
            # print("already seen ")
            return True
        else:
            return False

# #
# #
# def max_value(self, game_state, depth):
#     # print("enter to max")
#     v = -1e80
#
#     succs_direction_pair = game_state.generatePacmanSuccessors()
#     succs = [succ[0] for succ in succs_direction_pair]
#
#     unseen_succs = []
#     for succ in succs:
#         if not self.already_seen_state(succ):
#             unseen_succs.append(succ)
#     # values = []
#
#     if (len(unseen_succs) > 0):
#         v = max([self.value(unseen_succ, 1, depth) for unseen_succ in unseen_succs])
#         # print(v)
#
#     return v
#
#
# def min_value(self, game_state, agent_index, depth):
#     # print("enter to min")
#     v = 1e80
#
#     succs_direction_pair = game_state.generateGhostSuccessors(agent_index)
#     succs = [succ[0] for succ in succs_direction_pair]
#
#     unseen_succs = []
#     for succ in succs:
#         if not self.already_seen_state(succ):
#             unseen_succs.append(succ)
#
#     if len(unseen_succs) > 0:
#         v = min([self.value(unseen_succ, 0, depth) for unseen_succ in unseen_succs])
#
#     return v
#
