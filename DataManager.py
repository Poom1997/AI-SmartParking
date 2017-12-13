from GraphManager import *
import time
row = 25
col = 25
testData = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]]

testData2 = [[0, 0, 2],
             [0, 1, 0],
             [0, 1, 3]]

testReturn = [6,3,0,1,2,5,8]

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
        entranceNode = []
        exitNode = []
        newMatrixRow = -1
        for i in range(0,self.row):
            for j in range(0,self.col):
                newMatrixRow+=1
                #check for restricted block
                if(self.inputData[i][j] > 4 or self.inputData[i][j] < 0):
                    raise InvalidDataFormat()
                if(self.inputData[i][j] == 2 or self.inputData[i][j] == 3):
                    freeNode.append(newMatrixRow)
##                if(self.inputData[i][j] == 2):
##                    entranceNode.append(newMatrixRow)
##                elif(self.inputData[i][j] == 2):
##                    exitNode.append(newMatrixRow)
                if(self.inputData[i][j] == 0 or self.inputData[i][j] == 2 or self.inputData[i][j] == 3):
                    #check-left
                    if(j-1 >= 0):
                        if(self.inputData[i][j-1] == 0 or self.inputData[i][j-1] == 2 or self.inputData[i][j-1] == 3):
                            adjcencyMatrix[newMatrixRow][newMatrixRow-1] = 1

                    #check-right
                    if(j+1 <= col-1):
                        if(self.inputData[i][j+1] == 0 or self.inputData[i][j+1] == 2 or self.inputData[i][j+1] == 3):
                            adjcencyMatrix[newMatrixRow][newMatrixRow+1] = 1
                            
                    #check-up
                    if(i-1 >= 0):
                        if(self.inputData[i-1][j] == 0 or self.inputData[i-1][j] == 2 or self.inputData[i-1][j] == 3):
                            adjcencyMatrix[newMatrixRow][newMatrixRow-col] = 1
                            
                    #check-down
                    if(i+1 <= row-1):
                        if(self.inputData[i+1][j] == 0 or self.inputData[i+1][j] == 2 or self.inputData[i+1][j] == 3):
                            adjcencyMatrix[newMatrixRow][newMatrixRow+col] = 1

        print(freeNode)
        #self.connector.setGraph(adjcencyMatrix, freeNode ,exitNode)
        self.connector.setGraph(adjcencyMatrix, freeNode)

    def findFastestRoute(self, a=601, b=623, status = 'enter'):
        self.outputData = self.connector.getPath(a,b,status)
        #print(self.outputData)
        return self.returnTuple()

    def findFastestParkingRoute(self, row, col):
        print(row * self.row-1 + col-1)
        self.outputData = self.connector.park(row * self.row-1 + col-1)
        #print(self.outputData)
        return self.returnTuple()
    
    def findFastestExitRoute(self, a=601, b=623, status = 'enter'):
        self.outputData = self.connector.getPath(a,b,status)
        #print(self.outputData)
        return self.returnTuple()
    
    def returnTuple(self):
        listTuple = []
        for i in self.outputData:
            x = i//self.row
            y = i%self.col
            listTuple.append((x,y))
        return listTuple

##a = DataManager(row, col, testData)
##start_time = time.time()
##a.setup()
##print("--- %s seconds for setup ---" % (time.time() - start_time))
##start_time = time.time()
##print(a.findFastestRoute(601,623))
##print("--- %s seconds for shortest Path ---" % (time.time() - start_time))
##start_time = time.time()
##print(a.findFastestRoute(601,623))
##print("--- %s seconds for shortest Path ---" % (time.time() - start_time))

