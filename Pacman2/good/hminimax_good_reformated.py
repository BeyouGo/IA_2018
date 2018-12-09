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
        self.pacman_index = 0
        self.ghost_index = 1
        self.depth = 6
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
        self.add_seen_state(s, self.pacman_index, self.depth)

        # Generate s successor
        succs_direction_pair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succs_direction_pair]
        moves = [succ[1] for succ in succs_direction_pair]

        # Find the best one using h minimax
        v = [self.value(nextGameState, 1, self.depth) for nextGameState in succs]
        maxV = max(v)
        index = v.index(maxV)
        return moves[index]

    def value(self, game_state, agent_index, depth):

        # Check if game ended or max depth occures
        if game_state.isLose() or game_state.isWin() or depth == 0:
            return self.score_evaluation_function(game_state)

        # Avoid Loops
        if self.already_seen_state(game_state, agent_index, depth):
            if agent_index == 0:
                return self.infinity
            else:
                return -self.infinity
        self.add_seen_state(game_state, agent_index, depth)

        # Apply H minimax
        if agent_index == self.pacman_index:
            return self.max_value(game_state, depth - 1)

        if agent_index == self.ghost_index:
            return self.min_value(game_state, depth - 1)

    def max_value(self, game_state, depth):

        succs_direction_pair = game_state.generatePacmanSuccessors()
        succs = [succ[0] for succ in succs_direction_pair]
        v = max([self.value(succ, self.ghost_index, depth) for succ in succs])
        return v

    def min_value(self, game_state, depth):

        succs_direction_pair = game_state.generateGhostSuccessors(1)
        succs = [succ[0] for succ in succs_direction_pair]
        v = min([self.value(succ, self.pacman_index, depth) for succ in succs])
        return v

    def add_seen_state(self, game_state, agent_index, depth):
        self.seen.append(
            (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0], agent_index,
             depth))

    def already_seen_state(self, game_state, agent_index, depth):
        return (self.seen.count(
            (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],
             agent_index, depth)) > 0)

    def score_evaluation_function(self, current_game_state):
        food_list = current_game_state.getFood().asList()
        pacman_pos = current_game_state.getPacmanPosition()
        food_nbr = current_game_state.getNumFood()

        near_food_dist = 0
        if [util.manhattanDistance(pacman_pos, xy2) for xy2 in food_list]:
            food_list = [util.manhattanDistance(current_game_state.getPacmanPosition(), xy2) for xy2 in food_list]
            near_food_dist = min(food_list)

        ghost_pos = current_game_state.getGhostPosition(1)
        ghost_dist = 0
        if util.manhattanDistance(pacman_pos, ghost_pos) == 0:
            ghost_dist = self.infinity
        else:
            ghost_dist = util.manhattanDistance(pacman_pos, ghost_pos)

        evfun = - food_nbr * 10 - near_food_dist * 2 + current_game_state.getScore() - ghost_dist
        return evfun
