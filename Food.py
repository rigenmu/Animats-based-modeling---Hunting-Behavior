from Environment import Environment
import math

class Food(Environment):

    def __init__(self,worldMap,scopeDist,width,height,color):
        Environment.__init__(self,worldMap,'food',width,height,color)
        self.scopeDist = scopeDist

    def afterGotEaten(self):
        self.respawnOnMap()
