import random

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module import util
from random import randint
from pacman_module.util import *


class PacmanAgent(Agent):
    """
    An agent controlled by the keyboard.
    """

    #fringe = util.Stack()  #
    nodes = []        #
    path = []         #
    #seenPos =set()   #
    goal = None

    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.lastMove = Directions.STOP
        self.keys = []

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
        start_state=state
        if not self.path:
            state_winner=self.get_path(state)
            print("lolololo",state_winner.getPacmanPosition())
            aux=False
            while not (state_winner.getPacmanPosition(),state_winner.getFood())==(start_state.getPacmanPosition(),start_state.getFood()):
                #print(self.nodes)
                k = [row[1][0] for row in self.nodes]
                dirs = [row[1][1] for row in self.nodes]
                parents = [row[0] for row in self.nodes]
                #print(k)
                index = k.index(state_winner)
                state_winner = parents[index]
                self.path.append(dirs[index])
                print(state_winner)
                print("path: ",self.path)


        return self.path.pop(len(self.path)-1)










    def get_path(self, state):

        fringe = util.Stack()
        seenPos = set()

        succs = state.generatePacmanSuccessors()
        self.nodes.append([None, (state, Directions.STOP)])

        seenPos.add((state.getPacmanPosition(), state.getFood))

        for succ in succs:
            self.nodes.append([state, succ])
        fringe.push(state)

        while not fringe.isEmpty():
            print("-------- new loop\n\n")
            state_curr= fringe.pop()
            seenPos.add((state_curr.getPacmanPosition(),state_curr.getFood()))
            if state_curr.isWin():
                print(state_curr.getPacmanPosition())
                return state_curr
            succs=state_curr.generatePacmanSuccessors()
            print("state_current:\n\n ",state_curr.getPacmanPosition(),"\n", state_curr)
            numfoodcurr= state_curr.getNumFood()
            print("numFoodcurr: ", numfoodcurr)
            numfoodsucc=succs[0][0].getNumFood()
            print("numFoodsucc: ",numfoodsucc)

            for succ in succs:
                if not (succ[0].getPacmanPosition(),succ[0].getFood()) in seenPos:
                    self.nodes.append([state_curr, succ])
                    fringe.push(succ[0])
                    print("fringePush: ", fringe)











