from Animat import Animat
from Actions import Actions
import qlearn_mod_random as qlearn

class Predator(Animat):
    
    def __init__(self,worldMap,scopeDist,width,height,color):
        Animat.__init__(self,worldMap,'predator',width,height,color)
        self.ai = qlearn.QLearn(actions=range(Actions.directions),alpha=0.1, gamma=0.9, epsilon=0.1)
        self.setObjectAt(self,self.posOnMap):
     
    # we assume predator's sensor would not be blocked by obstacles
    def getPreysWithinScope(self):
        preysWithinScope = []
        gridsWithinScope = self.getGridsWithinScope()
        for grid in gridsWithinScope:
            if self.worldMap.hasObjectAt(grid,'prey'):
                preysWithinScope.append(grid)
                
        return preysWithinScope
    
    def hasPreysWithinScope(self):
        preysWithinScope = self.getPreysWithinScope()
        if preysWithinScope:
            return True
        else:
            return False
    
    def isEatingPrey(self):
        return self.isObjectAt(self.posOnMap,'prey')
         
    def update(self):
        state = self.calculateState()
        reward = -1
        
        #Check if the animat has been eaten by any of the predators
        if self.posOnMap in self.prevPositions:
            reward += -20
        elif self.hasPreysWithinScope():
            reward = 20                     
        if(self.isEatingPrey()):
            #PreyAdult re-spawns itself randomly, if it gets eaten
            self.fed += 1
            reward = 50            
                
        if(self.lastState is not None):
            self.ai.learn(self.lastState,self.lastAction,reward,state)
            
        state = self.calculateState()
        action = self.ai.chooseAction(state)
        self.lastState = state
        self.lastAction = action            
        self.setPrevious2Positions() #?????????????
        self.performAction(action)   #?????????????
        self.updateOnMap()   #?????????????
    
    def calculateState(self):   #???????????????
        def stateValueForGridWithinScope(gridWithinScope):
            if self.isPosOnPrey(gridWithinScope):
                return 3
            elif self.isPosOnFood(gridWithinScope):
                return 2
            elif self.isPosOnObstacle(gridWithinScope):
                return 1
            else:
                return 0
        
        return tuple([stateValueForGridsWithinScope(gridWithinScope) for gridWithinScope in self.getGridsWithinScope()])    
    
    #TODO: Requires massive change for multiple Predators
    def move(self, offset):
        originPos = self.posOnMap
        nextPos = (self.posOnMap[0]+offset[0],self.posOnMap[1]+offset[1])

        # we don't want to move onto another predator
        if self.isPosValid(nextPos):
            self.removeObjectAt(originPos)
            self.setObjectAt(nextPos):
            Animat.move(nextPos)
            #TODO: update map -> grid