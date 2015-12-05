from Grid import Grid

class Map:
       
    def __init__(self,numOfGridsInARow,sizeOfGrid,color,surface,pygame):
        self.numOfRows = numOfGridsInARow
        self.sizeOfGrid = sizeOfGrid
        self.pygame = pygame
        self.surface = surface
        self.color = color
        self.gridsMatrix = []
        
        # self.shouldDrawScreen = False
        self.setupMap()
        
    @property
    def numOfRows(self):
        return self._numOfRows
    
    @numOfRows.setter
    def numOfRows(self,value):
        self._numOfRows = value  

    @property
    def sizeOfGrid(self):
        return self._sizeOfGrid
            
    @sizeOfGrid.setter
    def sizeOfGrid(self,value):
        self._sizeOfGrid = value  

    @property
    def surface(self):
        return self._surface
    
    @surface.setter
    def surface(self,value):
        self._surface = value
    
    @property
    def pygame(self):
        return self._pygame
    
    @pygame.setter
    def pygame(self,value):
        self._pygame = value
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,value):
        self._color = value
     
    @property
    def gridsMatrix(self):
        return self._gridsMatrix
    
    @gridsMatrix.setter
    def gridsMatrix(self,value):
        self._gridsMatrix = value    
   
    def setupMap(self):
        self.gridsMatrix = [[Grid(self,self.sizeOfGrid,self.color,(i,j)) for i in range(self.numOfRows)] for j in range(self.numOfRows)] 
        for i in range(self.numOfRows):            
            for j in range(self.numOfRows):       
                self.gridsMatrix[i][j].drawGrid()
                
    def updateMap(self):
        # self.surface.fill(BLACK)
        for i in range(self.numOfRows):
            for j in range(self.numOfRows):
                self.gridsMatrix[i][j].drawGrid()  
        # self.pygame.display.update()
                
    def updateMapAt(self,pos,color):
        if self.isPosWithinBoundary(pos):
            self.gridsMatrix[pos[0]][pos[1]].drawGridWithColor(color)
                         
    def cleanMap(self):
        del self.gridsMatrix
            
    def isPosWithinBoundary(self,pos):
        if pos[0] < 0 or pos[0] >= self.numOfRows or pos[1] < 0 or pos[1] >= self.numOfRows:
            return False
        else:
            return True
     
    def hasAnyObjectAt(self,pos):
        if self.isPosWithinBoundary(pos):
            return self.gridsMatrix[pos[0]][pos[1]].hasAnyObject()
         
    def hasObjectAt(self,pos,objectName):
        if self.isPosWithinBoundary(pos):
            return self.gridsMatrix[pos[0]][pos[1]].hasObject(objectName)

    def setObjectAt(self,pos,objectName,obj):
        if self.isPosWithinBoundary(pos):
            self.gridsMatrix[pos[0]][pos[1]].objects.append(obj)
            self.gridsMatrix[pos[0]][pos[1]].objectsDict[objectName] = obj
     
    def setFoodIntensityAt(self,pos,foodIntensity):
        if self.isPosWithinBoundary(pos):
            self.gridsMatrix[pos[0]][pos[1]].foodIntensity += foodIntensity
           
    def removeObjectAt(self,pos,objectName):
        if self.hasObjectAt(pos,objectName):
            self.gridsMatrix[pos[0]][pos[1]].objects.remove(self.gridsMatrix[pos[0]][pos[1]].objectsDict[objectName])
            del self.gridsMatrix[pos[0]][pos[1]].objectsDict[objectName]
            
    def removeFoodIntensityAt(self,pos,foodIntensity):
        if self.isPosWithinBoundary(pos):
            self.gridsMatrix[pos[0]][pos[1]].foodIntensity -= foodIntensity
            if self.gridsMatrix[pos[0]][pos[1]].foodIntensity < 0:
                self.gridsMatrix[pos[0]][pos[1]].foodIntensity = 0
    
    def getObjectAt(self,pos,objectName):
        if self.hasObjectAt(pos,objectName):
            return self.gridsMatrix[pos[0]][pos[1]].objectsDict[objectName]
        
    def getFoodIntensityAt(self,pos):
        if self.isPosWithinBoundary(pos):
            return self.gridsMatrix[pos[0]][pos[1]].foodIntensity
                