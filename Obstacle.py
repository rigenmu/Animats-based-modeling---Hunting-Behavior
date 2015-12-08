from Environment import Environment
import random

class Obstacle(Environment):
      
    def __init__(self,worldMap,width,height,color):
        Environment.__init__(self,worldMap,'obstacle',width,height,color)
        self.remainArea = self.width * self.height
        
    def erode(self):
        while True:
            randX = random.randrange(self.posOnMap[0],self.posOnMap[0]+self.width)
            randY = random.randrange(self.posOnMap[1],self.posOnMap[1]+self.height)
            candidateErodePos = (randX,randY)
            if self.worldMap.hasObjectAt(candidateErodePos,'obstacle'):
                self.worldMap.removeObjectAt(candidateErodePos,'obstacle')
                self.remainArea -= 1
                break
            
        if self.remainArea <= 0:
            self.afterErode()
        
    def afterErode(self):
        self.width = random.randrange(1,4)
        self.height = random.randrange(1,4)
        self.remainArea = self.width * self.height
        self.initializeAtPos()