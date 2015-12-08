from Animat import Animat
from Actions import Actions
import qlearn_mod_random as qlearn

class Prey(Animat):

    def __init__(self,worldMap,scopeDist,width,height,color):
        Animat.__init__(self,worldMap,'prey',scopeDist,width,height,color)
        self.brain = qlearn.QLearn(actions=range(Actions.directions),alpha=0.1, gamma=0.9, epsilon=0.1)
        self.eatFood = 0

    @property
    def eatFood(self):
        return self._eatFood

    @eatFood.setter
    def eatFood(self,value):
        self._eatFood = value

    # we assume preys only have visual sensor
    # and visual scope would be blocked by obstacles
    def getGridsWithinVisualScope(self):
        gridsWithinVisualScope = []

        gridsWithinScope = self.getGridsWithinScope()
        candidateGridsWithinVisualScope = []
        obstaclesWithinScope = []

        # split grids within scope into obstacles and non-obstacles
        for grid in gridsWithinScope:
            if self.worldMap.hasObjectAt(grid,'obstacle'):
                obstaclesWithinScope.append(grid)
            elif grid != self.posOnMap:
                candidateGridsWithinVisualScope.append(grid)

        for candidate in candidateGridsWithinVisualScope:
            blocked = False
            for obstacle in obstaclesWithinScope:
                if self.isGridBlockedByObstacle(candidate,obstacle):
                    blocked = True
                    break
            if not blocked:
                gridsWithinVisualScope.append(candidate)

        # for grid in gridsWithinVisualScope:
        #     self.worldMap.updateMapAt(grid,(255, 102, 0))
        return gridsWithinVisualScope


    def getPredatorsWithinVisualScope(self):
        predatorsWithinScope = []

        gridsWithinVisualScope = self.getGridsWithinVisualScope()
        for grid in gridsWithinVisualScope:
            if self.worldMap.hasObjectAt(grid,'predator'):
                predatorsWithinScope.append(grid)

        return predatorsWithinScope

    def hasFoodWithinVisualScope(self):
        gridsWithinVisualScope = self.getGridsWithinVisualScope()
        for grid in gridsWithinVisualScope:
            if self.worldMap.hasObjectAt(grid,'food'):
                return True

        return False

    def isBeingEatenByPredator(self):
        return self.isObjectAt(self.posOnMap,'predator')

    def isEatingFood(self):
        return self.isObjectAt(self.posOnMap,'food')

    def printQTable(self):
        self.brain.printQTable()

    def update(self):
        state = self.calculateState()
        reward = -10

        if self.hasFoodWithinVisualScope:
            reward += 5

        if self.getPredatorsWithinVisualScope():
            reward -= 20

        if self.posOnMap in self.prevPos:
            reward -= 20

        #Check if the animat has been eaten by any of the predators
        if(self.isBeingEatenByPredator()):
            reward = -200
            if self.oldState is not None:
                self.brain.learn(self.oldState,self.oldAction,reward,state)

            #clean up
            self.oldState = None
            self.oldAction = None
            self.respawnOnMap()
            return

        if(self.isEatingFood()):
            #clean up the eaten food
            food = self.worldMap.getObjectAt(self.posOnMap,'food')
            food.afterGotEaten()
            self.eatFood += 1
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

    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def onSegment(self, p, q, r):
        if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
            return True
        return False

    def isIntersect(self,p1,q1,p2,q2):

        if p1 == p2 or q1 == q2:
            return False

        o1 = self.orientation(p1,q1,p2)
        o2 = self.orientation(p1,q1,q2)
        o3 = self.orientation(p2,q2,p1)
        o4 = self.orientation(p2,q2,q1)

        if o1 != o2 and o3 != o4:
            return True
        else:
            return False


    def isGridBlockedByObstacle(self,grid,obstacle):
        """judge if cur_pos-self line intersect with obstacle line"""
        p1 = self.posOnMap
        q1 = grid
        p2 = obstacle
        q2 = (obstacle[0]+1, obstacle[1])
        p3 = obstacle
        q3 = (obstacle[0], obstacle[1]+1)

        if self.isIntersect(p1,q1,p2,q2) or self.isIntersect(p1,q1,p3,q3):
            return True
        else:
            return False
        # if o1 == 0 and self.onSegment(p1,p2,q1):
        #     return True
        # if o2 == 0 and self.onSegment(p1,q2,q1):
        #     return True
        # if o3 == 0 and self.onSegment(p2,p1,q2):
        #     return True
        # if o4 == 0 and self.onSegment(p2,q1,q2):
        #     return True
