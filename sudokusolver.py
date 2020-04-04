# take in board as a list
import numpy as np 


def mini(board):
    # main loop to fill in the board
    for i in range(10):
        board = fill_hole(board)
    
    print_board(board)

def fill_hole(board):
    # solves 4x4 sudoku boards
    # brute force recursion
    # start at top left cell and insert lowest possible value that does not interfere with the rest of the board
    # once a successful value is found, move onto the next cell
    # if no cells are possible, remove previous cell and go to the next lowest possible value

    # find first 0 and replace with x
    for row in range(4):
        for col in range(4):
            if board[row,col]==0:
                print_board(board)
                board[row,col]=1 # set it as 1
                if test_legality(board):
                    return board # if 1 works, then move on to the next cell

                else:
                    board[row,col]+=1
                    return board


def test_legality(board):
    # test if the current board is legal
    # all rows and columns must contain 1:4
    # each 2x2 quadrant must contain 1:4

    # test rows and columns first
    for row in range(4):
        for value in range(4):
            if np.count_nonzero(board[row,:]==value+1)>1:
                return False

    for col in range(4):
        for value in range(4):
            if np.count_nonzero(board[:,col]==value+1)>1:
                return False

    # test quadrants
    # define the quadrant

    for qrow in range(2):
        for qcol in range(2):
            quadrant = board[2*qrow:2*(qrow+1),2*qcol:2*(qcol+1)]
            for value in range(4):
                if np.count_nonzero(quadrant==value+1)>1:
                    return False

    return True






def print_board(board):
    print('board: ')
    for row in range(4):
        
        print(board[row]) # 0 indicates empty cell

# Test case for 4x4 puzzle
def main():
    board = [[4,3,0,0],[1,2,3,0],[0,0,2,0],[2,1,0,0]]
    bnp = np.array(board)
    mini(bnp)


if __name__ == "__main__":
    main()
