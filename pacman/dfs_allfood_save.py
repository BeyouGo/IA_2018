import random

from pacman_module.game import Agent
from pacman_module.pacman import Directions
from random import randint
from pacman_module.util import *


class PacmanAgent(Agent):
    """
    An agent controlled by the keyboard.
    """


    fringe = Stack()  #
    nodes = []        #
    path = []         #
    seenPos =[]   #
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
        if not self.path:
            state_winner=self.get_path(state)
            print("lolololo",state_winner.getPacmanPosition())
            aux=False
            while not state_winner.getPacmanPosition() is (5,5):
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
                if state_winner.getPacmanPosition() == (5,5):
                    break

        return self.path.pop(len(self.path)-1)










    def get_path(self, state):
        if self.fringe.isEmpty():
            pos = state.getPacmanPosition()
            succs = state.generatePacmanSuccessors()
            self.nodes.append([None, (state, Directions.STOP)])

            self.seenPos.append([state.getPacmanPosition(), state.getFood])

            for succ in succs:
                # self.nodes.append([pos,[[succs[i],succs[i][1]]]])
                # self.nodes.append([succs[i][0].getPacmanPosition(),[[succs[i][0].getPacmanPosition(),succs[i][1]]]])
                # self.nodes.append([succs[i][0].getPacmanPosition(),[[s.getPacmanPosition(),]]])
                self.nodes.append([state, succ])
                self.fringe.push(succ[0])
                print("succ[o]",succ[0])


        print("esto qué?",self.fringe)


        while not False:

            print("-------- new loop\n\n")
            #print("Fringe before pop = ", self.fringe.list)
            #print("path = ", self.path)



            state_curr= self.fringe.pop()
            #print("Fringe after pop = ", self.fringe.list)
            if state_curr.isWin():
                print(state_curr.getPacmanPosition())
                return state_curr

            self.seenPos.append([state_curr.getPacmanPosition(),state_curr.getFood])

            succs=state_curr.generatePacmanSuccessors()
            print("seenPos: ",self.seenPos)
            print("succs: ",succs)
            #print("seenPos: ",[i for i in self.seenPos])

            #seenFoodFood=[i.getFood() for i in self.seenPos]


            print("state_current:\n\n ",state_curr.getPacmanPosition(),"\n", state_curr)
            numfoodcurr= state_curr.getNumFood()
            print("numFoodcurr: ", numfoodcurr)
            numfoodsucc=succs[0][0].getNumFood()
            print("numFoodsucc: ",numfoodsucc)
            print("lensuccs: ",len(succs))
           ##if len(succs)==1:
           #    self.nodes.append([state_curr, succ])
           #    self.fringe.push(succ[0])
           # print("comida en state?: ",state_curr.getFood()[state_curr.getPacmanPosition()[0]][state_curr.getPacmanPosition()[1]])
            for succ in succs:
                print("succPos: ",succ[0].getPacmanPosition())
                print("succFood: ",succ[0].getFood())
                #if succ[0].getFood()[succ[0].getPacmanPosition()[0]][succ[0].getPacmanPosition()[1]]:
                #    print("entra al bucle1: ")


                        #print("succ[0]getFood: ",succ[0].getFood())
                #    self.nodes.append([state_curr,succ])
                        #print("self.nodes", self.nodes)
                #    self.fringe.push(succ[0])
                  #  print("fringePush3: ",self.fringe)

                        #if succ[0].getPacmanPosition() in [i.getPacmanPosition() for i in self.seenPos] and succ[0].getFood() in [i.getFood() for i in self.seenPos]:
                        #   print("entro al bucle")
                        #  self.fringe.pop()
                        # self.nodes.pop()
                        #print("fringePop2: ",self.fringe)


                if succ[0].getPacmanPosition() not in [i[0] for i in self.seenPos]:
                   #print("succ[0]getFood: ",succ[0].getFood())
                   self.nodes.append([state_curr,succ])
                   #print("self.nodes", self.nodes)
                   self.fringe.push(succ[0])
                   print("fringePush2: ",self.fringe)


                elif succ[0].getFood() != state_curr.getFood():
                    #  for i in range (0,len(self.seenPos)-1):
                    #     print("entro al for")
                    # #k = [j for j in self.seenPos].index(succ[0].getPacmanPosition())
                    #     if succ[0].getPacmanPosition() == self.seenPos[i].getPacmanPosition() and succ[0].getFood() != self.seenPos[i].getFood():
                    #         print("entro al bucle3:",self.seenPos[i].getPacmanPosition())
                    self.nodes.append([state_curr, succ])
                    self.fringe.push(succ[0])
                    print("fringePush1: ", self.fringe)

                if succ[0].getPacmanPosition() in [i[0] for i in self.seenPos]:
                #    print("seenPos: ",i,self.seenPos[i])
                    print("llego aqui: ")
                    if [succ[0].getPacmanPosition,succ[0].getFood()] not in [i for i in self.seenPos]:

                        self.nodes.append([state_curr, succ])
                        self.fringe.push(succ[0])
                        print("fringePush2: ", self.fringe)











