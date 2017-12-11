import pygame
import csv

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



###########################################################################################
        
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
        with open('test_file.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            table = [[int(e) for e in r] for r in reader]

        for i in table:
            if(len(i) is not 0):
                self.grid.append(i)

                
##        self.grid = []

        
##        with open('testMat.txt.', 'r') as file_handler:
##            for item in file_handler:
##                self.grid.append(item)

                
##        for i in range(self.row):
##            self.grid.append([])
##            for j in range(self.column):
##                if i == 0 or i == self.row-1 or j == 0 or j == self.column-1:
##                    #print("i = ",i, " j = ",j) 
##                    self.grid[i].append(1)
##                else:
##                    self.grid[i].append(0)

        
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
                elif self.grid[i][j] == 4:
                    self.color = YELLOW
                pygame.draw.rect(window,self.color,
                                 [(margin + block) * j + margin,
                                  (margin + block) * i + margin,
                                   block, block])

        green_button = pygame.draw.rect(window,GREEN,(550,50,50,50))
        blue_button = pygame.draw.rect(window,BLUE,(610,50,50,50))
        red_button = pygame.draw.rect(window,RED,(550,110,50,50))
        white_button = pygame.draw.rect(window,WHITE,(610,110,50,50))
        green_button3 = pygame.draw.rect(window,GREEN,(550,170,50,50))
        blue_button3 = pygame.draw.rect(window,BLUE,(610,170,50,50))
        yellow_button1 = pygame.draw.rect(window,YELLOW,(550,230,50,50))
        yellow_button2 = pygame.draw.rect(window,YELLOW,(610,230,50,50))
        start_button = pygame.draw.rect(window,WHITE,(550,290,110,50))
        

        pygame.display.flip()
        
    def createCar(self):
        print("Hello")
        self.car1 = pygame.draw.rect(window,BLACK,[(margin+block)*1 + margin, (margin+block)*24 + margin, block, block])
        pygame.display.flip()

    def clickJa(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (block + margin)
                    row = pos[1] // (block + margin)
                    if 550+110 > pos[0] > 550 and 290+50 > pos[1] > 290:
                        #print("move down")
                        #self.moveDown()
                        self.moveToCoordinate()
                    elif self.grid[row][column] == 4:
                        print("Goto Exit")
##                    elif 610+50 > pos[0] > 610 and 170+50 > pos[1] > 170:
##                        print("move right")
##                        self.moveRight()
##                    if 550+50 > pos[0] > 550 and 110+50 > pos[1] > 110:
##                        print("move up")
##                        self.moveUp()
##                    elif 610+50 > pos[0] > 610 and 110+50 > pos[1] > 110:
##                        print("move left")
##                        self.moveLeft()

##    def GoToExit(self):
##        self.blockX = self.startUnit[1]
##        self.blockY = self.startUnit[0]
##        self.coX1 = (margin+block)* self.blockX + margin
##        self.coY1 = (margin+block)* self.blockY + margin
##        self.coX2 = self.coX1 + block
##        self.coY2 = self.coY1 + block
##        while not self.done:
##            for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                    done = True
##                elif event.type == pygame.MOUSEBUTTONDOWN:
##                    pos = pygame.mouse.get_pos()
##                    print(pos)
##                    if self.coX2 > pos[1] > self.coX1 and self.coY2 > pos[0] > self.coY1:
##                        print("Time to leave the station")

                        
    def moveController(self):   
        self.car1.move_ip(0,1)
        self.drawMap()    
        self.car1 = pygame.draw.rect(window,BLACK,self.car1)

        pygame.display.flip()

    def changeMatrix(self):
        self.newX = self.startUnit[1]
        self.newY = self.startUnit[0]
        self.grid[self.newX][self.newY] = 4
        self.drawMap()
        #self.GoToExit()
        
        
    def moveToCoordinate(self):
        self.startUnit = (24,1)
        self.testUnit = [(24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (22, 9), (21, 9), (20, 9), (19, 9), (18, 9), (17, 9), (16, 9), (15, 9), (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11), (20, 11), (21, 11), (22, 11), (23, 11), (23, 12), (23, 13), (22, 13), (21, 13), (20, 13), (19, 13), (18, 13), (17, 13), (16, 13), (15, 13), (14, 13), (13, 13), (12, 13), (11, 13), (10, 13), (9, 13), (8, 13), (7, 13), (6, 13), (5, 13), (4, 13), (3, 13), (2, 13), (1, 13), (1, 14), (1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15), (23, 16), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17), (18, 17), (17, 17), (16, 17), (15, 17), (14, 17), (13, 17), (12, 17), (11, 17), (10, 17), (9, 17), (8, 17), (7, 17), (6, 17), (5, 17), (4, 17), (3, 17), (2, 17), (1, 17), (1, 18), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (12, 19), (13, 19), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19), (19, 19), (20, 19), (21, 19), (22, 19), (23, 19), (23, 20), (23, 21), (22, 21), (21, 21), (20, 21), (19, 21), (18, 21), (17, 21), (16, 21), (15, 21), (14, 21), (13, 21), (12, 21), (11, 21), (10, 21), (9, 21), (8, 21), (7, 21), (6, 21), (5, 21), (4, 21), (3, 21), (2, 21), (1, 21), (1, 22), (1, 23), (2, 23), (3, 23), (4, 23), (5, 23), (6, 23), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23), (13, 23), (14, 23), (15, 23), (16, 23), (17, 23), (18, 23), (19, 23), (20, 23), (21, 23), (22, 23), (23, 23), (24, 23)]
        self.length = len(self.testUnit)
        for i in range(self.length):
            if self.startUnit[1] < self.testUnit[i][1]:
                print("right")
                self.moveRight()
                self.startUnit = self.testUnit[i]
                
            elif self.startUnit[1] > self.testUnit[i][1]:
                print("left")
                self.moveLeft()
                self.startUnit = self.testUnit[i]

            elif self.startUnit[0] < self.testUnit[i][0]:
                print("down")               
                self.moveDown()
                self.startUnit = self.testUnit[i]
                
            elif self.startUnit[0] > self.testUnit[i][0]:
                print("up")
                self.moveUp()
                self.startUnit = self.testUnit[i]
        self.changeMatrix()


        
                
        
        
        
        
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
