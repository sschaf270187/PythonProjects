#Sudoku Solver V1 (Backtracking Algorithm)

#*******************************
#Functions

def RowChecker(pzl) :
    errs = 0
#    print(pzl)
    for n in pzl :
        if(len(n) != len(set(n))):
            errs += 1
    return errs



def ColumnChecker(pzl) :
    errs = 0
    pzlCol = pzl.copy()
    for i in range(9) :
        for j in range(9) :
            pzlCol[i][j] = pzl[j][i]
            print(pzl[j][i])
    
    for n in pzlCol :
        if(len(n) != len(set(n))):
            errs += 1
    print(pzlCol)
    return errs

#end of functions
#*******************************

totalErrs = 0

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


totalErrs = totalErrs + RowChecker(allRows)

totalErrs = totalErrs + ColumnChecker(allRows)

print(totalErrs)

if(totalErrs > 0):
    print("Puzzle is not solved, there are still {} errors.".format(totalErrs))
