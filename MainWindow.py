import pygame

window = pygame.display.set_mode((685,600))
pygame.display.set_caption("Smart Parking")
block = 20
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,225)
GREEN = (0,255,0)
margin = 1
clock = pygame.time.Clock()
clock.tick(80)




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
        self.modeSelect()
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
                
        for a in range(self.row):
            for b in range(self.column):
                if self.grid[a][b] == 1:
                    pass
                   # print(a," and ",b)


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
                elif self.grid[i][j] == 2:
                    self.color = GREEN
                elif self.grid[i][j] == 3:
                    self.color = BLUE
                pygame.draw.rect(window,self.color,
                                 [(margin + block) * j + margin,
                                  (margin + block) * i + margin,
                                   block, block])

        green_button = pygame.draw.rect(window,GREEN,(550,50,50,50))
        blue_button = pygame.draw.rect(window,BLUE,(610,50,50,50))
        red_button = pygame.draw.rect(window,RED,(550,110,50,50))
        bwhite_button = pygame.draw.rect(window,WHITE,(610,110,50,50))
        green_button3 = pygame.draw.rect(window,GREEN,(550,170,50,50))
        blue_button3 = pygame.draw.rect(window,BLUE,(610,170,50,50))

        
        pygame.display.flip()
##
##    def greenButtonClicked(self):
##        mouse = pygame.mouse,get_pos()
##        if 550+50 > mouse[0] > 550 and 50+50 > mouse[1] > 50:

    def modeSelect(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 550+50 > pos[0] > 550 and 170+50 > pos[1] > 170:
                        print("Go to ClickBox")
                        self.clickBox()
                    elif 610+50 > pos[0] > 610 and 170+50 > pos[1] > 170:
                        print("Go to Simulate")
                        self.simulate()

    def simulate(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 550+50 > pos[0] > 550 and 170+50 > pos[1] > 170:
                        print("Go to ClickBox")
                        self.clickBox()
                    else:
                        pass
                        
            
        
            

    def clickBox(self):
        self.toggleNum = 1
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= 525 and pos[1] <= 525:
                        column = pos[0] // (block + margin)
                        row = pos[1] // (block + margin)
                        self.grid[row][column] = self.toggleNum
                        #print("Grid Coordinates: ", row, column, 'value: ',self.grid[row][column])
                        self.drawMap()
                        self.getParking()
                        #self.changeColor()
                    elif 610+50 > pos[0] > 610 and 110+50 > pos[1] > 110:
                        self.toggleNum = 0
                        print("White ja")
                    elif 550+50 > pos[0] > 550 and 110+50 > pos[1] > 110:
                        self.toggleNum = 1
                        print("Red ja")
                    elif 550+50 > pos[0] > 550 and 50+50 > pos[1] > 50:
                        self.toggleNum = 2
                        print("Green ja")
                    elif 610+50 > pos[0] > 610 and 50+50 > pos[1] > 50:
                        self.toggleNum = 3
                        print("Blue ja")
                    elif 550+50 > pos[0] > 550 and 170+50 > pos[1] > 170:
                        print("Go to ClickBox")
                        self.clickBox()
                    elif 610+50 > pos[0] > 610 and 170+50 > pos[1] > 170:
                        print("Go to Simulate")
                        self.simulate()

                    else:
                        print("Out of bound")

        
    def getMatrix(self):
        return self.grid

    def getParking(self):
        self.lstOfPark = []
        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j] == 2 or self.grid[i][j] == 3:
                    self.lstOfPark.append(self.grid[i][j])

        return self.lstOfPark
                    

    
    def display(self):

        pygame.display.update()
                
        
class Car():
    def __init__(self):
        pygame.init()
        self.x = 0
        self.y = 0
        self.row = 25
        self.column = 25
        self.done = False
        self.carNum = 0
        self.carPosX = 0
        self.carPosY = 0
        self.initPosX = 0
        self.initPosY = 0
        self.parkingMap()
        self.drawMap()
        self.createCar()
        self.clickJa()

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
                elif self.grid[i][j] == 2:
                    self.color = GREEN
                elif self.grid[i][j] == 3:
                    self.color = BLUE
                pygame.draw.rect(window,self.color,
                                 [(margin + block) * j + margin,
                                  (margin + block) * i + margin,
                                   block, block])

        green_button = pygame.draw.rect(window,GREEN,(550,50,50,50))
        blue_button = pygame.draw.rect(window,BLUE,(610,50,50,50))
        red_button = pygame.draw.rect(window,RED,(550,110,50,50))
        bwhite_button = pygame.draw.rect(window,WHITE,(610,110,50,50))
        green_button3 = pygame.draw.rect(window,GREEN,(550,170,50,50))
        blue_button3 = pygame.draw.rect(window,BLUE,(610,170,50,50))

        
        pygame.display.flip()
    def createCar(self):
        print("Hello")
        self.grid[10][10] = 5
        self.car1 = pygame.draw.rect(window,BLACK,[(margin+block)*1 + margin, (margin+block)*1 + margin, block, block])
        pygame.display.flip()

    def clickJa(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 550+50 > pos[0] > 550 and 170+50 > pos[1] > 170:
                        #print("move down")
                        #self.moveDown()
                        self.moveToCoordinate()
##                    elif 610+50 > pos[0] > 610 and 170+50 > pos[1] > 170:
##                        print("move right")
##                        self.moveRight()
##                    if 550+50 > pos[0] > 550 and 110+50 > pos[1] > 110:
##                        print("move up")
##                        self.moveUp()
##                    elif 610+50 > pos[0] > 610 and 110+50 > pos[1] > 110:
##                        print("move left")
##                        self.moveLeft()

                        
    def moveController(self):
        self.car1.move_ip(0,1)
        self.drawMap()
        self.car1 = pygame.draw.rect(window,BLACK,self.car1)

        pygame.display.flip()

    def moveToCoordinate(self):
        self.startUnit = (1,1)
        self.testUnit = [(1,2), (1,3), (1,4), (2,4), (2,5), (3,5), (3,6),(4,6), (4,7), (4,8), (3,8), (3,9)]
        self.length = len(self.testUnit)
        for i in range(self.length):
            if self.startUnit[0] < self.testUnit[i][0]:
                print("right")
                self.moveRight()
                self.startUnit = self.testUnit[i]
                
            elif self.startUnit[0] > self.testUnit[i][0]:
                print("left")
                self.moveLeft()
                self.startUnit = self.testUnit[i]

            elif self.startUnit[1] < self.testUnit[i][1]:
                print("down")               
                self.moveDown()
                self.startUnit = self.testUnit[i]
                
            elif self.startUnit[1] > self.testUnit[i][1]:
                print("up")
                self.moveUp()
                self.startUnit = self.testUnit[i]
                
            
        
        
        
        
    def initializer(self):
        MainWindow.__init__(self)

    def moveLeft(self):
        for i in range(21):
            self.car1.move_ip(-1,0)
            self.drawMap()
            self.car1 = pygame.draw.rect(window,BLACK,self.car1)
            
            pygame.display.flip()
            pygame.time.wait(10)

    def moveRight(self):
        for i in range(21):
            self.car1.move_ip(1,0)
            self.drawMap()
            self.car1 = pygame.draw.rect(window,BLACK,self.car1)

            pygame.display.flip()
            pygame.time.wait(10)
            

    def moveUp(self):
        for i in range(21):
            self.car1.move_ip(0,-1)
            self.drawMap()
            self.car1 = pygame.draw.rect(window,BLACK,self.car1)

            pygame.display.flip()
            pygame.time.wait(10)

    def moveDown(self):
        for i in range(21):
            self.car1.move_ip(0,1)
            self.drawMap()
            self.car1 = pygame.draw.rect(window,BLACK,self.car1)

            pygame.display.flip()
            pygame.time.wait(10)

    def park(self):
        #Car stop at the coordinate and stay there
        pass

    def move(self):
        #get the move path for the car
        pass
            

Car()
