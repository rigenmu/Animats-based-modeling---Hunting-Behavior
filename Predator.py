from Animat import Animat
from Actions import Actions
import qlearn_mod_random as qlearn

class Predator(Animat):

    def __init__(self,worldMap,scopeDist,width,height,color):
        Animat.__init__(self,worldMap,'predator',scopeDist,width,height,color)
        self.brain = qlearn.QLearn(actions=range(Actions.directions),alpha=0.1, gamma=0.9, epsilon=0.1)
        self.eatPreys = 0

    @property
    def eatPreys(self):
        return self._eatPreys

    @eatPreys.setter
    def eatPreys(self,value):
        self._eatPreys = value

    # predators' sensor would not be blocked by obstacles
    def getPreysWithinScope(self):
        preysWithinScope = []
        gridsWithinScope = self.getGridsWithinScope()
        for grid in gridsWithinScope:
            if self.worldMap.hasObjectAt(grid,'prey'):
                preysWithinScope.append(grid)

        return preysWithinScope

    def isEatingPrey(self):
        return self.isObjectAt(self.posOnMap,'prey')

    def printQTable(self):
        self.brain.printQTable()

    def update(self):
        state = self.calculateState()
        reward = -10

        #Check if the animat has been eaten by any of the predators
        if self.posOnMap in self.prevPos:
            reward += -40
        elif self.getPreysWithinScope():
            reward += 50 * (1 - self.calculateDist(self.posOnMap, min(self.getPreysWithinScope())))
        if self.isEatingPrey():
            #PreyAdult re-spawns itself randomly, if it gets eaten
            self.eatPreys += 1
            reward = 100

        if self.oldState is not None:
            self.brain.learn(self.oldState,self.oldAction,reward,state)

        state = self.calculateState()

        action, q = self.brain.chooseAction(state, True)
        # print q
        self.oldState = state
        self.oldAction = action
        self.recordPreviousNPos(2)
        self.performAction(action)

    def calculateState(self):
        def stateValueForGridWithinScope(gridWithinScope):
            if self.worldMap.hasObjectAt(gridWithinScope,'prey'):
                return 3
            elif self.worldMap.hasObjectAt(gridWithinScope,'food'):
                return 2
            elif self.worldMap.hasObjectAt(gridWithinScope,'obstacle'):
                return 1
            else:
                return 0

        return tuple([stateValueForGridWithinScope(gridWithinScope) for gridWithinScope in self.getGridsWithinScope()])
