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
numOfGridsInARow = 8
sizeOfGrid = 20
sizeOfScreen = numOfGridsInARow * sizeOfGrid
surface = pygame.display.set_mode((numOfGridsInARow * sizeOfGrid,numOfGridsInARow * sizeOfGrid))

numOfPreys = 1
numOfPredators = 1
numOfObstacles = 0
numOfFood = 1

worldMap = Map(numOfGridsInARow,sizeOfGrid,WHITE,surface,pygame)
# fixed item should be placed first, since our grid is implemented in a stack manner
obstacles = [Obstacle(worldMap,random.randrange(1,4),random.randrange(1,4),BROWN) for i in range(numOfObstacles)]
# obstacles = [Obstacle(worldMap,3,1,BROWN) for i in range(numOfObstacles)]
foods = [Food(worldMap,3,1,1,GREEN) for i in range(numOfFood)]
predators = [Predator(worldMap,2,1,1,RED) for i in range(numOfPredators)]
preys = [Prey(worldMap,2,1,1,YELLOW) for i in range(numOfPreys)]

age = 1
learningAges = 200000
preysEaten = []
foodEaten = []
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        break

    surface.fill(WHITE)

    #update for every animat in the world
    eatP = 0
    for predator in predators:
        predator.update()
        eatP += predator.eatPreys
        if age % 10000 == 0:
            predator.eatPreys = 0

    eatF = 0
    for prey in preys:
        prey.update()
        eatF += prey.eatFood
        if age % 10000 == 0:
            prey.eatFood = 0

    if age % 10000 == 0:
        preysEaten.append(eatP)
        foodEaten.append(eatF)

    if age == learningAges:
        print "Predators eat prey:"
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(preysEaten)))
        print "Prey eat Food:"
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(foodEaten)))
        # for prey in preys:
#             print "prey Q table ----------------------------------------"
#             prey.printQTable()
#         for predator in predators:
#             print "predator Q table ----------------------------------------"
#             predator.printQTable()

    if age >= learningAges:
        worldMap.updateMap()
        clock.tick(10)

    age += 1
