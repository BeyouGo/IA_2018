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
        # Get first pacman successors
        self.seen = []
        self.add_seen_state(s, self.pacmanIndex)

        # simulate pacman turn
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]

        # Compute value for each of the pacman moves
        v = [self.min_value(succ, -self.infinity, self.infinity) for succ in succs]

        # return best one
        maxV = max(v)
        index = v.index(maxV)
        return moves[index]

    # Pacman turn
    def max_value(self, game_state, alpha, beta):

        # Check if game ended
        if game_state.isLose() or game_state.isWin():
            # return self.scoreEvaluationFunction(game_state)
            return game_state.getScore()

        # Avoid Loops
        if self.already_seen_state(game_state, self.pacmanIndex):
            return -self.infinity

        self.add_seen_state(game_state, self.pacmanIndex)

        # Applying alphabeta pruning
        v = -self.infinity
        for (succ, move) in game_state.generatePacmanSuccessors():
            v = max((self.min_value(succ, alpha, beta), v))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    # Ghost turn
    def min_value(self, game_state, alpha, beta):

        # Check if game ended
        if game_state.isLose() or game_state.isWin():
            return game_state.getScore()
            # return self.score_evaluation_function(game_state)

        # Avoid Loops
        if self.already_seen_state(game_state, self.ghostIndex):
            return self.infinity

        self.add_seen_state(game_state, self.ghostIndex)

        # Applying alphabeta pruning
        v = self.infinity
        for (succ, move) in game_state.generateGhostSuccessors(1):
            v = min(self.max_value(succ, alpha, beta), v)
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def add_seen_state(self, game_state, agent_index):
        self.seen.append(
            (game_state.getFood(), game_state.getPacmanPosition(), game_state.getGhostPositions()[0],
             agent_index))

    def already_seen_state(self, game_state, agent_index):
        return (self.seen.count(
            (game_state.getFood(), game_state.getPacmanPosition(), game_state.getGhostPositions()[0],
             agent_index)) > 0)

    def score_evaluation_function(self, current_game_state):
        food_list = current_game_state.getFood().asList()
        pacman_pos = current_game_state.getPacmanPosition()
        food_nbr = len(food_list)

        nearfooddist = 0
        if [util.manhattanDistance(pacman_pos, xy2) for xy2 in food_list]:
            food_dist_list = [util.manhattanDistance(current_game_state.getPacmanPosition(), xy2) for xy2 in food_list]
            nearfooddist = min(food_dist_list)

        ghost_pos = current_game_state.getGhostPosition(self.ghostIndex)
        ghost_dist = 0
        if util.manhattanDistance(pacman_pos, ghost_pos) == 0:
            ghost_dist = self.infinity
        else:
            ghost_dist = util.manhattanDistance(pacman_pos, ghost_pos)

        return - food_nbr * 10 - nearfooddist * 2 + current_game_state.getScore() - ghost_dist

