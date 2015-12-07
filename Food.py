from Environment import Environment
import math

class Food(Environment):

    def __init__(self,worldMap,scopeDist,width,height,color):
        Environment.__init__(self,worldMap,'food',width,height,color)
        self.scopeDist = scopeDist

        self.setupFood()

    def setupFood(self):
        self.worldMap.setFoodIntensityAt(self.posOnMap,1)
        self.setFoodIntensityWithinScope()

    def getGridsWithinScope(self):
        gridsWithinScope = []
        for i in range (-self.scopeDist,self.scopeDist+1):
            for j in range (-self.scopeDist,self.scopeDist+1):
                grid = (self.posOnMap[0]+i,self.posOnMap[1]+j)
                if self.worldMap.isPosWithinBoundary(grid) and not (i == 0 and j == 0):
                    gridsWithinScope.append(grid)

        return gridsWithinScope

    def setFoodIntensityWithinScope(self):
        gridsWithinScope = self.getGridsWithinScope()
        for grid in gridsWithinScope:
            dist = self.calculateDist(self.posOnMap,grid)
            foodIntensityAtGrid = self.gaussianFn((dist+1)*0.35)
            # print foodIntensityAtGrid
            self.worldMap.setFoodIntensityAt(grid,foodIntensityAtGrid)

    def removeFoodIntensityWithinScope(self):
        gridsWithinScope = self.getGridsWithinScope()
        for grid in gridsWithinScope:
            dist = self.calculateDist(self.posOnMap,grid)
            foodIntensityAtGrid = self.gaussianFn((dist+1)*0.35)
            self.worldMap.removeFoodIntensityAt(grid,foodIntensityAtGrid)

        self.worldMap.removeFoodIntensityAt(self.posOnMap,foodIntensityAtGrid)

    def afterGotEaten(self):
        self.removeFoodIntensityWithinScope()
        self.respawnOnMap()
        self.setupFood()

    def calculateDist(self,pos1,pos2):
        return math.hypot(pos2[0] - pos1[0], pos2[1] - pos1[1])

    def gaussianFn(self,x):
        pi = 22/7
        sigma = 0.8
        y = 2*(1/(sigma * math.sqrt(2*pi)))*math.exp(-(math.pow(x, 2))/(2*math.pow(sigma,2)))
        return round(y,2)
