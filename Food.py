from Environment import Environment
import math

class Food(Environment):

    def __init__(self,worldMap,width,height,color):
        Environment.__init__(self,worldMap,'food',width,height,color)

    def afterGotEaten(self):
        self.respawnOnMap()
