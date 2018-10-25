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
            self.path,last = self.astar2(state)
            self.path = self.reconstrucPath(last)

        direction = self.path.pop(state)
        print(direction)

        return direction



    def astar2(self,state):

        path = {}
        costs = {}
        fringe = util.PriorityQueue()
        expanded = set()

        last = [None,None]
        expanded.add((state.getPacmanPosition(), state.getFood()))

        path[state] = [None, None]
        costs[(state.getPacmanPosition(),state.getFood())] = 0
        fringe.push(state,0)

        while not fringe.isEmpty():
            oldHeuristic,current = fringe.pop()
            expanded.add((current.getPacmanPosition(), current.getFood()))

            # print("new loop")

            if(current.isWin()):
                last = current
                break

            for successor, direction in current.generatePacmanSuccessors():
                if not (successor.getPacmanPosition(),successor.getFood()) in expanded:
                    succCost = (costs[(current.getPacmanPosition(),current.getFood())] + 1)
                    costs[(successor.getPacmanPosition(),successor.getFood())] = succCost
                    fringe.push(successor,succCost+self.heuristic(successor,[(0,0)]))

                    # if successors not already expanded
                    # add them to fringe


                    path[successor] = [current, direction]



        return path,last










    def heuristic(self,state,goal):

        foods = []
        for i in range (0, state.getFood().width-1):
            for j in range (0, state.getFood().height-1):
                if(state.getFood().data[i][j] == True):
                    foods.append((i,j))

        node = state.getPacmanPosition()
        heuristic = 0

        while foods:
            distance, food = min([(util.manhattanDistance(node, food), food) for food in foods])
            heuristic += distance
            node = food
            foods.remove(food)

        return heuristic

    # def heuristic(self,state,goal):
    #
    #     heuristic = util.manhattanDistance(state.getPacmanPosition(), goal)
    #     return heuristic

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


    #
    # def astar(self,state,goal):
    #
    #     print(" A* started ...")
    #     fringe = util.PriorityQueue()
    #     seen = []
    #     costs = {}
    #     path = {}
    #
    #     path[state.getPacmanPosition()] = [None,None]
    #     costs[state.getPacmanPosition()] = 0
    #     fringe.push(state,costs[state.getPacmanPosition()]+self.heuristic(state,goal) )
    #
    #
    #     while not fringe.isEmpty():
    #
    #         oldHeuristic, currState = fringe.pop()
    #         print("currState :\n",currState)
    #         print(path)
    #
    #
    #         seen.append(currState.getPacmanPosition())
    #
    #         if self.isGoal(currState):
    #             break
    #
    #
    #         for successor, direction in currState.generatePacmanSuccessors():
    #             if(seen.count(successor.getPacmanPosition()) ==  0):
    #                 succCost = (costs[currState.getPacmanPosition()] + 1)
    #                 costs[successor.getPacmanPosition()] = succCost
    #                 fringe.push(successor,succCost + self.heuristic(successor,goal))
    #
    #                 path[successor.getPacmanPosition()] = [currState.getPacmanPosition(), direction]
    #
    #
    #     return path

        # came_from = {}
        # came_dir = {}
        # test1 = {}
        # cost_so_far = {}
        # came_from[state] = [None,None]
        # cost_so_far[state] = 0
        #
        #
        # while not frontier.isEmpty():
        #     print("====== New Loop")
        #
        #     heuristic,current = frontier.pop()
        #
        #     print(current)
        #
        #     if current.isWin():
        #         print("win")
        #         break
        #
        #     for succ, dir in current.generatePacmanSuccessors():
        #         new_cost = cost_so_far[current] + 1
        #
        #         if succ not in cost_so_far or new_cost < cost_so_far[succ]:
        #             cost_so_far[succ] = new_cost
        #             priority = new_cost + self.heuristic(succ)
        #             frontier.push(succ, priority)
        #             # came_from[succ] = current
        #             # came_dir[succ] = dir
        #
        #             test1[current] = [succ,dir]
        #
        # # return came_from,came_dir
        #
        # print(" A* finished")


    # def findFoodPos(self,state):
    #     foods = []
    #     for i in range(0, state.getFood().width - 1):
    #         for j in range(0, state.getFood().height - 1):
    #             if (state.getFood().data[i][j] == True):
    #                 return (i,j)
    #
    #
    # def isGoal(self,state):
    #     foods = []
    #     for i in range (0, state.getFood().width-1):
    #         for j in range (0, state.getFood().height-1):
    #             if(state.getFood().data[i][j] == True):
    #                 foods.append((i,j))
    #     return len(foods) == 0

