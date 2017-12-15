import pygame
import csv
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from DataManager import *
from System_Settings import *
from Car import *
from GridController import *

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
                        self.simulate = MainSimulation()
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
        self.pic = pathSign
        self.grid = []
        self.parkingMap()

    def parkingMap(self):
        try:
            self.grid = []
            for i in range(self.row):
                self.grid.append([])
                for j in range(self.column):
                    if i == 0 or i == self.row-1 or j == 0 or j == self.column-1:
                        self.grid[i].append(1)
                    else:
                        self.grid[i].append(0)
        except IndexError as e:
            message = "The file you are trying to load has an invalid dimension.\n Valid Dimensions is 25x25"
            messagebox.showinfo("Invalid Dimension", message)
                
    def saveMap(self):
        try:
            self.fileName = asksaveasfilename()
            with open(self.fileName, 'w') as csvfile:
                writer = csv.writer(csvfile)
                [writer.writerow(r) for r in self.grid]
                
        except FileNotFoundError as e:
            pass
            
    def loadMap(self):
        try:
            self.grid = []
            self.file_path = filedialog.askopenfilename()
            with open(self.file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                table = [[int(e) for e in r] for r in reader]

            for i in table:
                if(len(i) is not 0):
                    self.grid.append(i)

        except ValueError as e:
            message = "The file you are trying to load has an invalid data.\n File is Corrupted!"
            messagebox.showerror("Invalid Dimension", message)
            m = Menu()
            m.main_loop()

        except InvalidDataFormat as e:
            message = "The file you are trying to load has an invalid data.\n File is Corrupted!"
            messagebox.showerror("Invalid Dimension", message)
            m = Menu()
            m.main_loop()

        except FileNotFoundError as e:
            message = "Please select a file to load.\nFile not Found!"
            messagebox.showinfo("File?", message)
            m = Menu()
            m.main_loop()
            
    def drawMap(self):
        try:
            for i in range(self.row):
                for j in range(self.column):
                    self.color = WHITE
                    if self.grid[i][j] == 0:
                        self.pic = pathSign
                        self.color = WHITE
                    if self.grid[i][j] == 1:
                        self.pic = wallSign
                        self.color = RED
                    elif self.grid[i][j] == 2:
                        self.pic = parkingSign
                        self.color = GREEN
                    elif self.grid[i][j] == 3:
                        self.pic = entranceSign
                        self.color = BLUE
                    elif self.grid[i][j] == 4:
                        self.pic = carInSign
                        self.color = YELLOW
                    elif self.grid[i][j] == 5:
                        self.pic = exitSign
                        self.color = PURPLE
                    window.blit(self.pic,[(margin + block) * j + margin,
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
            
        except IndexError as e:
            message = "The file you are trying to load has an invalid dimension.\n Valid Dimensions is 25x25"
            messagebox.showinfo("Invalid Dimension", message)
            m = Menu()
            m.main_loop()
            
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
                        #print("Path")
                    elif 550+130 > pos[0] > 550 and 115+50 > pos[1] > 115:
                        self.toggleNum = 1
                        #print("Wall")
                    elif 550+130 > pos[0] > 550 and 50+50 > pos[1] > 50:
                        self.toggleNum = 2
                        #print("Parking Lot")
                    elif 550+130 > pos[0] > 550 and 180+50 > pos[1] > 180:
                        self.toggleNum = 3
                        #print("Entrance")
                    elif 550+130 > pos[0] > 550 and 245+50 > pos[1] > 245:
                        self.toggleNum = 5
                        #print("Exit")
                   
                    ## SaveButton
                    elif 550+130 > pos[0] > 550 and 385+25 > pos[1] > 385:
                        #print("saveMap")
                        self.saveMap()
                    ## LoadButton
                    elif 550+130 > pos[0] > 550 and 430+25 > pos[1] > 430:
                        #print("loadMap")
                        self.loadMap()
                    ## ClearButton
                    elif 550 + 130 > pos[0] > 550 and 475+25 > pos[1] > 475:
                        #print('clearMap')
                        m = Menu()
                        m.main_loop()
                    else:
                        pass

            pygame.display.update()
            clock.tick(80)
            
#Start Simulation Mode
class MainSimulation:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.row = 25
        self.column = 25
        self.prologConnector = None
        self.isPause = False
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
        self.car_list = []
        self.availableSlot = 0
        self.clickCountCar = 0
        self.wordPause = "Pause"
        self.carNo = 0
        self.delay = 0
        self.time = 0
        self.pic = pathSign
        self.carNo1 = 0
        self.carNo2 = 0
        self.tempColor = WHITE
        self.grid = []
        self.pathway = []
        self.carLocation = 22
        self.parkingMap()
        self.setup()
        
    def parkingMap(self):
        try:
            self.grid = []
            self.file_path = filedialog.askopenfilename()
            with open(self.file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                table = [[int(e) for e in r] for r in reader]

            for i in table:
                if(len(i) is not 0):
                    self.grid.append(i)

        except ValueError as e:
            message = "The file you are trying to load has an invalid data.\n File is Corrupted!"
            messagebox.showerror("Invalid Dimension", message)
            m = Menu()
            m.main_loop()

        except InvalidDataFormat as e:
            message = "The file you are trying to load has an invalid data.\n File is Corrupted!"
            messagebox.showerror("Invalid Dimension", message)
            m = Menu()
            m.main_loop()

        except FileNotFoundError as e:
            message = "Please select a file to load.\nFile not Found!"
            messagebox.showinfo("File?", message)
            m = Menu()
            m.main_loop()

    def setup(self):
        #print("in")
        #print(self.grid)
        try:
            self.prologConnector = DataManager(self.row, self.column, self.grid)
            self.prologConnector.setup()
            self.availableSlot = self.prologConnector.getLenPark()
        except IndexError as e:
            message = "The file you are trying to load has an invalid dimension.\n Valid Dimensions is 25x25"
            messagebox.showerror("Invalid Dimension", message)
            m = Menu()
            m.main_loop()

    def drawMap(self):
        try:
            self.strCarNo1 = str(self.carNo1)
            self.strCarNo2 = str(self.carNo2)
            self.carNoText1 = font3.render(self.strCarNo1,True, self.tempColor)
            self.carNoText2 = font3.render(self.strCarNo2,True, self.tempColor)
            parkingText = font1.render("Car Park",True, BLACK)
            for i in range(self.row):
                for j in range(self.column):
                    self.color = WHITE
                    if self.grid[i][j] == 0:
                        self.pic = pathSign
                        #print(i," and ",j)
                    if self.grid[i][j] == 1:
                        #print("i = ",i, " j = ",j)
                        self.pic = wallSign
                        self.color = RED
                    elif self.grid[i][j] == 2:
                        self.pic = parkingSign
                        self.color = GREEN
                    elif self.grid[i][j] == 3:
                        self.pic = entranceSign
                        self.color = BLUE
                    elif self.grid[i][j] == 4:
                        self.pic = carInSign
                        self.color = YELLOW
                    elif self.grid[i][j] == 5:
                        self.pic = exitSign
                        self.color = PURPLE
                    window.blit(self.pic,[(margin + block) * j + margin,
                                      (margin + block) * i + margin,
                                       block, block])

            stop_button = pygame.draw.rect(window,CYAN,(550,365,140,35))
            back_button = pygame.draw.rect(window,CYAN,(550,440,140,35))

            stopText = font1.render(self.wordPause,True,BLACK)

            window.blit(carEntranceText1, (540,10))
            window.blit(carEntranceText2, (555,170))
            self.strCarNo = str(self.carNo)
            self.carNoText = font3.render(self.strCarNo,True,WHITE)
            self.strAvailable = str(self.availableSlot)
            self.availableText = font3.render(self.strAvailable,True,WHITE)

            if self.availableSlot <= 9:
                window.blit(self.availableText, (self.xNumCoor1+5,50))
                if self.carNo <= 9:
                    window.blit(self.carNoText,(self.xNumCoor2+5,230))
                elif self.carNo > 9:
                    window.blit(self.carNoText,(self.xNumCoor2-7,230))
                    
            elif self.availableSlot > 9:
                window.blit(self.availableText, (self.xNumCoor1-7,50))
                if self.carNo <= 9:
                    window.blit(self.carNoText,(self.xNumCoor2+5,230))
                elif self.carNo > 9:
                    window.blit(self.carNoText,(self.xNumCoor2-7,230))
            window.blit(stopText, (585,365))
            window.blit(backText2, (590,440))

        except IndexError as e:
            message = "The file you are trying to load has an invalid dimension.\n Valid Dimensions is 25x25"
            messagebox.showerror("Invalid Dimension", message)
            m = Menu()
            m.main_loop()
        
    def main_loop(self):
        gridController = GridController()
        #Event Handling
        while self.run:
            window.blit(menuPic,(0,0))
            window.fill(BLACK,((0,0),(525,525)))
            self.drawMap()
            self.time = (int(round(pygame.time.get_ticks()/1000)))
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()
                    Y = pos[1] // (block + margin)
                    X = pos[0] // (block + margin)
                    if pos[0] <= 525 and pos[1] <= 525:
                        if self.grid[Y][X] == 3 and self.time > self.delay:
                            #print("Entrance = ",X,",",Y)
                            temp_car = Car(X*(block+margin),Y*(block+margin),(Y,X),gridController)
                            path = self.prologConnector.findFastestParkingRoute(Y,X)
                            if path != []:
                                temp_car.setPath(path)
                                destination = temp_car.getDestination()
                                self.car_list.append(temp_car)
                                self.carNo += 1
                                self.availableSlot -= 1
                                self.clickCountCar += 1
                                self.delay = self.time+1 
                                if destination != None:
                                    self.grid[destination[0]][destination[1]] = 4

                        elif self.grid[Y][X] == 4 and self.time > self.delay:
                            #print("park = ",X,",",Y)
                            for car in self.car_list:
                                car_grid = car.getCurrentNode()
                                #print(car_grid)
                                if Y == car_grid[0] and X == car_grid[1]:
                                    exitPath = self.prologConnector.findFastestExitRoute(Y,X)
                                    car.setPath(exitPath)
                                    dest = car.getDestination()
                                    car.setExit()
                                    self.carNo -= 1
                                    self.availableSlot += 1
                                    self.grid[Y][X] = 2
                                    self.clickCountCar -= 1
                                    self.delay = self.time+1
                                    
                                else:
                                    #print("Wrong")
                                    pass
                        
                        else:
                            #print("Not the car parking")
                            pass
                        
                    elif 550+140 > pos[0] > 550 and 365+35 > pos[1] > 365:
                       if self.isPause == False:
                            self.wordPause = "Resume"
                            self.isPause = True
                            
                       elif self.isPause ==True:
                            self.wordPause = "Pause"
                            self.isPause = False
                        
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
                    else:
                        #print("Out of bound")
                        pass
                        
            ## Main Game Loop      
            if self.isPause == False:
                for car in self.car_list:
                    car.move()
                    if ((car.getDestination() == None) and (car.getStatus() == "exit")):
                        car.freeGrid()
                        self.car_list.remove(car)
                        #print('Car lenght')
                        #print(len(self.car_list))
                        continue

            else: pass
            for car in self.car_list:
                    car.draw()
            pygame.display.update()
            clock.tick(120)
