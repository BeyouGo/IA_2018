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

        self.came_from={}

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

        if(len(self.came_from) == 0):
            self.came_from = self.astar(state)

        # succ = state
        # while succ in self.came_from.keys():
        #     print(self.came_from[succ][0])
        #     succ,direction = self.came_from[succ]


        succ,direction =  self.came_from[state]

        print(direction)


        return direction


    def isGoal(self,state):
        foods = []
        for i in range (0, state.getFood().width-1):
            for j in range (0, state.getFood().height-1):
                if(state.getFood().data[i][j] == True):
                    foods.append((i,j))
        return len(foods) == 0


    def heuristic(self,state):

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


    def astar(self,state):

        print(" A* started ...")
        frontier = util.PriorityQueue()
        frontier.push(state,0)
        came_from = {}
        came_dir = {}
        test1 = {}
        cost_so_far = {}
        came_from[state] = [None,None]
        cost_so_far[state] = 0


        while not frontier.isEmpty():
            print("====== New Loop")

            heuristic,current = frontier.pop()

            print(current)

            if current.isWin():
                print("win")
                break

            for succ, dir in current.generatePacmanSuccessors():
                new_cost = cost_so_far[current] + 1

                if succ not in cost_so_far or new_cost < cost_so_far[succ]:
                    cost_so_far[succ] = new_cost
                    priority = new_cost + self.heuristic(succ)
                    frontier.push(succ, priority)
                    # came_from[succ] = current
                    # came_dir[succ] = dir

                    test1[current] = [succ,dir]

        # return came_from,came_dir

        print(" A* finished")
        return test1


