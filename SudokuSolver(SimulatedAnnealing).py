#Sudoku Solver V2 (BSimulated Annealing) Algorithm)

import random

#*******************************
#Global Cycle Counter Variable
count = 0
#*******************************


#*******************************
#Functions

def RowChecker(pzl, num, row) :
    errs = 0
#    print(pzl)
    for n in range(9) :
        if(pzl[row][n] == num):
            errs += 1
    return errs



def ColumnChecker(pzl, num, col) :
    errs = 0

    for n in range(9) :
        if(pzl[n][col] == num):
            errs += 1
    return errs



def GridChecker(pzl, num, row, col) :
    errs = 0
    gridR = row//3
    gridC = col//3
    grid3 = [[0,1,2],[0,1,2],[0,1,2]]
    gridPzl = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            gridPzl[i][j] = pzl[int(grid3[j][i])+gridR*3][int(grid3[i][j])+gridC*3]
#            print("rows:{}".format(int(grid3[j][i])+gridR))
#            print("cols:{}".format(int(grid3[i][j])+gridC))
#    print("GridChecker Checker! {}".format(gridPzl))
    for i in range(3):
        if num in gridPzl[i]:
            errs += 1
    return errs



def CheckAll(pzl, num, row, col) :
    errs = 0
    errs += RowChecker(pzl, num, row)
    errs += ColumnChecker(pzl, num, col)
    errs += GridChecker(pzl, num, row, col)
    return errs



def Blanks(pzl) :
    for i in range(9):
        for j in range(9):
            if pzl[i][j] == 0:
                lst = [i,j]
                return lst
    return 0



def SolveAnnealing(index, pzl) :
    pzl1 = []
    errsS0 = CheckErrorTotal(pzl)
    print(errsS0)
    pzl1 = NewState(pzl, index)
    errsS1 = CheckErrorTotal(pzl1)
    print(errsS1)
    #PrintReadable(pzl)
    #PrintReadable(pzl1)

    return



def CheckErrorTotal(pzl) :
    errs = 0
    for i in range(9):
        for j in range(9):
            errs = errs + CheckAll(pzl, pzl[j][i], j, i)

    return errs



def NewState(pzl, index) :

    pzl1 = [x[:] for x in pzl]

    indexX = random.randint(0,8)
    indexY = random.randint(0,8)

    while (index[indexX][indexY] == 1):
        indexX = random.randint(0,8)
        indexY = random.randint(0,8)

    #print("Changed value at... X:{}, Y:{}".format(indexX, indexY))
    rand = random.randint(1,9)
    while(pzl1[indexX][indexY] == rand):
        rand = random.randint(1,9)

    #print(pzl == pzl1)
    pzl1[indexX][indexY] = rand
    #print(pzl == pzl1)

    return pzl1



#Initialize values randomly, save the intial value locations in an array
def Initialize(pzl) :
    index = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

    for i in range(9):
        for j in range(9):
            if(pzl[i][j] != 0):
                index[i][j] = 1
            else:
                #index[i][j] = 0
                pzl[i][j] = random.randint(1,9)

    arrays = [index, pzl]
    return arrays



def PrintReadable(pzl) :
    print("\n")
    for n in pzl:
        print(n)
    print("\n")
#    print("Total number of cycles: {}".format(count))
#    print("\n")

#end of functions
#*******************************


#Input Puzzle HERE:
R1 = [0,0,0,0,0,0,2,0,0]
R2 = [0,8,0,0,0,7,0,9,0]
R3 = [6,0,2,0,0,0,5,0,0]
R4 = [0,7,0,0,6,0,0,0,0]
R5 = [0,0,0,9,0,1,0,0,0]
R6 = [0,0,0,0,2,0,0,4,0]
R7 = [0,0,5,0,0,0,6,0,3]
R8 = [0,9,0,4,0,0,0,7,0]
R9 = [0,0,6,0,0,0,0,0,0]

allRows = [R1,R2,R3,R4,R5,R6,R7,R8,R9]
print("Unsolved Puzzle:")
PrintReadable(allRows)

grids = []
grids = Initialize(allRows)
print("Index Grid:\n")
PrintReadable(grids[0])
print("Randomized Puzzle:\n")
PrintReadable(grids[1])


SolveAnnealing(grids[0],grids[1])
#solved = SolveAnnealing(allRows)


#if(solved):
#    print("The puzzle is solved!")
#    PrintReadable(solved)




#Function Checking
#print("Number of blanks: {}".format(Blanks(allRows)))
#print("All errors: {}".format(CheckAll(allRows, 7, 2, 5)))
#print("Grid checker: {}".format(GridChecker(allRows, 7, 2, 5)))
#print("Column error: {}".format(ColumnChecker(allRows, 7, 5)))
#print("Row error: {}".format(RowChecker(allRows, 7, 2)))
