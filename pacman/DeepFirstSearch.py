# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
from pacman_module.util import *


class PacmanAgent(Agent):
    seenPos = set()  # position " (1,2) "
    path = []  # "[ [(1,2),"South"], ... ]"
    fringe = Stack()  # [ [state,"South"] , ... ]
    branches = Stack()  # [[state,"south"],..]
    counter = 0

    seenFood = []

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
        pos = s.getPacmanPosition()
        if pos in [i[0] for i in self.path]:

            k = [j[0] for j in self.path].index(pos)
            if (len(self.path) > k+1):
                print("State already in the path ==> here is the next move pre-computed: ", self.path[k + 1][1])
                return self.path[k + 1][1]
            else:
                print("REFRESH ALL ")
                self.seenPos = set()  # position " (1,2) "
                self.path = []  # "[ [(1,2),"South"], ... ]"
                self.fringe = Stack()  # [ [state,"South"] , ... ]
                self.branches = Stack()  # [[state,"south"],..]
                # counter = 0

        tmp = []
        if self.fringe.isEmpty():
            self.seenPos.add(s.getPacmanPosition())
            succs = s.generatePacmanSuccessors()
            for i in (0, len(succs) - 1):
                self.fringe.push(succs[i])
                tmp.append(succs[i])

        while not self.fringe.isEmpty():

            print("-------- new loop\n\n")
            print("Fringe before pop = ", self.fringe.list)
            # print("path = ", self.path)
            [curr, currDir] = self.fringe.pop()
            print("Fringe after pop = ", self.fringe.list)
            # print("this is the fringe !! " ,self.fringe.list)
            print("curr pos = ", curr.getPacmanPosition())
            print("Curr State\n", curr)

            self.seenPos.add(curr.getPacmanPosition())

            # self.counter = self.counter+1
            # print("counter =", str(self.counter))
            # print("seen \n",self.seen)
            self.path.append([curr.getPacmanPosition(), currDir])

            # print("Food pos =", curr.getFood())
            print("Is food : ", curr.getFood()[curr.getPacmanPosition()[0]+1][curr.getPacmanPosition()[1]]+1)
            if (curr.getFood()[curr.getPacmanPosition()[0] + 1][curr.getPacmanPosition()[1] + 1] == True):
                print("I EAT FOOD")
                if not curr.getPacmanPosition() in self.seenFood:
                    self.seenFood.append(curr.getPacmanPosition())
                    return self.path[0][1]

            # print("SeenPos :", self.seenPos)
            allSuccs = curr.generatePacmanSuccessors()

            if len(allSuccs) == 0:
                return self.path[0][1]

            print("All      ", [i[0].getPacmanPosition() for i in allSuccs])
            succs = self.removeSeenFromSuccessor(allSuccs)
            print("Succs    ", [i[0].getPacmanPosition() for i in succs])

            if (len(succs) > 1):
                for i in (1, len(succs) - 1):
                    self.branches.push(curr)

            if (len(succs) == 0):
                if (not self.branches.isEmpty()):
                    currBranch = self.branches.pop()
                    self.removeInPathUntil(currBranch)

            for succ in succs:
                if succ[0].getPacmanPosition() not in self.seenPos:
                    self.fringe.push(succ)
            print("fringe  final = ", self.fringe.list)

    def removeInPathUntil(self, s):
        # print("old path = ",self.path)
        i = [i[0] for i in self.path].index(s.getPacmanPosition())

        newPath = self.path[0: i+1]  # Possible error here with the i or i+1 ----> todo: check if it works
        self.path = newPath
        print("new path = ", self.path)
        return

    def removeSeenFromSuccessor(self, succs):

        for currPos in self.seenPos:
            # print("curr seen :\n ", curr)

            # print( "LIST OF SUCCS POS" , [i[0].getPacmanPosition() for i in succs])

            j = [i[0].getPacmanPosition() for i in succs].count(currPos)
            # print("curr seenPos = ",currPos, " : " , j, " times ")


            if j > 0:
                # print("curr Pos =  ", currPos)
                # print("\t\t before pop ",str(j)," :",succs)
                succs.pop([i[0].getPacmanPosition() for i in succs].index(currPos))
                # print("\t\t after pop ", str(j), " :" , succs)
                # print("succ in  removeFrom... : ",[i[0].getPacmanPosition() for i in succs])

        return succs
