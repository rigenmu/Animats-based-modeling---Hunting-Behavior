import pygame
from Map import Map
from Grid import Grid
# from Food import Food
from Obstacle import Obstacle
# from Predator import Predator
# from Prey import Prey

BlACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (153, 76, 0)
ORANGE = (255, 102, 0)

pygame.init()
pygame.display.set_caption("Welcome to the 77th Hunger Game!")
clock = pygame.time.Clock()

# map size: numOfGridsInARow * numOfGridsInARow grids
numOfGridsInARow = 30
sizeOfGrid = 20
sizeOfScreen = numOfGridsInARow * sizeOfGrid
screen = pygame.display.set_mode((numOfGridsInARow * sizeOfGrid,numOfGridsInARow * sizeOfGrid))

numOfPreys = 5
numOfPredators = 3
numOfObstacles = 10
numOfFood = 10

worldMap = Map(numOfGridsInARow,sizeOfGrid,WHITE,screen,pygame)

# fixed item should be placed first, since our grid is implemented in a stack manner
[Obstacle(worldMap,3,1,BROWN) for i in range(numOfObstacles)]
[Food(worldMap,1,1,GREEN) for i in range(numOfFood)]
[Predator(worldMap,3,1,1,RED) for i in range(numOfPredators)]
[Prey(worldMap,2,1,1,YELLOW) for i in range(numOfPreys)]

done = False
def worldUpdate():
    worldMap.setupMap()
    
    # replenish food if running out
    # or update every food state
    
    # update every obstacle state
    
    # update every predator
    
    # update every prey
    
    if showDisplay:
        pygame.display.update()
        clock.tick(10)
        
i = 0
while not done and i < 50000:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    worldUpdate()
    
    if i % 10000 == 0:
        for every prey:
            print data
    
    i = i + 1

pygame.quit()
