# Complete this class for all parts of the project

from pacman_module.game import Agent, random, Directions

from pacman_module.pacman import GameState
from pacman_module import util
numOfExpandedStates = 0


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

        trueDepth = self.agentCount * self.depth

        # Get first pacman successors
        succsDirectionPair = s.generatePacmanSuccessors()
        succs = [succ[0] for succ in succsDirectionPair]
        moves = [succ[1] for succ in succsDirectionPair]

        v = [self.Alpha_Beta_Value(self.agentCount, 1, nextGameState, trueDepth - 1, -1e308, 1e308) for nextGameState in
             succs]
        print(v)
        maxV = max(v)
        index = v.index(maxV)
        return moves[index]

    def Alpha_Beta_Value(self, numOfAgent, agentIndex, gameState, depth, alpha, beta):

        global numOfExpandedStates

        LegalActions = gameState.getLegalActions(agentIndex)
        if (agentIndex == 0):
            if Directions.STOP in LegalActions:
                LegalActions.remove(Directions.STOP)
        listNextStates = [gameState.generateSuccessor(agentIndex, action) for action in LegalActions]
        numOfExpandedStates += len(listNextStates)
        print("Number of states expanded = " + str(numOfExpandedStates))

        # terminal test
        if (gameState.isLose() or gameState.isWin() or depth == 0):
            return self.scoreEvaluationFunction(gameState,agentIndex)
        else:
            # if Pacman
            if (agentIndex == 0):
                v = -1e308
                for nextState in listNextStates:
                    v = max(
                        self.Alpha_Beta_Value(numOfAgent, (agentIndex + 1) % numOfAgent, nextState, depth - 1, alpha,
                                              beta), v)
                    if (v >= beta):
                        return v
                    alpha = max(alpha, v)
                return v
            # if Ghost
            else:
                v = 1e308
                for nextState in listNextStates:
                    v = min(
                        self.Alpha_Beta_Value(numOfAgent, (agentIndex + 1) % numOfAgent, nextState, depth - 1, alpha,
                                              beta), v)
                    if (v <= alpha):
                        return v
                    beta = min(beta, v)
                return v

    def scoreEvaluationFunction(self, currentGameState, agentIndex):
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
        numfood=currentGameState.getNumFood()



        nearfooddist = 0
        if [util.manhattanDistance(pos, xy2) for xy2 in foodlist]:
            list = [util.manhattanDistance(currentGameState.getPacmanPosition(), xy2) for xy2 in foodlist]
            print("list: ", list)
            nearfooddist = min(list)
            print("nearfooddist: ", nearfooddist)

        posghost=currentGameState.getGhostPosition(1)
        if util.manhattanDistance(pos, posghost) == 0:
            distghost=-99
        else:
            distghost=util.manhattanDistance(pos, posghost)

        evfun =currentGameState.getScore()-nearfooddist-numfood*1000-distghost
        print("evfun: ",evfun)
        return evfun
