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
            self.path, last = self.astar2(state)
            self.path = self.reconstruc_path(last)

        direction = self.path.pop(state)

        return direction

    def astar2(self, state):

        path = {}
        costs = {}
        fringe = util.PriorityQueue()
        expanded = set()

        last = [None, None]
        expanded.add((state.getPacmanPosition(), state.getFood()))

        path[state] = [None, None]
        costs[(state.getPacmanPosition(), state.getFood())] = 0
        fringe.push(state, 0)

        while not fringe.isEmpty():
            old_heuristic, current = fringe.pop()
            expanded.add((current.getPacmanPosition(), current.getFood()))

            if (current.isWin()):
                last = current
                break

            # if successors not already expanded add them in the fringe
            for successor, direction in current.generatePacmanSuccessors():
                if not (successor.getPacmanPosition(), successor.getFood()) in expanded:
                    # Compute cost
                    succ_cost = (costs[(current.getPacmanPosition(), current.getFood())] + 1)
                    costs[(successor.getPacmanPosition(), successor.getFood())] = succ_cost

                    # add on the fringe with heuristic + cost
                    fringe.push(successor, succ_cost + self.heuristic(successor))

                    # keep track of the path taken
                    path[successor] = [current, direction]

        return path, last

    # Compute the minimum path between all food,
    # with the distance between two foods is the manathan distance between them
    def heuristic(self, state):

        foods = []
        for i in range(0, state.getFood().width - 1):
            for j in range(0, state.getFood().height - 1):
                if state.getFood().data[i][j]:
                    foods.append((i, j))

        node = state.getPacmanPosition()
        heuristic = 0

        while foods:
            distance, food = min([(util.manhattanDistance(node, food), food) for food in foods])
            heuristic += distance
            node = food
            foods.remove(food)

        return heuristic

    # Reconstruct the path to ease the access of direction
    def reconstruc_path(self, goal):

        new_path = {}
        predecessor, direction = self.path[goal]

        while predecessor is not None:
            new_path[predecessor] = direction
            predecessor, direction = self.path[predecessor]

        return new_path
