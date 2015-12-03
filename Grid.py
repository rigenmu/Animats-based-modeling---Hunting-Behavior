class Grid(object):

    def __init__(self,worldMap,size,color,pos):
        self.worldMap = worldMap
        self.size = size
        self.color = color
        self.posOnMap = pos # (x,y)                                                                     
        # dictionary objectsIdx stores the object name and its corresponding index in list objects
        self.objectsIdx = dict()
        # list objects stores the actual object in a stack manner, so we can always draw the object on top
        self.objects = []
        # TODO: see if foodIntensity can be part of objects
        # no food but can have food intensity
        self.foodIntensity = 0
    
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
    def objectsIdx(self):
        return self._objectsIdx
    
    @objectsIdx.setter
    def objectsIdx(self,value):
        self._objectsIdx = value
                
    @property
    def objects(self):
        return self._objects
    
    @objects.setter
    def objects(self,value):
        self._objects = value

    @property
    def foodIntensity(self):
        return self._foodIntensity
    
    @foodIntensity.setter
    def foodIntensity(self,value):
        self._foodIntensity = value
      
    def hasObject(self,objectName):
        return objectName in self._objectsIdx;
        
    def hasAnyObject(self):
        if self._objectsIdx:
            return True
        else:
            return False
             
    def drawGrid(self):
        if self.hasAnyObject():
            self._worldMap.pygame.draw.rect(self._worldMap.screen,self.objects[-1].color,(self._posOnMap[0]*self._size,self._posOnMap[1]*self._size,self._size,self.size))
        else:
            self._worldMap.pygame.draw.rect(self._worldMap.screen,self.color,(self._posOnMap[0]*self._size,self._posOnMap[1]*self._size,self._size,self.size))
        # if(self.grid.shouldDrawScreen):
    
    