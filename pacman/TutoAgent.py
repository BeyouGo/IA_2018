# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
from pacman_module.util import *



class PacmanAgent(Agent):

    seen = set()
    path = []
    fringe = Stack()
    branches = Stack()

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

        print("New Time Step : \n\n")

        if s in [i[0] for i in self.path]:

            i = [i[0] for i in self.path].index(s)
            print("State already in the path ==> here is the next move pre-computed: ", self.path[i][1] )
            return self.path[i][1]

        tmp = []
        if self.fringe.isEmpty():
            self.seen.add(s)
            succs = s.generatePacmanSuccessors()
            for i in (0, len(succs) -1):
                self.fringe.push(succs[i])
                tmp.append(succs[i])



        while not self.fringe.isEmpty():

            print("new loop\n\n")
            [curr, currDir] = self.fringe.pop()
            # print("this is the fringe !! " ,self.fringe.list)

            self.seen.add(curr)
            # print("seen \n",self.seen)
            self.path.append([curr,currDir])

            if (curr.getFood()[curr.getPacmanPosition()[0]][curr.getPacmanPosition()[1]] == "T"):
                return self.path[0][1]

            allSuccs = curr.generatePacmanSuccessors()
            print("All      ", allSuccs)
            succs = self.removeSeenFromSuccessor(allSuccs)
            print("Succs    ", succs)



            if(len(succs) > 1):
                for i in (1, len(succs)-1):
                    self.branches.push(curr)

            if(len(succs) == 0):
                currBranch = self.branches.pop()
                self.removeInPathUntil(currBranch)


            for i in (0, len(succs) -1):
                if succs[i][0] not in self.seen:
                    self.fringe.push(succs[i])



    def removeInPathUntil(self, s ):

        i = [i[0] for i in self.path].index(s)

        newPath = self.path[0: i] # Possible error here with the i or i+1 ----> todo: check if it works
        self.path = newPath
        return


    def removeSeenFromSuccessor(self,succs):

        for curr in self.seen :
            print("curr seen :\n ", curr)
            try:
                j = [i[0] for i in succs].index(curr)

            except ValueError:
                "hello" # nothing to do
            else:
                succs.remove(j)
                succs.remove(curr)

        return succs



        #
        #
        # legals = s.getLegalActions()
        # legals.remove(Directions.STOP)
        # id = randint(0, len(legals)-1)



        return legals[id]

