import pygame
import os

class Car:
    def __init__(self, posX,posY, entrace):
        self.posX = posX
        self.posY = posY
        self.current_Node = entrace
        self.nextNode = None
        self.path = []
        self.isMoving = False
        self.grid_range = 21
        self.move_range = 0
        self.car_pic = pygame.image.load(os.path.join("photo","car.png"))

    def setPath(self,path):
        self.path = path

    def move(self):
        #go next grid
        if (self.isMoving == False):
            #not reach destination(go on)
            if(self.path != []):
                print(self.path)
                self.nextNode = self.path.pop(0)
                self.isMoving = True
            #reach destination(stop)    
            else:
                return
        #moving       
        if(self.nextNode[0] == self.current_Node[0]):
            #go down
            if(self.nextNode[1] > self.current_Node[1]):
                print('down')
                self.posY += 2
            #go up
            elif(self.nextNode[1] < self.current_Node[1]):
                print('up')
                self.posY -= 2
            self.move_range += 2
            
        elif(self.nextNode[1] == self.current_Node[1]):
            #go right
            if(self.nextNode[0] > self.current_Node[0]):
                print('right')
                self.posX += 2
            #go left
            elif(self.nextNode[0] < self.current_Node[0]):
                print('left')
                self.posX -= 2
            self.move_range += 2

        #reached grid
        if(self.move_range >= self.grid_range):
            self.current_Node = self.nextNode
            self.isMoving = False
            self.move_range = 0
            

    def draw(self):
        window.blit(self.pic,(self.posX, self.posY))
