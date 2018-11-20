# Complete this class for all parts of the project
import sys

from pacman_module.game import Agent, random, Directions
from pacman_module.pacman import GameState
from pacman_module import util
numOfExpandedStates = 0
totExpandedStates=0
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
        #trueDepth = self.agentCount * self.depth

        # Get first pacman successors
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]
        print("llego a antes de vvalue")
        v = [self.value(nextGameState, 1, self.depth,numOfExpandedStates) for nextGameState in succs]
        print("despues de vvalue")
        print("totExpandedStates: ",totExpandedStates)
        print(v)
        maxV = max(v)
        index = v.index(maxV)
        return moves[index]

    def value(self, gameState,agentIndex,depth,numOfExpandedStates):
        global totExpandedStates

        # print("entro a value")
        # print("depth in value: ", depth)

        totExpandedStates+=numOfExpandedStates
        if gameState.isLose() or gameState.isWin() or depth == 0:
            # print("mando score")
            # print("totOfExpandedStates: ",totExpandedStates)
            return gameState.getScore()
            # return self.scoreEvaluationFunction(gameState)

        if agentIndex==0:
            # print("voy a max_value")
            return self.max_value(gameState,depth,numOfExpandedStates)

        if agentIndex>0:
            # print("voy a min_value")
            return self.min_value(gameState,agentIndex,depth,numOfExpandedStates)

    def max_value(self, gameState,depth,numOfExpandedStates):
        v=-1e80
        nextMoves = gameState.getLegalPacmanActions()
        nextStates = [gameState.generatePacmanSuccessor(action) for action in nextMoves]
        numOfExpandedStates += len(nextStates)
        # print("depth en max_value: ",depth)
        v=max([self.value(next,1, depth-1,numOfExpandedStates) for next in nextStates])
        return v

    def min_value(self, gameState,agentIndex,depth,numOfExpandedStates):
        v=1e80
        succsDirectionPair = gameState.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        numOfExpandedStates += len(succs)
        # print("depth en min_value: ",depth)
        v=max([self.value(succ,0, depth,numOfExpandedStates) for succ in succs])

        return v



    def scoreEvaluationFunction(self, currentGameState):
        """
          This default evaluation function just returns the score of the state.
          The score is the same one displayed in the Pacman GUI.
          This evaluation function is meant for use with adversarial search agents
          (not reflex agents).
        """
        # print(currentGameState.getFood())
        foodlist=currentGameState.getFood().asList()
        # print("foodlist: ",foodlist)
        pos=currentGameState.getPacmanPosition()
        # print("Pos: ",pos)
        numfood=currentGameState.getNumFood()

        nearfooddist = 0
        if [util.manhattanDistance(pos, xy2) for xy2 in foodlist]:
            list = [util.manhattanDistance(currentGameState.getPacmanPosition(), xy2) for xy2 in foodlist]
            # print("list: ", list)
            nearfooddist = min(list)
            # print("nearfooddist: ", nearfooddist)

        posghost=currentGameState.getGhostPosition(1)
        if util.manhattanDistance(pos, posghost) == 0:
            distghost=-99
        else:
            distghost=util.manhattanDistance(pos, posghost)

        evfun =currentGameState.getScore()-nearfooddist*1.5-numfood*10-distghost
        # print("evfun: ",evfun)
        return evfun
