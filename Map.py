from Grid import Grid

class Map:
       
    def __init__(self,numOfGridsInARow,sizeOfGrid,color,screen,pygame):
        self.numOfRows = numOfGridsInARow
        self.sizeOfGrid = sizeOfGrid
        self.pygame = pygame
        self.screen = screen
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
    def screen(self):
        return self._screen
    
    @screen.setter
    def screen(self,value):
        self._screen = value
    
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
    
    def isPosWithinBoundary(pos):
        if pos[0] < 0 or pos[0] >= self.numOfRows or pos[1] < 0 or pos[1] >= self.numOfRows:
            return False
        else
            return True
    
    def getFoodIntensityAt(self,pos):
        return self.gridsMatrix[pos[0]][pos[1]].foodIntensity
     
    def hasAnyObjectAt(self,pos):
        return self.gridsMatrix[pos[0]][pos[1]].hasAnyObject()
         
    def hasObjectAt(self,pos,objectName):
        return self.gridsMatrix[pos[0]][pos[1]].hasObject(objectName)

    def setObjectAt(self,pos,objectName,obj):
        self.gridsMatrix[pos[0]][pos[1]].objects.append(obj)
        self.gridsMatrix[pos[0]][pos[1]].objectsIdx[objectName] = len(self.gridsMatrix[pos[0]][pos[1]].objects)-1
     
    def setFoodIntensityAt(self,pos,foodIntensity):
        self.gridMatrix[pos[0]][pos[1]].foodIntensity = foodIntensity
           
    def removeObjectAt(self,pos,objectName):
        if self.hasObjectAt(pos,objectName):
            del self.gridsMatrix[pos[0]][pos[1]].objects[objectsIdx[objectName]]
            del self.gridsMatrix[pos[0]][pos[1]].objectsIdx[objectName]
    
    def updateMapAt(self,pos):
        if self.isPosWithinBoundary(pos):
            self.gridsMatrix[pos[0]][pos[1]].drawGrid() 
            
    def setupMap(self):
        self.gridsMatrix = [[Grid(self,self.sizeOfGrid,self.color,(i,j)) for i in range(self.numOfRows)] for j in range(self.numOfRows)] 
        for i in range(self.numOfRows):            
            for j in range(self.numOfRows):       
                self.gridsMatrix[i][j].drawGrid()  
                 
    def cleanMap(self):
        del self.gridsMatrix    
        
    def updateMap(self):
        self.cleanMap()
        self.setUpMap()  