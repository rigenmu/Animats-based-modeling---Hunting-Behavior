class Grid(object):

    def __init__(self,worldMap,size,color,pos):
        self.worldMap = worldMap
        self.size = size
        self.color = color
        self.posOnMap = pos # (x,y)                                                                     
        # dictionary objectsIdx stores the object name and its corresponding object
        self.objectsDict = dict()
        # list objects shows the comming order of the object, so we can always draw the object on top
        self.objects = []
    
    @property
    def worldMap(self):
        return self._worldMap

    @worldMap.setter
    def worldMap(self,value):
        self._worldMap = value
        
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,value):
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color = value
    
    @property
    def posOnMap(self):
        return self._posOnMap
    
    @posOnMap.setter
    def posOnMap(self,value):
        self._posOnMap = value

    @property
    def objectsDict(self):
        return self._objectsDict
    
    @objectsDict.setter
    def objectsDict(self,value):
        self._objectsDict = value
                
    @property
    def objects(self):
        return self._objects
    
    @objects.setter
    def objects(self,value):
        self._objects = value
      
    def hasObject(self,objectName):
        return objectName in self.objectsDict;
        
    def hasAnyObject(self):
        if self.objectsDict:
            return True
        else:
            return False
             
    def drawGrid(self):
        if self.hasAnyObject():
            self.worldMap.pygame.draw.rect(self.worldMap.surface,self.objects[-1].color,(self.posOnMap[0]*self.size,self.posOnMap[1]*self.size,self.size,self.size))
        else:
            self.worldMap.pygame.draw.rect(self.worldMap.surface,self.color,(self.posOnMap[0]*self.size,self.posOnMap[1]*self.size,self.size,self.size))
    
    def drawGridWithColor(self,color):
        self.worldMap.pygame.draw.rect(self.worldMap.surface,color,(self.posOnMap[0]*self.size,self.posOnMap[1]*self.size,self.size,self.size))
        
        