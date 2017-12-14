from GraphManager import *
import time

class InvalidDataFormat(Exception):
    pass

class DataManager:
    def __init__(self, row, column, inputData = []):
        self.connector = GraphManager()
        self.inputData = inputData
        self.outputData = []
        self.row = row
        self.col = column
        
    def generateZeroMatrix(self):
        newMatrix = [[0 for x in range(self.row*self.col)] for y in range(self.col*self.row)]
        return newMatrix
    
    def setup(self):
        adjcencyMatrix = self.generateZeroMatrix()
        freeNode = []
        parkingNode = []
        exitNode = []
        newMatrixRow = -1
        for i in range(0,self.row):
            for j in range(0,self.col):
                newMatrixRow+=1
                #check for restricted block
                if(self.inputData[i][j] > 5 or self.inputData[i][j] < 0):
                    raise InvalidDataFormat()
                if(self.inputData[i][j] == 2):
                    parkingNode.append(newMatrixRow)
                elif(self.inputData[i][j] == 5):
                    exitNode.append(newMatrixRow)
                if(self.inputData[i][j] == 0 or self.inputData[i][j] == 2 or self.inputData[i][j] == 3):
                    #check-left
                    if(j-1 >= 0):
                        if(self.inputData[i][j-1] == 0 or self.inputData[i][j-1] == 2 or self.inputData[i][j-1] == 3 or self.inputData[i][j-1] == 5):
                            adjcencyMatrix[newMatrixRow][newMatrixRow-1] = 1

                    #check-right
                    if(j+1 <= col-1):
                        if(self.inputData[i][j+1] == 0 or self.inputData[i][j+1] == 2 or self.inputData[i][j+1] == 3 or self.inputData[i][j+1] == 5):
                            adjcencyMatrix[newMatrixRow][newMatrixRow+1] = 1
                            
                    #check-up
                    if(i-1 >= 0):
                        if(self.inputData[i-1][j] == 0 or self.inputData[i-1][j] == 2 or self.inputData[i-1][j] == 3 or self.inputData[i-1][j] == 5):
                            adjcencyMatrix[newMatrixRow][newMatrixRow-col] = 1
                            
                    #check-down
                    if(i+1 <= row-1):
                        if(self.inputData[i+1][j] == 0 or self.inputData[i+1][j] == 2 or self.inputData[i+1][j] == 3 or self.inputData[i+1][j] == 5):
                            adjcencyMatrix[newMatrixRow][newMatrixRow+col] = 1

        self.connector.setGraph(adjcencyMatrix, parkingNode, exitNode)

    def findFastestParkingRoute(self, row, col):
        print((row * self.row) + col)
        self.outputData = self.connector.park(((row * self.row) + col))
        if self.outputData == []:
            return []
        return self.returnTuple()
    
    def findFastestExitRoute(self, row, col):
        print((row * self.row) + col)
        self.outputData = self.connector.autoexit(((row * self.row) + col))
        if self.outputData == []:
            return []
        return self.returnTuple()
    
    def returnTuple(self):
        listTuple = []
        for i in self.outputData:
            x = i//self.row
            y = i%self.col
            listTuple.append((x,y))
        return listTuple
    
    def getLenPark(self):
        return self.connector.getLenPark()
