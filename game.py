def solve(bo):
    #getting the coordinate of empty box
    find = is_empty(bo)
    #if no empty found, whole grid is full, we are done
    if not find:
        return True
    else:
        row, col = find
    #using backtracking algo to check for the correct ans to be filled in that given box
    for i in range(1,10):
        if valid(bo, i ,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False

def valid(bo,num,pos):
    #checking of duplicasy row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #checking for duplicasy in column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False
    #checking for duplicasy in the 3X3 grid
    x_box = pos[1] // 3
    y_box = pos[0] // 3
    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box*3, x_box*3 +3):
            if bo[i][j] == num and (i,j)!= pos:
                return False
    return True
#to return the coordinate of empty box
def is_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i,j)
    return None

#fun to print the board, just for testing purpose
def print_board(bo):
    for i in range(len(bo)):
        if i%3 == 0 and i!=0:
            print("- - - - - - - - - - - - -")
        for j in range(len(bo)):
            if j%3==0 and j!= 0:
                print(" | ",end="")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " " ,end="")



