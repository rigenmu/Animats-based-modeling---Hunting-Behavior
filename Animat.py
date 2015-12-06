from BasicObject import BasicObject
from Obstacle import Obstacle
from Actions import Actions
import random

class Animat(BasicObject):   

    def __init__(self,worldMap,name,scopeDist,width,height,color):
        BasicObject.__init__(self,worldMap,name,width,height,color)   
        self.scopeDist = scopeDist         
        # for calculation of q-value   
        self.oldState = None
        self.oldAction = None 
        # encourage to visit un-explored area      
        self.prevPos = [] 
        
    @property
    def scopeDist(self):
        return self._scopeDist
    
    @scopeDist.setter
    def scopeDist(self,value):
        self._scopeDist = value
           
    @property
    def brain(self):
        return self._brain
    
    @brain.setter
    def brain(self,value):
        self._brain = value
        
    @property
    def oldState(self):
        return self._oldState
    
    @oldState.setter
    def oldState(self,value):
        self._oldState = value
        
    @property
    def oldAction(self):
        return self._oldAction
    
    @oldAction.setter
    def oldAction(self,value):
        self._oldAction = value
    
    @property
    def prevPos(self):
        return self._prevPos
    
    @prevPos.setter
    def prevPositions(self,value):
        self._prevPos = value
     
    # return all the grids' positions within animat's smell sensor scope    
    # i.e. without care of obstacles
    def getGridsWithinScope(self):
        gridsWithinScope = []     
        for i in range (-self.scopeDist,self.scopeDist+1):
            for j in range (-self.scopeDist,self.scopeDist+1):
                grid = (self.posOnMap[0]+i,self.posOnMap[1]+j)
                if self.worldMap.isPosWithinBoundary(grid):
                    gridsWithinScope.append(grid)
                    
        return gridsWithinScope
      
    # def getPosFoodIntensity(self,pos):
    #     return self.worldMap.getFoodIntensityAt(pos)    
               
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

    def move(self,offset):
        originPos = self.posOnMap
        nextPos = (self.posOnMap[0]+offset[0],self.posOnMap[1]+offset[1])

        if self.isPosValid(nextPos):
            self.removeObjectAt(originPos)
            self.posOnMap = nextPos
            self.setObjectAt(self.posOnMap)
            # self.drawOnMap()
           
    def moveRandomly(self):
        randAction = random.randrange(Actions.directions)  
        self.performAction(randAction)
       
    # ????????
    def recordPreviousNPos(self,n):
        if len(self.prevPos) >= n:
            self.prevPos.pop(0)
        self.prevPos.append(self.posOnMap)

        
        