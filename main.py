board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    row, col = find

    for i in range(1,10):
        if valid(bo, i, [row, col]):
            bo[row][col] = i
            
            if solve(bo):
                return True
            bo[row][col] = 0
    return False




def valid(bo, num, pos):
    #Check row
    if bo[pos[0]].count(num) > 0:
        return False
    #Check Coloumn
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    #Check Box
    box_X = pos[1] // 3    
    box_Y = pos[0] // 3
    for i in range(box_Y * 3, box_Y * 3 + 3):
        for j in range(box_X * 3, box_X * 3 + 3):
            if bo[i][j] == num and (pos[0] != i and pos[1] != j):
                return False
    return True

#Prints the board to terminal 
def print_board(bo):
    for i in range(len(bo)):
        if not i % 3 and i !=0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(bo[0])):
            if not j % 3 and j != 0:
                print(" | ", end="")      
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#Finds the first empty cell in a board, from left to right, top down
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return [i,j]
    return None



print_board(board)
solve(board)
print("\n")
print_board(board)