from EnvironmentObject import EnvironmentObject

class Obstacle(EnvironmentObject):
    
    #Static Variable - Class members
    dictionaryOfObstacles = dict()
        
    def __init__(self,width,height,color,grid):
        EnvironmentObject.__init__(self,width,height,color,grid)
        #Already initialized at a random position by superclass
        for i in range(0,width):
            Obstacle.dictionaryOfObstacles[(self.gridX+i,self.gridY)] = self