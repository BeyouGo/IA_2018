# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint


class PacmanAgent(Agent):
    maxInt = 10000000
    # seen = []
    reallySeen = []

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


        print("New Time Step : \n\n")

        seen = self.reallySeen.copy()

        try:
            b = self.reallySeen.index(s.getPacmanPosition())
        except ValueError:
            self.reallySeen.append(s.getPacmanPosition())

        succs = s.generatePacmanSuccessors()

        nextDirection = 'WEST'
        final = s

        for i in (0, len(succs) - 1):
            try:
                b = seen.index(succs[i][0].getPacmanPosition())
            except ValueError:
                found = self.recurr(succs[i][0], seen)
                if (found):
                    final = succs[i][0];
                    nextDirection = succs[i][1]
                    break
            else:
                print(succs[i][0].getPacmanPosition() , " is already seen")

        print(" i really add ",final.getPacmanPosition())
        self.reallySeen.append(final.getPacmanPosition())
        print("----------------------------------\n-------------------------------\n")
        return nextDirection

    def recurr(self, s, seen):
        # legals = s.getLegalActions()


        succs = s.generatePacmanSuccessors()

        if (s.getFood()[s.getPacmanPosition()[0]][s.getPacmanPosition()[1]] == "T"):
            print("There is food in that direction HERE !")

            return True

        for i in (0, len(succs) - 1):

            try:
            except ValueError:

                seen.append(succs[i][0].getPacmanPosition())

                print("i add ", succs[i][0].getPacmanPosition(), " to the seen list")
                self.recurr(succs[i][0], seen)

            else:
                "Do something with variable b"
            return False
