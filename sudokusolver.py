# take in board as a list
import numpy as np 





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
