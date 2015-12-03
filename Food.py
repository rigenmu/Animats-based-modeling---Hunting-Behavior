from Environment import Environment
import math

class Food(Environment):
    
    def __init__(self,worldMap,width,height,color):
        Environment.__init__(self,worldMap,'food',width,height,color)
        # self.reward = 0 ?????????????????????
        self.gradientsCreated = False
        self.foodStrengthRounds = 0
        
        self.setup()

    @property
    def gradientsCreated(self):
        return self._gradientsCreated
    
    @gradientsCreated.setter
    def gradientsCreated(self,value):
        self._gradientsCreated = value
    
    def setup(self):
        self.worldMap.setFoodIntensityAt(self.posOnMap,1)
        
    def getNeighborGridCoordinates(self,numberOfRoundsAroundFood):
        neighborPositionsInRound = []
        for cellDistance in range(1,numberOfRoundsAroundFood+1):
            currentRoundNeighbors = []
            start = True
            hopIncrement = 1
            hopCount = 0
            (x,y) = (self.gridX,self.gridY)
            columnActivated = True
            while (x,y) != (self.gridX-cellDistance,self.gridY-(-cellDistance)):
                if start:
                    (x,y) = (self.gridX-cellDistance,self.gridY-(-cellDistance))
                    start = False
        
                if columnActivated:
                    y = y - hopIncrement
                    hopCount += hopIncrement
                else:
                    x -= hopIncrement
                    hopCount += hopIncrement
        
                if hopCount == -(cellDistance)*2 or hopCount == (cellDistance*2):
                    hopIncrement = -1 * hopIncrement
                    columnActivated = not columnActivated
        
                if hopCount == 0:
                    columnActivated = not columnActivated
                
                if((self.isWithinBounds(x, y))):
                    currentRoundNeighbors.append((x,y))
            neighborPositionsInRound.append(currentRoundNeighbors)
        return neighborPositionsInRound
    
    def createFoodGradientsInNeighbors(self,numberOfRoundsAroundFood):
        cellPositionsInNeighborhood = self.getNeighborGridCoordinates(numberOfRoundsAroundFood)        
        for neighborRoundCells in range(0,numberOfRoundsAroundFood):
            for cellPosition in cellPositionsInNeighborhood[neighborRoundCells]:
                cell = self.grid.cellMatrix[cellPosition[0]][cellPosition[1]]
                self.drawFoodIntensities(cell,neighborRoundCells)
                
    def drawFoodIntensities(self,cell,neighborRound): 
        self.foodStrengthRounds = neighborRound       
        foodIntensityAtCell = self.gaussianFn((neighborRound+1)*0.35)
        redGradientValue = 255        
        greenGradientValue = math.ceil(102 * foodIntensityAtCell)
        blueGradientValue = math.ceil(255 * foodIntensityAtCell)
        color = (255,255,255);
        # redGradientValue,255 - greenGradientValue,255 - blueGradientValue)
        if(foodIntensityAtCell >= cell.foodIntensity):
            if(self.grid.shouldDrawScreen):
                self.grid.pygame.draw.rect(self.grid.screen,color,(cell.x,cell.y,cell.width,cell.height))
            cell.foodIntensity = foodIntensityAtCell
            
    def gaussianFn(self,x):
        pi = 22/7
        sigma = 0.8
        y = 2*(1/(sigma * math.sqrt(2*pi)))*math.exp(-(math.pow(x, 2))/(2*math.pow(sigma,2)))
        return round(y,2)
    
    def gotEaten(self):
        cellPositionsInNeighborhood = self.getNeighborGridCoordinates(self.foodStrengthRounds)        
        for neighborRoundCells in range(0,self.foodStrengthRounds):
            for cellPosition in cellPositionsInNeighborhood[neighborRoundCells]:
                cell = self.grid.cellMatrix[cellPosition[0]][cellPosition[1]]
                self.clearFoodIntensities(cell)
    
    def clearFoodIntensities(self,cell):        
#         foodIntensityAtCell = self.gaussianFn((self.foodStrengthRounds+1)*0.35)        
        color = (255,255,255)
        if(cell.foodIntensity != 1):
            self.grid.pygame.draw.rect(self.grid.screen,color,(cell.x,cell.y,cell.width,cell.height))
            cell.foodIntensity = 0