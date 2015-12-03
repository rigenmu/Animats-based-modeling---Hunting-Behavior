from BasicObject import BasicObject
from Obstacle import Obstacle
from Actions import Actions
import random

class Animat(BasicObject):   

    def __init__(self,worldMap,name,scopeDist,width,height,color):
        BasicObject.__init__(self,worldMap,name,width,height,color)   
        self.scopeDist = scopeDist     
        self.ai = None        
        self.fed = 0
        self.lastState = None
        self.lastAction = None       
        self.prevPositions = [] 
        
    @property
    def scopeDist(self):
        return self._scopeDist
    
    @scopeDist.setter
    def scopeDist(self,value):
        self._scopeDist = value
           
    @property
    def ai(self):
        return self._ai
    
    @ai.setter
    def ai(self,value):
        self._ai = value
    
    @property
    def fed(self):
        return self._fed
    
    @fed.setter
    def fed(self,value):
        self._fed = value
        
    @property
    def lastState(self):
        return self._lastState
    
    @lastState.setter
    def lastState(self,value):
        self._lastState = value
        
    @property
    def lastAction(self):
        return self._lastAction
    
    @lastAction.setter
    def lastAction(self,value):
        self._lastAction = value
    
    @property
    def prevPositions(self):
        return self._prevPositions
    
    @prevPositions.setter
    def prevPositions(self,value):
        self._prevPositions = value
      
    # we don't allow moving onto another animat that is of the same type
    def isPosValid(self,pos):
        if self.isWithinBoundaryAt(pos) and not self.isObjectAt(pos,'obstacle') and not self.isObjectAt(pos,self.name):
            return True
        return False
     
    # return all the grids position within animat's smell sensor scope    
    # i.e. without care of obstacles
    def getGridsWithinScope(self):
        gridsWithinScope = []     
        for i in range (-self.scopeDist,self.scopeDist+1):
            for j in range (-self.scopeDist,self.scopeDist+1):
                grid = (self.posOnMap[0]+i,self.posOnMap[1]+j)
                if self.worldMap.isPosWithinBoundary(grid):
                    gridsWithinScope.append(grid)
                    
        return gridsWithinScope
      
    def getPosFoodIntensity(self,pos):
        return self.worldMap.getFoodIntensityAt(pos)       
               
    def performAction(self,action):
        offset = (0,0)
        if action == Actions.MOVE_UP:
            offset = (0,1)
        elif action == Actions.MOVE_RIGHT:
            offset = (1,0)
        elif action == Actions.MOVE_DOWN:
            offset = (0,-1)
        elif action == Actions.MOVE_LEFT:
            offset = (-1,0)

        self.move(offset)          

    def move(self,nextPos):
        self.posOnMap = nextPos
        self.updateOnMap()
        #TODO: self.updateOnMap() 
#             self.removeFoodIfAnimatIsOnFood(self._gridX, self._gridY)
#             self.drawGameObjectAtCurrentPosition()
           
    def moveRandomly(self):
        randAction = random.randrange(Actions.directions)  
        self.performAction(randAction)
       
    # ????????
    def setPrevious2Positions(self):
        if(len(self.previousPositionTuples) == 2):
            self.previousPositionTuples.pop(0)
        self.previousPositionTuples.append(self.posOnMap)

        
        