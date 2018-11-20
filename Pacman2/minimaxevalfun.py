# Complete this class for all parts of the project
import sys

from pacman_module.game import Agent, random, Directions
from pacman_module.pacman import GameState
from pacman_module import util
numOfExpandedStates = 0

sys.setrecursionlimit(1000)
class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args
        self.pacmanIndex = 0
        self.ghostIndex = 1

        self.agentCount = 2
        self.depth = 3

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
        print( random.randint(0, 5 - 1))

        s.generatePacmanSuccessors()
        s.generateGhostSuccessors(self.pacmanIndex)
        s.getLegalActions(self.pacmanIndex)
        s.getPacmanPosition()
        s.getScore()
        s.getFood()
        s.getWalls()
        s.getGhostPositions()
        s.getCapsules()
        s.isWin()
        s.isLose()

        # true depth is because that each agent plays one in a total move.
        trueDepth = self.agentCount * self.depth

        # Get first pacman successors
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]
        print("succs: ", succs)
        # LegalActions = gameState.getLegalActions(0)
        # if Directions.STOP in LegalActions:
        #     LegalActions.remove(Directions.STOP)
        # listNextStates = [gameState.generateSuccessor(0, action) for action in LegalActions]
        # print(self.MiniMax_Value(numOfAgent,0,gameState,trueDepth))

        # get the minimax value as a
        print("antes de V")
        v = [self.MiniMax_Value(self.agentCount, 1, nextState, trueDepth - 1) for nextState in succs]
        print("Despues de V")
        print(v)
        maxV = max(v)
        index = v.index(maxV)
        # listMax = []
        # for i in range(0, len(v)):
        #     if v[i] == MaxV:
        #         listMax.append(i)
        #     i = random.randint(0, len(listMax) - 1)
        #     # i = randint(0, len(listMax) - 1)
        #
        # action = moves[listMax[i]]
        # print(action)
        print("moves: ",moves[index])
        return moves[index]

    def MiniMax_Value(self, numOfAgent, agentIndex, gameState, depth):

        global numOfExpandedStates

        LegalActions = gameState.getLegalActions(agentIndex)
        listNextStates = [gameState.generateSuccessor(agentIndex, action) for action in LegalActions]
        print("nextstates: ",listNextStates)
        numOfExpandedStates += len(listNextStates)
        print("Number of states expanded = " + str(numOfExpandedStates))
        print("agentindex",agentIndex)
        if gameState.isLose() or gameState.isWin() or depth == 0: #
            return self.scoreEvaluationFunction(gameState)
        else:

            if (agentIndex == 0):
                print("entro aquí")
                return max(
                    [self.MiniMax_Value(numOfAgent, (agentIndex + 1) % numOfAgent, nextState, depth - 1) for nextState
                     in listNextStates])
            else:

                return min(
                    [self.MiniMax_Value(numOfAgent, (agentIndex + 1) % numOfAgent, nextState, depth - 1) for nextState
                     in listNextStates])

    def scoreEvaluationFunction(self, currentGameState):
        """
          This default evaluation function just returns the score of the state.
          The score is the same one displayed in the Pacman GUI.
          This evaluation function is meant for use with adversarial search agents
          (not reflex agents).
        """
        print(currentGameState.getFood())
        foodlist=currentGameState.getFood().asList()
        print("foodlist: ",foodlist)
        pos=currentGameState.getPacmanPosition()
        print("Pos: ",pos)



        nearfooddist = 0
        if [util.manhattanDistance(pos, xy2) for xy2 in foodlist]:
            list = [util.manhattanDistance(currentGameState.getPacmanPosition(), xy2) for xy2 in foodlist]
            print("list: ", list)
            nearfooddist = min(list)
            print("nearfooddist: ", nearfooddist)

        numfood = currentGameState.getNumFood()
        print("numfood: ",numfood)
        evfun =-nearfooddist + currentGameState.getScore()*2-numfood*100
        return evfun
