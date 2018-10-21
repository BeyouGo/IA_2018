# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
from pacman_module.util import *


class PacmanAgent(Agent):
    # seenPos = set()  # position " (1,2) "
    # path = []  # "[ [(1,2),"South"], ... ]"
    # fringe = Stack()  # [ [state,"South"] , ... ]
    # branches = Stack()  # [[state,"south"],..]
    # counter = 0
    #
    # seenFood = []

    fringe = Queue()    # [ [state,"South"] , ... ]
    nodes = list()      # [ [[(5,4),"west"],...,[(5,3),"East"]], ... ,[[(5,4),"west"],...,[(5,3),"East"]] ]
    path = list()       # [ [pos, dir],...,[pos,dir]]
    seenPos = set()    # [pos,...,pos]
    goal = None

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
        print("Current position : ", pos)
        print("Pathes computed : ",[j[0] for j in self.path])

        # We already have computed a path
        print(pos ," ", self.path)
        if(pos in [i[0] for i in self.path] and (not (pos == self.path[0][0]))):

            print("heehehhehhee : ",[j[0] for j in self.path])
            k = [j[0] for j in self.path].index(pos)
            return self.path[k-1][1]
        else:
            print("Your not in a computed path.")
            print("Clear all and recompute path...")

            self.path.clear()
            self.fringe = Stack()
            self.nodes.clear()
            self.seenPos = set()
            self.goal = None




        # There is no path, we have to initiate the computation of the path
        if self.fringe.isEmpty():
            pos = s.getPacmanPosition()
            succs = s.generatePacmanSuccessors()

            self.seenPos.add(pos)

            for i in (0, len(succs) - 1):
                # self.nodes.append([pos,[[succs[i],succs[i][1]]]])
                # self.nodes.append([succs[i][0].getPacmanPosition(),[[succs[i][0].getPacmanPosition(),succs[i][1]]]])
                # self.nodes.append([succs[i][0].getPacmanPosition(),[[s.getPacmanPosition(),]]])
                self.nodes.append([[succs[i][0].getPacmanPosition(),succs[i][1]]])
                self.fringe.push(succs[i])

        curr = s
        prev = s

        # computation of the path has been initiated, we have to continue until we 've found some food
        while not self.fringe.isEmpty():

            print("-------- new loop\n\n")
            # print("Fringe before pop = ", self.fringe.list)
            # print("path = ", self.path)

            prev = curr

            [curr, currDir] = self.fringe.pop()

            # print("Fringe after pop = ", self.fringe.list)
            # # print("this is the fringe !! " ,self.fringe.list)
            # print("curr pos = ", curr.getPacmanPosition())
            # print("Curr State\n", curr)
            # # Take the first element in the fringe

            currPos = curr.getPacmanPosition() # ie. (4 , 5)

            # Considere the element as "Seen" to avoid loop
            self.seenPos.add(currPos)


            # self.path.append([curr.getPacmanPosition(), currDir])


            # is there food ?
            # print("prev\n",prev)
            # print(currPos)
            # print("Food: ",prev.getFood())
            if (prev.getFood()[currPos[0] ][currPos[1] ]):
                print("Found food at: " , str(currPos))

                # Define curr node as the final one
                self.goal = currPos
                # print("Goal = ", self.goal)

                k = [j[0][0] for j in self.nodes ].index(currPos)
                self.path = list(self.nodes[k])



                # compute the first move to make to reach goal

                # k = [j[0] for j in self.nodes].index(self.goal)
                # currPath = self.nodes[k][1]
                # print(self.path)
                length = len(self.path)
                return self.path[length-1][1]


                # check if it is a food that we already ate?

                # if not curr.getPacmanPosition() in self.seenFood:
                #     self.seenFood.append(curr.getPacmanPosition())
                #     return self.path[0][1]


            # print("SeenPos :", self.seenPos)
            allSuccs = curr.generatePacmanSuccessors()
            if len(allSuccs) == 0:
                print("Error : It should always exist at least one successor")


            # print("All      ", [i[0].getPacmanPosition() for i in allSuccs])
            succs = self.removeSeenFromSuccessor(allSuccs)
            # print("Succs    ", [i[0].getPacmanPosition() for i in succs])

            # if (len(succs) > 1):
            #     for i in (1, len(succs) - 1):
            #         self.branches.push(curr)

            # if (len(succs) == 0):
            #     if (not self.branches.isEmpty()):
            #         currBranch = self.branches.pop()
            #         self.removeInPathUntil(currBranch)

            for succ in succs:
                if succ[0].getPacmanPosition() not in self.seenPos:

                    # get path from initial state to the previous current node
                    print(self.nodes)


                    print([j[0][0] for j in self.nodes])
                    k = [j[0][0] for j in self.nodes].index(currPos)
                    currPath = list( self.nodes[k])


                    currPath.insert(0,[succ[0].getPacmanPosition(),succ[1]])
                    # currPath.append([currPos[0].getPacmanPosition(),currPos[1]])
                    # currPath.append([succ.getPacmanPosition(),succ[1]])
                    # currPath.append([currPos,succ[1]])

                    self.nodes.append(currPath)
                    # self.nodes.append([succ[0].getPacmanPosition(),currPath])
                    self.fringe.push(succ)


    # def removeInPathUntil(self, s):
    #     # print("old path = ",self.path)
    #     i = [i[0] for i in self.path].index(s.getPacmanPosition())
    #
    #     newPath = self.path[0: i+1]  # Possible error here with the i or i+1 ----> todo: check if it works
    #     self.path = newPath
    #     # print("new path = ", self.path)
    #     return

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
