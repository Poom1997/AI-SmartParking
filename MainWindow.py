import pygame

window = pygame.display.set_mode((750,750))
pygame.display.set_caption("Smart Parking")
block = 20
WHITE = (255,255,255)
RED = (255,0,0)
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
                self.grid[i].append(0)

        


    def drawMap(self):
        
        for i in range(self.row):
            for j in range(self.column):
                self.color = WHITE
                if i == 0 or i == self.row-1 or j == 0 or j == self.column-1:
                    #print("i = ",i, " j = ",j) 
                    self.color = RED
                pygame.draw.rect(window,self.color,
                                 [(margin + block) * i + margin,
                                  (margin + block) * j + margin,
                                   block, block])
        pygame.display.flip()

    def clickBox(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (block + margin)
                    row = pos[1] // (block + margin)
                    self.grid[row][column] = 1
                    print("CLICK at position: ",pos, "Grid Coordinates: ", row, column)
                    print(self.grid)

    def display(self):

        pygame.display.update()
                
        
                
            

MainWindow()
