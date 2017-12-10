row = 3
col = 3
testData = [[0,0,0],
            [0,1,0],
            [0,1,0]]
testReturn = [6,3,0,1,2,5,8]

class DataManager:
    def __init__(self, row, column, inputData = [], outputData = []):
        self.inputData = inputData
        self.outputData = outputData
        self.row = row
        self.col = column
        
    def generateZeroMatrix(self):
        newMatrix = [[0 for x in range(self.row*self.col)] for y in range(self.col*self.row)]
        return newMatrix
    
    def generateAdjcencyMatrix(self):
        adjcencyMatrix = self.generateZeroMatrix()
        newMatrixRow = -1
        for i in range(0,self.row):
            for j in range(0,self.col):
                newMatrixRow+=1
                #check for restricted block
                if(self.inputData[i][j] == 0):
                    #check-left
                    if(j-1 >= 0):
                        if(self.inputData[i][j-1] == 0):
                            adjcencyMatrix[newMatrixRow][newMatrixRow-1] = 1

                    #check-right
                    if(j+1 <= col-1):
                        if(self.inputData[i][j+1] == 0):
                            adjcencyMatrix[newMatrixRow][newMatrixRow+1] = 1
                            
                    #check-up
                    if(i-1 >= 0):
                        if(self.inputData[i-1][j] == 0):
                            adjcencyMatrix[newMatrixRow][newMatrixRow-col] = 1
                            
                    #check-down
                    if(i+1 <= row-1):
                        if(self.inputData[i+1][j] == 0):
                            adjcencyMatrix[newMatrixRow][newMatrixRow+col] = 1
        print(adjcencyMatrix)

    def generateReturnTuple(self):
        listTuple = []
        for i in self.outputData:
            x = i//self.row
            y = i%self.col
            listTuple.append((x,y))
        print(listTuple)

a = DataManager(row, col, testData, testReturn)
a.generateAdjcencyMatrix()
a.generateReturnTuple()
