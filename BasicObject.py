import random

class BasicObject():
    def __init__(self,worldMap,name,width,height,color):
        self.worldMap = worldMap
        self.name = name
        self.width = width
        self.height = height
        self.color = color

        self.posOnMap = (0,0)
        self.initializeAtPos()

    @property
    def worldMap(self):
        return self._worldMap

    @worldMap.setter
    def worldMap(self,value):
        self._worldMap = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

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

    def initializeAtPos(self):
        self.posOnMap = self.genRandPos()
        self.setObjectAt(self.posOnMap)

    # set current object on map
    def setObjectAt(self,pos):
        for i in range(pos[0],pos[0]+self.width):
            for j in range(pos[1],pos[1]+self.height):
                self.worldMap.setObjectAt((i,j),self.name,self)

    def isWithinBoundaryAt(self,pos):
        for i in range(pos[0],pos[0]+self.width):
            for j in range(pos[1],pos[1]+self.height):
                if not self.worldMap.isPosWithinBoundary((i,j)):
                    return False
        return True

    def isAnyObjectAt(self,pos):
        for i in range(pos[0],pos[0]+self.width):
            for j in range(pos[1],pos[1]+self.height):
                if self.worldMap.hasAnyObjectAt(pos):
                    return True
        return False

    # check if current object would collide with certain object at certain position on map
    def isObjectAt(self,pos,objectName):
        for i in range(pos[0],pos[0]+self.width):
            for j in range(pos[1],pos[1]+self.height):
                if self.worldMap.hasObjectAt((i,j),objectName):
                    return True
        return False

    # we don't place an object on a position that is already been occupied by same-type object
    def isPosValid(self,pos):
        if not self.isWithinBoundaryAt(pos) or self.isObjectAt(pos,'obstacle') or self.isObjectAt(pos,self.name):
            return False
        return True

    # remove current object from map
    def removeObjectAt(self,pos):
        for i in range(pos[0],pos[0]+self.width):
            for j in range(pos[1],pos[1]+self.height):
                self.worldMap.removeObjectAt((i,j),self.name)

    # put object at a valid position on map
    def genRandPos(self):
        # ensure the whole object is within boundary
        while True:
            randX = random.randrange(0,self.worldMap.numOfRows-self.width)
            randY = random.randrange(0,self.worldMap.numOfRows-self.height)
            candidatePos = (randX,randY)
            if not self.isAnyObjectAt(candidatePos):
                return candidatePos

    def drawOnMap(self):
        for i in range(self.posOnMap[0],self.posOnMap[0]+self.width):
            for j in range(self.posOnMap[1],self.posOnMap[1]+self.height):
                self.worldMap.updateMapAt((i,j),self.color)

    def respawnOnMap(self):
        self.removeObjectAt(self.posOnMap)
        self.initializeAtPos()
