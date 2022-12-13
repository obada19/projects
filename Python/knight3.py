board = [[1, 0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0,0]
       ]

board2 = [[1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        ]


promising = 0
visited = 0


def inBoard(board,x,y):
    if x >= 0 and x < len(board[0]) and y >= 0 and y < len(board) and board[x][y]==0:
        return True
    return False

# this function solves the problem
# it takes three parameters
# the board, knight's position (x,y) inside the board and a counter starting with value 1
# the counter's value increeses as long as the function inBoard() returns true
def solve(board,x,y,counter):
    global promising
    global visited
# here the function checks if the value of the counter is larger than 65
# becuase once we reach 65 so all cells in the board must had been filled
# then the function returns True, and thus we got a solution
    if counter == len(board[0])**2:
        return True
# pos_x and pos_y are all possible moves that the knight kan take
    pos_x = [1, 1, -1, -1, 2, -2, 2, -2]
    pos_y = [2, -2, 2, -2, -1, -1, 1, 1]
    if inBoard(board,x,y):
        return True

    for i in range(8):
        # here we try the moves one by one by looping over the values of either pos_x and pos_y
        new_x = x + pos_x[i]
        new_y = y + pos_y[i]
        # checks if this move is possible
        if inBoard(board, new_x, new_y):
                # if it is possible, the counter increments by 1
                # and the value of this new position are equal to coumter

                board[new_x][new_y] = counter
                promising +=1
                # here we try the same move but from this new position
                # if it is possible so we keep use same move as long as the function inBoard() is true
                #and the counter <=65
                if solve(board,new_x,new_y,counter+1):
                    # if solve() function returns false
                    # the i value in the for loop increments by 1 in order to try another move
                    # if solve() returns true so the solution is completed
                    return True
                board[new_x][new_y] = 0
                visited += 1
    return False


# solve(board,0,0,1)
# for i in board:
#     print(i)
#
solve(board2,0,0,1)
for i in board2:
    print(i)

# print("promising",promising)
# print("visited",visited)
