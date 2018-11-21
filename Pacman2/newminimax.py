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

        ## simulate pacman turn
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]

        # Compute value for each of the pacman moves
        v = [self.value(nextGameState, 1) for nextGameState in succs]

        # return best one
        maxV = max(v)
        print(str(moves) + " - " + str(v) + " <-> " + str(maxV))
        index = v.index(maxV)

        return moves[index]

    def value(self, gameState, agent_index):
        # print("enter to value")
        # print("Depth = " + str(depth))
        # print("Agent Index = " + str(agent_index))
        # print("\n\n")

        if gameState.isLose() or gameState.isWin():
            return gameState.getScore()

        if self.already_seen_state(gameState, agent_index):
            if agent_index == self.pacmanIndex:
                return -1e80
            else:
                return 1e80
        self.add_seen_state(gameState, agent_index)


        if agent_index == self.pacmanIndex:
            return self.max_value(gameState,agent_index)

        if agent_index == self.ghostIndex:
            return self.min_value(gameState, agent_index)

    def max_value(self, game_state, agent_index):
        # print("enter to max")

        succs_direction_pair = game_state.generatePacmanSuccessors()
        succs = [succ[0] for succ in succs_direction_pair]

        v = max([self.value(succ, (agent_index + 1) % 2) for succ in succs])

        print("Max with agent " + str(agent_index)+ " <-> "+str(v))
        return v

    def min_value(self, game_state, agent_index):
        # print("enter to min")

        succs_direction_pair = game_state.generateGhostSuccessors(1)
        # print(succs_direction_pair)
        succs = [succ[0] for succ in succs_direction_pair]

        v = min([self.value(succ, (agent_index + 1) % 2) for succ in succs])

        print("Min with agent " + str(agent_index) + " <-> "+str(v))
        return v

    def add_seen_state(self, game_state, agent_index):
        # print((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],agent_index))
        self.seen.append(
            (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0], agent_index))

    def already_seen_state(self, game_state, agent_index):
        # print("Enter Already Seen State :")
        if (self.seen.count(
                (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],
                 agent_index)) > 0):
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
