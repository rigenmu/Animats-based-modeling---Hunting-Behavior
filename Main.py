import pygame
import random

from Map import Map
from Obstacle import Obstacle
from Food import Food

from Predator import Predator
from Prey import Prey

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (153, 76, 0)
ORANGE = (255, 102, 0)

pygame.init()
pygame.display.set_caption("Welcome to the 77th Hunger Game!")
clock = pygame.time.Clock()

# worldMap size: numOfGridsInARow * numOfGridsInARow grids
numOfGridsInARow = 30
sizeOfGrid = 20
sizeOfScreen = numOfGridsInARow * sizeOfGrid
surface = pygame.display.set_mode((numOfGridsInARow * sizeOfGrid,numOfGridsInARow * sizeOfGrid))

numOfPreys = 5
numOfPredators = 3
numOfObstacles = 10
numOfFood = 10
      
worldMap = Map(numOfGridsInARow,sizeOfGrid,WHITE,surface,pygame)
# fixed item should be placed first, since our grid is implemented in a stack manner
# obstacles = [Obstacle(worldMap,random.randrange(0,3),random.randrange(0,3),BROWN) for i in range(numOfObstacles)]
obstacles = [Obstacle(worldMap,3,1,BROWN) for i in range(numOfObstacles)]
foods = [Food(worldMap,3,1,1,GREEN) for i in range(numOfFood)]
predators = [Predator(worldMap,3,1,1,RED) for i in range(numOfPredators)]
preys = [Prey(worldMap,2,1,1,YELLOW) for i in range(numOfPreys)]

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        break

    surface.fill(WHITE)
    worldMap.updateMap()
    #update for every object in the world
    for predator in predators:
        predator.update()
    
    for prey in preys:
        prey.update()
        
    pygame.display.update()  
    clock.tick(10) 
