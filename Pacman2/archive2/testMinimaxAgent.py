# Complete this class for all parts of the project
import sys

from pacman_module.game import Agent, random, Directions

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
        self.depth = 5
        self.seen = []

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

        self.seen = []
        self.add_seen_state(s,0)

        # LegalActions = gameState.getLegalActions(0)
        # if Directions.STOP in LegalActions:
        #     LegalActions.remove(Directions.STOP)
        # listNextStates = [gameState.generateSuccessor(0, action) for action in LegalActions]
        # print(self.MiniMax_Value(numOfAgent,0,gameState,trueDepth))

        # get the minimax value as a
        v = [self.MiniMax_Value(self.agentCount, 1, nextState, trueDepth - 1) for nextState in succs]

        print(str(moves) + " <-> "+str(v))
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
        return moves[index]

    def MiniMax_Value(self, numOfAgent, agentIndex, gameState, depth):


        LegalActions = gameState.getLegalActions(agentIndex)
        listNextStates = [gameState.generateSuccessor(agentIndex, action) for action in LegalActions]

        # if self.already_seen_state(gameState, agentIndex):
        #     if agentIndex == 0:
        #         return 1e80
        #     else:
        #         return -1e80
        #
        # self.add_seen_state(gameState, agentIndex)


        if gameState.isLose() or gameState.isWin() : #
            return self.scoreEvaluationFunction(gameState)
        else:

            if (agentIndex == 0):

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
        return currentGameState.getScore()


    def add_seen_state(self, game_state, agent_index):
        # print((game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0], agent_index))
        self.seen.append(
            (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0], agent_index))

    def already_seen_state(self, game_state, agent_index):
        # print("Enter Already Seen State :")
        return (self.seen.count(
                (game_state.getPacmanPosition(), game_state.getFood(), game_state.getGhostPositions()[0],
                 agent_index)) > 0)