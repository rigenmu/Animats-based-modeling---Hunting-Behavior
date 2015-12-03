from Environment import Environment

class Obstacle(Environment):
      
    def __init__(self,worldMap,width,height,color):
        Environment.__init__(self,worldMap,'obstacle',width,height,color)