# Complete this class for all parts of the project
from pacman_module import util
from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
import numpy


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args

        self.path = {}

    def get_action(self, state):
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

        if len(self.path) == 0:
            self.path, last = self.dfs(state)
            self.path = self.reconstruc_path(last)

        direction = self.path.pop(state)
        return direction

    def dfs(self, state):

        path = {}
        fringe = util.Stack()
        expanded = set()

        last = [None, None]
        expanded.add((state.getPacmanPosition(), state.getFood()))

        path[state] = [None, None]
        fringe.push(state)

        while not fringe.isEmpty():
            current = fringe.pop()
            expanded.add((current.getPacmanPosition(), current.getFood()))

            if current.isWin():
                last = current
                break

            # Add in the fringe is the node hasn't be expanded yet with the same food configuration
            for successor, direction in current.generatePacmanSuccessors():
                if not (successor.getPacmanPosition(), successor.getFood()) in expanded:
                    fringe.push(successor)
                    path[successor] = [current, direction]

        return path, last

    # Reconstruct the path to ease the access of direction
    def reconstruc_path(self, goal):

        new_path = {}
        predecessor, direction = self.path[goal]

        while predecessor is not None:
            new_path[predecessor] = direction
            predecessor, direction = self.path[predecessor]
        return new_path
