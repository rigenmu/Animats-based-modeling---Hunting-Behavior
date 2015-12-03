from Animat import Animat
from Actions import Actions
import qlearn_mod_random as qlearn

class Prey(Animat):
    
    def __init__(self,worldMap,scopeDist,width,height,color):
        Animat.__init__(self,worldMap,width,height,color)
        self.scope = scopeDist  
        self.ai = qlearn.QLearn(actions=range(Actions.directions),alpha=0.1, gamma=0.9, epsilon=0.1)
        self.eaten = 0      
    
    # we assume preys only have visual sensor
    # and visual scope would be blocked by obstacles
    def getGridsWithinVisualScope(self):
        gridsWithinVisualScope = []
        
        gridsWithinScope = getGridsWithinScope(self.scope)
        candidateGridsWithinVisualScope = []
        obstaclesWithinScope = []

        # split grids within scope into obstacles and non-obstacles
        for grid in gridsWithinScope:
            if self.worldMap.hasObjectAt(grid,'obstacle'):
                obstaclesWithinScope.append(grid)
            else:
                candidateGridsWithinVisualScope.append(grid)
                
        for candidate in candidateGridsWithinVisualScope:
            blocked = False
            for obstacle in obstaclesWithinScope:
                if self.isGridBlockedByObstacle(candidate,obstacle):
                    blocked = True
                    break
            if not blocked:
                gridsWithinVisualScope.append(candidate)
        
        # for neighbor in positionsOfNeighborGrids:
       #      cell = self.grid.cellMatrix[neighbor[0]][neighbor[1]]
       #      self.grid.pygame.draw.rect(self.grid.screen,(0, 0, 255),(cell.x,cell.y,cell.width,cell.height))
       #
            
    def getPredatorsWithinVisualScope(self):
        predatorsWithinScope = []
        
        gridsWithinVisualScope = self.getGridsWithinVisualScope()
        for grid in gridsWithinVisualScope:
            if self.worldMap.hasObjectAt(grid,'predator'):
                predatorsWithinScope.append(grid)
                
        return predatorsWithinScope

    def hasPredatorsWithinVisualScope(self):
        predatorsWithinScope = self.getPredatorsWithinVisualScope()
        
        if predatorsWithinScope:
            return True
        else:
            return False
     
    def isBeingEatenByPredator(self):
        return self.isObjectAt(self.posOnMap,'predator'):
    
    def isEatingFood(self):
        return self.isObjectAt(self.posOnMap,'food')
                                  
    def update(self):
        return
        #Override this for all subclasses
#         state = self.calculateState()
#         reward = -20
#         
#         #Check if the animat is on a food Intensity gradient                
#         if(self.rewardForProximityToFood()):
#             reward +=  -1*(1 - self.rewardForProximityToFood())
#             
#         if(self.hasPredatorInNeighborhood()):
#             reward += -40
#             
#         if (self.gridX,self.gridY) in self.previousPositionTuples:
#             reward += -20
#             
#         #Check if the animat has been eaten by any of the predators        
#         if(self.isBeingEatenByPredator()):
#             self.eaten += 1
#             reward = -200
#             if self.lastState is not None:
#                 self.ai.learn(self.lastState,self.lastAction,reward,state)
#                 
#             #Since the prey will be re-spawned, reset the last state
#             self.lastState = None
#             self.respawnAtRandomPosition()
#             return
#         
#         if(self.isEatingFood()):
#             #Remove the food being eaten
#             eatenFood = Food.dictionaryOfFoodObjects.pop((self.gridX,self.gridY))
#             eatenFood.gotEaten()
#             eatenFoodCell = self.grid.cellMatrix[eatenFood.gridX][eatenFood.gridY]
#             eatenFoodCell.foodIntensity = 0
#             eatenFood = None
#             self.fed += 1
#             reward += 100
#         
#         #Reward for being in between offspring and predator
#         reward += self.rewardForProtection()            
#             
#         if(self.lastState is not None):
#             self.ai.learn(self.lastState,self.lastAction,reward,state)
#             
#         state = self.calculateState()
#         action = self.ai.chooseAction(state)
#         self.lastState = state
#         self.lastAction = action
#         self.setPrevious2Positions()
#         self.performAction(action)
#         self.drawGameObjectAtCurrentPosition()    
    
    def calculateState(self):
        def stateValueForGridWithinvisualScope(gridWithinVisualScope):
            currentGridState = ()
            if self.isPosOnPredator(gridWithinVisualScope):
                currentGridState += (4,)
            if self.isPosOnFood(gridWithinVisualScope):
                currentGridState += (3,)
            if self.isPosOnObstacle(gridWithinVisualScope):
                currentGridState = (2,)                        
            if self.isPosIdle(gridWithinVisualScope):
                currentGridState = (0,)
                
            if self.getPosFoodIntensity(gridWithinVisualScope) > 0:
                currentGridState += (self.getPosFoodIntensity(gridWithinVisualScope),)
                
            return currentGridState
            
        return tuple([stateValueForGridWithinvisualScope(gridWithinVisualScope) for gridWithinVisualScope in self.getGridsWithinVisualScope()])
            
    def move(self, offset):
        originPos = self.posOnMap
        nextPos = (self.posOnMap[0]+offset[0], self.posOnMap[1]+offset[1])
        
        if self.isPosValid(nextPos):
            self.removeObjectAt(originPos)
            self.setObjectAt(nextPos)
            Animat.move(nextPos)

#         oldXPosition = self.gridX
#         oldYPosition = self.gridY        
#         nextXPosition = self.gridX + directionX
#         nextYPosition = self.gridY + directionY
#         if(self.isMovementPossible(nextXPosition, nextYPosition)):
#             #If prey is in new position     
#             if(not Prey.dictionaryOfPrey.has_key((nextXPosition,nextYPosition))):
#                 #Another Prey is not on the next Position, so valid movement
#                 Animat.move(self, directionX, directionY)
#                 Prey.dictionaryOfPrey.pop((oldXPosition,oldYPosition))
#                 Prey.dictionaryOfPrey[(self.gridX,self.gridY)] = self;
        
    def respawnAtRandPos(self):
        #Override for subclass
        return
#         oldXPosition = self.gridX
#         oldYPosition = self.gridY
#         
#         randomX = random.randrange(0,self.grid.numberOfColumns)
#         randomY = random.randrange(0,self.grid.numberOfRows)
#         self.setXYPosition(randomX, randomY)
#                 
#         Prey.dictionaryOfPrey.pop((oldXPosition,oldYPosition))
#         while Prey.dictionaryOfPrey.has_key((self.gridX,self.gridY)):
#             randomX = random.randrange(0,self.grid.numberOfColumns)
#             randomY = random.randrange(0,self.grid.numberOfRows)
#             self.setXYPosition(randomX, randomY)
#         Prey.dictionaryOfPrey[(self.gridX,self.gridY)] = self        
        
    def rewardForProximityToFood(self):              
        return self.getPosFoodIntensity(self.posOnMap)
   
    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2
     
    def onSegment(self, p, q, r):
        if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
            return True
        return False
     
    def isIntersect(self,p1,q1,p2,q2):
        
        if p1 == p2 or q1 == q2:
            return False
            
        o1 = self.orientation(p1,q1,p2)
        o2 = self.orientation(p1,q1,q2)
        o3 = self.orientation(p2,q2,p1)
        o4 = self.orientation(p2,q2,q1)
        
        if o1 != o2 and o3 != o4:
            return True
        else:
            return False
    
       
    def isGridBlockedByObstacle(self,grid,obstacle):
        """judge if cur_pos-self line intersect with obstacle line"""
        p1 = self.posOnMap
        q1 = grid
        p2 = obstacle
        q2 = (obstacle[0]+1, obstacle[1])
        p3 = obstacle
        q3 = (obstacle[0], obstacle[1]+1)
        
        if self.isIntersect(p1,q1,p2,q2) or self.isIntersect(p1,q1,p3,q3):
            return True
        else:
            return False
        # if o1 == 0 and self.onSegment(p1,p2,q1):
        #     return True
        # if o2 == 0 and self.onSegment(p1,q2,q1):
        #     return True
        # if o3 == 0 and self.onSegment(p2,p1,q2):
        #     return True
        # if o4 == 0 and self.onSegment(p2,q1,q2):
        #     return True