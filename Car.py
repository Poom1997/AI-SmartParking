import pygame
import os
from System_Settings import *

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
        self.car_pic = pygame.image.load(os.path.join("photo","carUp.png"))
        self.status = ""

    def setExit(self):
        self.status = "exit"

    def getStatus(self):
        return self.status

    def getMove(self):
        return self.isMoving
        
    def setPath(self,path):
        self.path = path

    def getCurrentNode(self):
        return self.current_Node

    def move(self):
        #go next grid
        if (self.isMoving == False):
            #not reach destination(go on)
            if(self.path != []):
                self.nextNode = self.path.pop(0)
                self.isMoving = True
            #reach destination(stop)    
            else:
                return
        #moving       
        if(self.nextNode[0] == self.current_Node[0]):
            #go down
            if(self.nextNode[1] > self.current_Node[1]):
                self.posX += 2.1
            #go up
            elif(self.nextNode[1] < self.current_Node[1]):
                self.posX -= 2.1
            self.move_range += 2.1
            
        elif(self.nextNode[1] == self.current_Node[1]):
            #go right
            if(self.nextNode[0] > self.current_Node[0]):
                self.posY += 2.1
            #go left
            elif(self.nextNode[0] < self.current_Node[0]):
                self.posY -= 2.1
            self.move_range += 2.1

        #reached grid
        if(self.move_range >= self.grid_range):
            self.current_Node = self.nextNode
            self.isMoving = False
            self.move_range = 0

    def getDestination(self):
        if self.path != []:
            return self.path[-1]
        else:
            return None

    def draw(self):
        window.blit(self.car_pic,(self.posX, self.posY))
