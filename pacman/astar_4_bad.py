# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
from pacman_module.util import *


class PacmanAgent(Agent):

        # [ [state,"South"] , ... ]
    nodes = list()      # [ [[(5,4),"west"],...,[(5,3),"East"]], ... ,[[(5,4),"west"],...,[(5,3),"East"]] ]
    path = list()       # [ [pos, dir],...,[pos,dir]]
    seenPos = set()    # [pos,...,pos]
    goal = None

    came_from = {}
    cost_so_far = {}

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
        self.goal = compute_goal()
        return


    def a_star_search(self,start,goal) :
        frontier = PriorityQueue()
        frontier.push(s,0)

        came_from = {}
        cost_so_far = {}
        came_from[s] = None
        cost_so_far[s] = 0


        while not frontier.isEmpty():
            current = frontier.pop()

            if(self.isFood(current)):
                break

            for next in s.getPacmanSuccessors():
                new_cost = cost_so_far[current] + 1

                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(self.goal, next)
                    frontier.push(next,priority)
                    came_from[next] = current

                    s.getCo













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
            self.fringe = PriorityQueue()
            self.nodes.clear()
            self.seenPos = set()
            self.goal = None




        # There is no path, we have to initiate the computation of the path
        if self.fringe.isEmpty():
            pos = s.getPacmanPosition()
            succs = s.generatePacmanSuccessors()

            self.seenPos.add(pos)

            for i in (0, len(succs) - 1):

                self.nodes.append([[succs[i][0].getPacmanPosition(),succs[i][1]]])
                self.fringe.push(succs[i])

        curr = s
        prev = s

        # computation of the path has been initiated, we have to continue until we 've found some food
        while not self.fringe.isEmpty():

            print("-------- new loop\n\n")


            prev = curr

            [curr, currDir] = self.fringe.pop()

            currPos = curr.getPacmanPosition() # ie. (4 , 5)

            # Considere the element as "Seen" to avoid loop
            self.seenPos.add(currPos)

            if (prev.getFood()[currPos[0] ][currPos[1] ]):
                print("Found food at: " , str(currPos))

                # Define curr node as the final one
                self.goal = currPos

                k = [j[0][0] for j in self.nodes ].index(currPos)
                self.path = list(self.nodes[k])
                length = len(self.path)
                return self.path[length-1][1]

            allSuccs = curr.generatePacmanSuccessors()
            if len(allSuccs) == 0:
                print("Error : It should always exist at least one successor")

           succs = self.removeSeenFromSuccessor(allSuccs)

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

        def isFood(self, current):
            pass


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


# Manatan distance has heuristic
    def heuristic(self,state1,state2):
        (x1,y1) = state1.getPacmanPosition()
        (x2,y2) = state2.getPacmanPosition()

        return abs(x1-x2) + abs(y1-y2)