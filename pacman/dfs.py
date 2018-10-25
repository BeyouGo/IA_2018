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

        if len(self.path) == 0 :
            self.path,last = self.dfs(state)
            self.path = self.reconstrucPath(last)

        direction = self.path.pop(state)
        print(direction)
        return direction



    def dfs(self,state):

        path = {}
        costs = {}
        fringe = util.Stack()
        expanded = set()

        last = [None,None]
        expanded.add((state.getPacmanPosition(), state.getFood()))

        path[state] = [None, None]
        costs[(state.getPacmanPosition(),state.getFood())] = 0
        fringe.push(state)

        while not fringe.isEmpty():
            current = fringe.pop()
            expanded.add((current.getPacmanPosition(), current.getFood()))

            if(current.isWin()):
                last = current
                break

            for successor, direction in current.generatePacmanSuccessors():
                if not (successor.getPacmanPosition(),successor.getFood()) in expanded:
                    succCost = (costs[(current.getPacmanPosition(),current.getFood())] + 1)
                    costs[(successor.getPacmanPosition(),successor.getFood())] = succCost
                    fringe.push(successor)

                    path[successor] = [current, direction]

        return path,last



    def reconstrucPath(self,goal):

        newPath = {}
        # print("path: ",self.path)
        # print("Goal:",goal)
        predecessor,direction = self.path[goal]

        while predecessor != None:
            newPath[predecessor] = direction
            predecessor,direction = self.path[predecessor]
            # print(predecessor)

        print("new Path: ",newPath)
        return newPath


