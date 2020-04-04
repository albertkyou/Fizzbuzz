# take in board as a list
import numpy as np 


def solver(board):
    print('Original Board: ')
    print_board(board)
    empties = get_empties(board)

    hole = 0
    flag=True
    while flag==True:

        # Get current hole
        # Fill hole in with smallest value (1)
        # Test to see if it is legal
        # if it is legal, move on to the next hole
        # if it is not legal, increase the value
        # if the value is now greater than 4, an error has been made already
        # reset the current hole back to 0 and go back to the previous hole
        # increase the value of current hole


        # find the smallest value that works for the current hole
        board[empties[hole][0],empties[hole][1]]+=1
        # print_board(board)
        if test_legality(board):
            hole+=1
        else:
            if board[empties[hole][0],empties[hole][1]] > 4:
                board[empties[hole][0],empties[hole][1]] = 0
                hole-=1

        if hole==len(empties):
            flag=False

    print('Solution: ')
    print_board(board)

def get_empties(board):
    empties = []
    for row in range(4):
        for col in range(4):
            if board[row,col]==0:
                empties.append([row,col])

    return empties



def test_legality(board):
    # test if the current board is legal
    # all rows and columns must contain 1:4
    # each 2x2 quadrant must contain 1:4
    if np.max(board) > 4:
        return False
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
    for row in range(4):
        print(board[row]) # 0 indicates empty cell

# Test case for 4x4 puzzle
def main():
    board = [[1,0,0,0],
             [0,0,0,4],
             [0,0,2,0],
             [0,3,0,0]]
    bnp = np.array(board)
    print(solver(bnp))


if __name__ == "__main__":
    main()
