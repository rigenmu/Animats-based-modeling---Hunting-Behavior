from BasicObject import BasicObject

class Environment(BasicObject):  

    def __init__(self,worldMap,name,width,height,color):
        BasicObject.__init__(self,worldMap,name,width,height,color)       

        #Already initialized at a random position by superclass
        self.reward = 0  
        
    @property
    def reward(self):
        return self._reward

    @reward.setter
    def reward(self,value):
        self._reward = value
                