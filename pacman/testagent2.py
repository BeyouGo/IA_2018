# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
import queue


class PacmanAgent(Agent):
    reallySeen = []
    path = queue.Queue()


    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args

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
        val = self.depth_first_search(s)
        print(val)

        return "WEST"
        # legals = s.getLegalActions()
        # pos = s.getPacmanPosition()
        # score = s.getScore()
        # food = s.getFood()
        # walls = s.getWalls()
        # caps = s.getCapsules()

        # print("successors = " , successors)
        # print("socre = " , score)
        # print("pos = " , pos)
        # print("food = " , food)
        # print("walls = " , walls)
        # print("caps = " , caps)
        #
        #
        # frontier = [s]
        # seen = [s]
        # seen.extend(self.reallySeen)
        #
        # suc = self.recurr(frontier,seen)
        #
        # self.reallySeen.append(suc[0])
        #
        # return suc[1]


        myVariable = Stack(10)
    # def recurr(self, frontier, seen):
    #
    #     if (len(frontier) == 0):
    #         return False
    #
    #     curr = frontier[0]
    #     frontier.remove(curr)
    #
    #     succs = curr.generatePacmanSuccessors()
    #
    #     for i in (0, len(succs) - 1):
    #         currChild = succs[i][0]
    #         dir = succs[i][1]
    #
    #         try:
    #             b = seen.index(currChild)
    #         except ValueError:
    #
    #             frontier.append(currChild)
    #             seen.append(currChild)
    #
    #             if (currChild.getFood()[currChild.getPacmanPosition()[0]][currChild.getPacmanPosition()[1]] == "T"):
    #                 print("There is food in that direction HERE !")
    #                 return succs[i]
    #
    #             else:
    #                 print(frontier)
    #                 suc = self.recurr(frontier, seen)
    #                 return suc


    def depth_first_search(self, s):
        visited, stack = set(), [s]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                sucs = s.generatePacmanSuccessors()

                stack.extend(sucs[:][0].remove( visited))
        return visited