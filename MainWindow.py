import pygame

window = pygame.display.set_mode((685,600))
pygame.display.set_caption("Smart Parking")
block = 20
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,225)
GREEN = (0,255,0)
margin = 1
clock = pygame.time.Clock()
clock.tick(60)




class MainWindow():
    def __init__(self):
        pygame.init()
        self.x = 0
        self.y = 0
        self.row = 25
        self.column = 25
        self.done = False
        self.parkingMap()
        self.drawMap()
        self.clickBox()
        self.display()

    def parkingMap(self):
        self.grid = []
        for i in range(self.row):
            self.grid.append([])
            for j in range(self.column):
                if i == 0 or i == self.row-1 or j == 0 or j == self.column-1:
                    #print("i = ",i, " j = ",j) 
                    self.grid[i].append(1)
                else:
                    self.grid[i].append(0)
                

        print(self.grid)

        for a in range(self.row):
            for b in range(self.column):
                if self.grid[a][b] == 1:
                    print(a," and ",b)

        


    def drawMap(self):
        for i in range(self.row):
            for j in range(self.column):
                self.color = WHITE
                if self.grid[i][j] == 1:
                    pass
                    #print(i," and ",j)
                if self.grid[i][j] == 1:
                    #print("i = ",i, " j = ",j) 
                    self.color = RED
                pygame.draw.rect(window,self.color,
                                 [(margin + block) * i + margin,
                                  (margin + block) * j + margin,
                                   block, block])

        green_button = pygame.draw.rect(window,GREEN,(550,50,50,50))
        blue_button = pygame.draw.rect(window,BLUE,(610,50,50,50))
        green_button2 = pygame.draw.rect(window,GREEN,(550,110,50,50))
        blue_button2 = pygame.draw.rect(window,BLUE,(610,110,50,50))
        green_button3 = pygame.draw.rect(window,GREEN,(550,170,50,50))
        blue_button3 = pygame.draw.rect(window,BLUE,(610,170,50,50))

        
        pygame.display.flip()

    def clickBox(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= 525 and pos[1] <= 525:
                        column = pos[0] // (block + margin)
                        row = pos[1] // (block + margin)
                        self.grid[row][column] = 1
                        #print("CLICK at position: ",pos, "Grid Coordinates: ", row, column)
                        self.changeColor()
                    else:
                        print("Out of bound")


    def changeColor(self):
        self.color = RED
        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j] == 1:
                    #print(i,"and",j)
                    pygame.draw.rect(window,RED,
                                     [(margin + block) * i + margin,
                                      (margin + block) * j + margin,
                                       block, block])
        
    def getMatrix(self):
        return self.grid

    
    def display(self):

        pygame.display.update()
                
        
                
            

MainWindow()
