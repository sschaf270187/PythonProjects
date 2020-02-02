#Sudoku Solver V1 (Backtracking Algorithm)

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



def Solve(pzl) :
    loc = Blanks(pzl)
    if(loc == 0):
        return pzl
    else:
        for n in range(1,10):
            if(CheckAll(pzl, n, loc[0], loc[1]) == 0):
                pzl[loc[0]][loc[1]] = n
                PrintReadable(pzl)
                if(Solve(pzl)):
                    return pzl
                else:
                    pzl[loc[0]][loc[1]] = 0
        return 0

    
    
def PrintReadable(pzl) :
    print("\n")
    for n in pzl:
        print(n)
    print("\n")
    global count
    count = count + 1
    print("Total number of cycles: {}".format(count))
    print("\n")

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


solved = Solve(allRows)
if(solved):
    print("The puzzle is solved!")
    PrintReadable(solved)


#Function Checking
#print("Number of blanks: {}".format(Blanks(allRows)))
#print("All errors: {}".format(CheckAll(allRows, 7, 2, 5)))
#print("Grid checker: {}".format(GridChecker(allRows, 7, 2, 5)))
#print("Column error: {}".format(ColumnChecker(allRows, 7, 5)))
#print("Row error: {}".format(RowChecker(allRows, 7, 2)))
