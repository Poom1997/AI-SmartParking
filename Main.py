import pygame
import csv
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from DataManager import *
from System_Settings import *

class Menu:
    def __init__(self):
        self.run = True
        self.file_path = ""
        self.root = tk.Tk()
        self.root.withdraw()
        self.edit = EditMap()
        self.drawMenu()

    def drawMenu(self):
        window.blit(mainMenuPic,(0,0))
        window.blit(editButtonPic,((70,240),(350,310)))
        window.blit(simulateButtonPic,((70,360),(350,430)))
        window.blit(exitButtonPic,((525,460),(680,500)))
    

    def main_loop(self):
        #Event Handling
        while self.run:
            self.drawMenu()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                    if 350 > pos[0] > 70 and 310 > pos[1] > 240:
                        self.edit.main_loop()
                    elif 350 > pos[0] > 70 and 430 > pos[1] > 360:
                        self.file_path = filedialog.askopenfilename()
                        self.simulate = MainSimulation(self.file_path)
                        self.simulate.main_loop()
                    elif 680 > pos[0] > 525 and 500 > pos[1] > 460:
                        pygame.quit()
                        sys.exit()
                    

            pygame.display.update()
            clock.tick(80)

    

#Start Map edit Mode
class EditMap:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.x = 0
        self.y = 0
        self.row = 25
        self.column = 25
        self.run = True
        self.currentMovingNode = 0
        self.toggleNum = 0
        
        self.grid = []
        self.parkingMap()

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
                
    def saveMap(self):
        self.fileName = asksaveasfilename()
        with open(self.fileName, 'w') as csvfile:
            writer = csv.writer(csvfile)
            [writer.writerow(r) for r in self.grid]
            
    def loadMap(self):
        self.grid = []
        self.file_path = filedialog.askopenfilename()
        with open(self.file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            table = [[int(e) for e in r] for r in reader]

        for i in table:
            if(len(i) is not 0):
                self.grid.append(i)
        
            
    def drawMap(self):
        for i in range(self.row):
            for j in range(self.column):
                self.color = WHITE
                if self.grid[i][j] == 0:
                    self.color = WHITE
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

        green_button  = pygame.draw.rect(window,GREEN, (550,50,130,50))
        red_button    = pygame.draw.rect(window,RED,   (550,115,130,50))
        blue_button   = pygame.draw.rect(window,BLUE,  (550,180,130,50))
        purple_button = pygame.draw.rect(window,PURPLE,(550,245,130,50))
        white_button  = pygame.draw.rect(window,WHITE, (550,310,130,50))
        
        save_button = pygame.draw.rect(window,CYAN,(550,385,130,25))
        back_button = pygame.draw.rect(window,CYAN,(550,430,130,25))
        load_button = pygame.draw.rect(window,CYAN,(550,475,130,25))

        window.blit(panelText, (541,10))
        window.blit(parkingText, (560,60))
        window.blit(wallText,(585,123))
        window.blit(entranceText,(565,190))
        window.blit(exitText,(590,253))
        window.blit(pathText,(590,318))

        
        window.blit(saveText,(594,387))
        window.blit(loadText,(594,432))
        window.blit(backText,(595,477))
           
    def main_loop(self):
        #Event Handling
        while self.run:
            window.blit(menuPic,(0,0))
            window.fill(BLACK,((0,0),(525,525)))
            self.drawMap()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (block + margin)
                    row = pos[1] // (block + margin)
                    if pos[0] <= 525 and pos[1] <= 525:
                        self.grid[row][column] = self.toggleNum
                    elif 550+130 > pos[0] > 550 and 310+50 > pos[1] > 310:
                        self.toggleNum = 0
                        print("Path")
                    elif 550+130 > pos[0] > 550 and 115+50 > pos[1] > 115:
                        self.toggleNum = 1
                        print("Wall")
                    elif 550+130 > pos[0] > 550 and 50+50 > pos[1] > 50:
                        self.toggleNum = 2
                        print("Parking Lot")
                    elif 550+130 > pos[0] > 550 and 180+50 > pos[1] > 180:
                        self.toggleNum = 3
                        print("Entrance")
                    elif 550+130 > pos[0] > 550 and 245+50 > pos[1] > 245:
                        print("Exit")
                   
                    ## SaveButton
                    elif 550+130 > pos[0] > 550 and 385+25 > pos[1] > 385:
                        print("saveMap")
                        self.saveMap()
                    ## LoadButton
                    elif 550+130 > pos[0] > 550 and 430+25 > pos[1] > 430:
                        print("loadMap")
                        self.loadMap()
                    ## ClearButton
                    elif 550 + 130 > pos[0] > 550 and 475+25 > pos[1] > 475:
                        print('clearMap')
                        m = Menu()
                        m.main_loop()
                    else:
                        print("Out of bound")

            pygame.display.update()
            clock.tick(80)
            
#Start Simulation Mode
class MainSimulation:
    def __init__(self,filePath):
        self.file = filePath
        self.x = 0
        self.y = 0
        self.row = 25
        self.column = 25
        self.prologConnector = None
        self.run = True
        self.move = False
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.calculate = True
        self.carNum = 0
        self.carPosX = 0
        self.carPosY = 0
        self.initPosX = 0
        self.initPosY = 0
        self.xNumCoor1 = 605
        self.xNumCoor2 = 605

        self.carNo1 = 0
        self.carNo2 = 0
        self.tempColor = WHITE
        
        self.grid = []
        self.pathway = []
        
        self.carLocation = 22
        
        self.parkingMap()
        self.setup()

    def parkingMap(self):
        self.grid = []
        with open(self.file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            table = [[int(e) for e in r] for r in reader]

        for i in table:
            if(len(i) is not 0):
                self.grid.append(i)

    def setup(self):
        print("in")
        self.prologConnector = DataManager(self.row, self.column, self.grid)
        self.prologConnector.setup()

    def drawMap(self):
        self.strCarNo1 = str(self.carNo1)
        self.strCarNo2 = str(self.carNo2)
        self.carNoText1 = font3.render(self.strCarNo1,True, self.tempColor)
        self.carNoText2 = font3.render(self.strCarNo2,True, self.tempColor)
        parkingText = font1.render("Car Park",True, BLACK)
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

        decrease_button1 = pygame.draw.rect(window,WHITE,(550,50,40,70))
        increase_button1 = pygame.draw.rect(window,WHITE,(650,50,40,70))
        decrease_button2 = pygame.draw.rect(window,WHITE,(550,180,40,70))
        increase_button2 = pygame.draw.rect(window,WHITE,(650,180,40,70))
        start_button = pygame.draw.rect(window,CYAN,(550,290,140,35))
        stop_button = pygame.draw.rect(window,CYAN,(550,365,140,35))
        back_button = pygame.draw.rect(window,CYAN,(550,440,140,35))

        window.blit(carEntranceText1, (585,10))
        window.blit(carEntranceText2, (585,140))

        window.blit(decText1, (560,45))
        window.blit(incText1, (655,50))
        window.blit(decText2, (560,175))
        window.blit(incText2, (655,180))

        window.blit(self.carNoText1, (self.xNumCoor1,50))
        window.blit(self.carNoText2, (self.xNumCoor2,180))

        
        window.blit(startText, (592,290))
        window.blit(stopText, (555,365))
        window.blit(backText2, (590,440))

        


    def createCar(self):
        self.car1 = pygame.draw.rect(window,BLACK,[(margin+block)*1 + margin + self.carPosX, (margin+block)*24 + margin + self.carPosY, block+1, block+1])
        
    def moveToCoordinate(self):
        #print('here' + str(self.carLocation))
        temp = int(self.carLocation) // 21
        if(temp != len(self.pathway)):
            nextNode = self.pathway[temp]
            #print('in2')
            #print(self.carCurrentPosition[1])
            #print(nextNode[1])
            #print(self.carCurrentPosition[0])
            #print(nextNode[0])
            if(self.carCurrentPosition[1] < nextNode[1]):
               #print('Moving Right')
               self.carPosX += 2
               self.carLocation += 2
               if((self.carLocation % 21) == 0):
                   self.carCurrentPosition = nextNode
            elif(self.carCurrentPosition[1] > nextNode[1]):
               #print('Moving Left')
               self.carPosX -= 2
               self.carLocation += 2
               if((self.carLocation % 21) == 0):
                   self.carCurrentPosition = nextNode
            elif(self.carCurrentPosition[0] < nextNode[0]):
               #print('Moving Down')
               self.carPosY += 2
               self.carLocation += 2
               if((self.carLocation % 21) == 0):
                   self.carCurrentPosition = nextNode
            elif(self.carCurrentPosition[0] > nextNode[0]):
               #print('Moving Up')
               self.carPosY -= 2
               self.carLocation += 2
               if((self.carLocation % 21) == 0):
                   self.carCurrentPosition = nextNode
        else:
            self.carCurrentPosition = self.pathway[-1]
            self.changeMatrix()
            self.move = False
            self.calculate = True
            self.carPosX = 0
            self.carPosY = 0
            self.carLocation = 22
           
    def changeMatrix(self):
        self.newX = self.carCurrentPosition[0]
        self.newY = self.carCurrentPosition[1]
        #print(self.newX)
        #print(self.newY)
        #print(self.carCurrentPosition)
        self.grid[self.newX][self.newY] = 4
        #self.drawMap()

    def calculatePath(self):
        #self.pathway = [(24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (22, 9), (21, 9), (20, 9), (19, 9), (18, 9), (17, 9), (16, 9), (15, 9), (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11), (20, 11), (21, 11), (22, 11), (23, 11), (23, 12), (23, 13), (22, 13), (21, 13), (20, 13), (19, 13), (18, 13), (17, 13), (16, 13), (15, 13), (14, 13), (13, 13), (12, 13), (11, 13), (10, 13), (9, 13), (8, 13), (7, 13), (6, 13), (5, 13), (4, 13), (3, 13), (2, 13), (1, 13), (1, 14), (1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15), (23, 16), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17), (18, 17), (17, 17), (16, 17), (15, 17), (14, 17), (13, 17), (12, 17), (11, 17), (10, 17), (9, 17), (8, 17), (7, 17), (6, 17), (5, 17), (4, 17), (3, 17), (2, 17), (1, 17), (1, 18), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (12, 19), (13, 19), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19), (19, 19), (20, 19), (21, 19), (22, 19), (23, 19), (23, 20), (23, 21), (22, 21), (21, 21), (20, 21), (19, 21), (18, 21), (17, 21), (16, 21), (15, 21), (14, 21), (13, 21), (12, 21), (11, 21), (10, 21), (9, 21), (8, 21), (7, 21), (6, 21), (5, 21), (4, 21), (3, 21), (2, 21), (1, 21), (1, 22), (1, 23), (2, 23), (3, 23), (4, 23), (5, 23), (6, 23), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23), (13, 23), (14, 23), (15, 23), (16, 23), (17, 23), (18, 23), (19, 23), (20, 23), (21, 23), (22, 23), (23, 23), (24, 23)]
        print('in')
        self.pathway = self.prologConnector.findFastestRoute()
        print(self.pathway)
        self.carCurrentPosition = self.pathway[0]
        self.calculate = False
        self.move = True
    
    def main_loop(self):
        #Event Handling
        while self.run:
            window.blit(menuPic,(0,0))
            window.fill(BLACK,((0,0),(525,525)))
            self.drawMap()
            self.createCar()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (block + margin)
                    row = pos[1] // (block + margin)
                    
                    if 550+140 > pos[0] > 550 and 290+35 > pos[1] > 290:
                        print("Start")
                        if(self.calculate == True):
                            self.carPosY-=2
                            print('in')
                            self.calculatePath()
                        elif self.grid[row][column] == 4:
                            print("Goto Exit")
                    elif 550+140 > pos[0] > 550 and 365+35 > pos[1] > 365:
                        print("Stop")
                        
                    elif 550+140 > pos[0] > 550 and 440+35 > pos[1] > 440:
                        m = Menu()
                        m.main_loop()
                            
                    ################### increase and decrease #################
                    elif 550+40 > pos[0] > 550 and 50+70 > pos[1] > 50:
                        if self.carNo1 == 10:
                            self.carNo1 -= 1
                            self.xNumCoor1 = 605
                            
                        elif self.carNo1 > 10:
                            self.carNo1 -= 1
                            self.xNumCoor1 = 590
                        
                        elif self.carNo1 == 0:
                            self.carNo1 = 0
                            self.xNumCoor1 = 605
                            
                        else:
                            self.carNo1 -= 1
                            self.xNumCoor1 = 605

                    elif 650+40 > pos[0] > 650 and 50+70 > pos[1] > 50:
                        if self.carNo1 >= 10:
                            self.carNo1 += 1
                            self.xNumCoor1 = 590
                            
                        elif self.carNo1 == 9:
                            self.carNo1 += 1
                            self.xNumCoor1 = 590
                            
                        else:
                            self.carNo1 += 1
                            self.xNumCoor1 = 605
                            
                    elif 550+40 > pos[0] > 550 and 180+70 > pos[1] > 180:
                        if self.carNo2 == 10:
                            self.carNo2 -= 1
                            self.xNumCoor2 = 605
                            
                        elif self.carNo2 > 10:
                            self.carNo2 -= 1
                            self.xNumCoor2 = 590
                        
                        elif self.carNo2 == 0:
                            self.carNo2 = 0
                            self.xNumCoor2 = 605
                            
                        else:
                            self.carNo2 -= 1
                            self.xNumCoor2 = 605

                    elif 650+40 > pos[0] > 650 and 180+70 > pos[1] > 180:
                        if self.carNo2 >= 10:
                            self.carNo2 += 1
                            self.xNumCoor2 = 590
                            
                        elif self.carNo2 == 9:
                            self.carNo2 += 1
                            self.xNumCoor2 = 590
                            
                        else:
                            self.carNo2 += 1
                            self.xNumCoor2 = 605

##                    elif self.grid[row][column] == 4:
##                        print("Goto Exit")

                    else:
                        print("Out of bound")
                        
                    

                        
            if(self.move == True):
                self.moveToCoordinate()
                
            pygame.display.update()
            clock.tick(80)
            
    

        
