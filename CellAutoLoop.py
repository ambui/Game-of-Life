import pygame,time


#initialize Parameters
pygame.init()
pygame.display.set_caption("Cellular Automata")



# 90*90 Grid
size = [900, 900]
screen = pygame.display.set_mode(size)
# size of square 
width = 10
height = 10

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# background color
screen.fill(BLACK)

#create 2d-list, Holds data for location of pixels
gridArray = []
tempArray = []
for i in range(90): #row
    for j in range(90): #col
        tempArray.append(0)
    gridArray.append(tempArray)
    tempArray = []

gridWidth = len(gridArray)

# random expolsion
gridArray[44][1] = 1
gridArray[45][1] = 1
gridArray[46][1] = 1
gridArray[45][0] = 1
gridArray[44][2] = 1

# glider
# gridArray[44][44] = 1
# gridArray[45][45] = 1
# gridArray[46][45] = 1
# gridArray[46][44] = 1
# gridArray[46][43] = 1

#function translates list->screen
def drawPixel(row,col,color):
    row = row*10
    col = col*10
    pygame.draw.rect(screen,color, [col,row, width, height])


# find which pixels should be birthed or killed
# and draw
def gol(array):
    
    deathMark = []
    birthMark = []
    
    for i in range(gridWidth):  #row
        for j in range(gridWidth):  #col
            pix = array[i][j]
            
            if (pix == 0):
                pixBearth = birthCheck(i,j)
                if len(pixBearth) > 1:
                    birthMark.append(pixBearth)
                
            elif (pix == 1):
                pixDeath = popCheck(i,j)
                if len(pixDeath) > 1:
                    deathMark.append(pixDeath)

    for i in range(len(birthMark)):
        row = birthMark[i][0]
        col = birthMark[i][1]
        gridArray[row][col] = 1
        #print("birth coor " + str(birthMark[i]))

    for i in range(len(deathMark)):
        row = deathMark[i][0]
        col = deathMark[i][1]
        gridArray[row][col] = 0
        #print(deathMark[i])
    
# check neighbor pixels
# return coordinates where pixel should be birthed
def birthCheck(row,col):

    birthPix = []
        
    liveNeighbors = checkNeighbors(row,col)
    #check if birth
    if (liveNeighbors == 3):
        birthPix = [row,col]

    return birthPix

#check neighbors
#return coordinates of kill, if necessary
def popCheck(row,col):
    deathPix = []

    liveNeighbors = checkNeighbors(row,col)
            
    #check if death
    if (liveNeighbors == 0 or liveNeighbors == 1):
        deathPix = [row,col]
        #print("die 0/1")
    elif (liveNeighbors > 3):
        deathPix = [row,col]
        #print("die 4+")

    return deathPix

#check neighbor of pixel
def checkNeighbors(row,col):


    liveNeighbors = 0
    # top row - loop check
    topRow = row - 1
    if topRow < 0:
        topRow = 89

    # bot row - loop check
    botRow = row + 1
    if botRow > 89:
        botRow = 0

    # left col - loop checl
    leftCol = col - 1
    if leftCol < 0:
        leftCol = 89

    rCol = col + 1
    if rCol > 89:
        rCol = 0

    try:
        #top left
        check = gridArray[topRow][leftCol]
        if (check == 1):
            liveNeighbors += 1

        #top middle
        check = gridArray[topRow][col]
        if (check == 1):
            liveNeighbors += 1

        #top right
        check = gridArray[topRow][rCol]
        if (check == 1):
            liveNeighbors += 1

        #same left
        check = gridArray[row][leftCol]
        if (check == 1):
            liveNeighbors += 1

        #same right
        check = gridArray[row][rCol]
        if (check == 1):
            liveNeighbors += 1

        #bottom left
        check = gridArray[botRow][leftCol]
        if (check == 1):
            liveNeighbors += 1

        #bottom mid
        check = gridArray[botRow][col]
        if (check == 1):
            liveNeighbors += 1

        #bottom right
        check = gridArray[botRow][rCol]
        if (check == 1):
            liveNeighbors += 1
    except:
        pass

    return liveNeighbors

def main():

    pygame.mixer.music.load("1.mid")
    pygame.event.wait()


    while True:
        # close button listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)

        #draw from data in list
        for i in range(gridWidth):
            for j in range(gridWidth):
                pixCheck = gridArray[i][j]
                if (pixCheck == 1):
                    drawPixel(i,j,GREEN)

        #algorithm for next gen
        gol(gridArray)

        #update
        pygame.display.flip()
        clock.tick(5)


main()