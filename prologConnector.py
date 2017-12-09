row = 3
col = 3
testData = [[0,0,0],
            [0,1,0],
            [0,1,0]]
testReturn = [6,3,0,1,2,5,8]

def newMatrixGenerator(row, col):
    temp = [[0 for x in range(row*col)] for y in range(col*row)]
    return temp
    
def generateAdjcencyMatrix(row, col, inp_data):
    newMatrix = newMatrixGenerator(row, col)
    newMatrixRow = -1
    for i in range(0,row):
        for j in range(0,col):
            newMatrixRow+=1
            #check for restricted block
            if(inp_data[i][j] == 0):
                #check-left
                if(j-1 >= 0):
                    if(inp_data[i][j-1] == 0):
                        newMatrix[newMatrixRow][newMatrixRow-1] = 1

                #check-right
                if(j+1 <= col-1):
                    if(inp_data[i][j+1] == 0):
                        newMatrix[newMatrixRow][newMatrixRow+1] = 1
                        
                #check-up
                if(i-1 >= 0):
                    if(inp_data[i-1][j] == 0):
                        newMatrix[newMatrixRow][newMatrixRow-col] = 1
                        
                #check-down
                if(i+1 <= row-1):
                    if(inp_data[i+1][j] == 0):
                        newMatrix[newMatrixRow][newMatrixRow+col] = 1
    print(newMatrix)

def generateReturnTuple(row, col, input_data):
    temp = []
    for i in input_data:
        x = i//row
        y = i%col
        temp.append((x,y))
    print(temp)
    
generateAdjcencyMatrix(row, col, testData)
generateReturnTuple(3,3,testReturn)
