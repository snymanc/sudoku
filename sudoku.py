from pprint import pprint


def find_next_empty(puzzle):
    # find next row, col on the puzzle that not filled yet
    # return row, col tuple (or None, None)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces are empty (-1)


def isvalid(puzzle, guess, row, col):
    # validate guess of row/col in puzzle
    # returns True else False

    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # validate col
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col]
                for i in range(9)]  # use List Comprehension instead
    if guess in col_vals:
        return False

    # validate 3x3 square
    # get start index of square and iterate values in the row/col
    row_start = (row // 3) * 3  # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # guess is valid!
    return True


def solve_sudoku(puzzle):
    # solve using backtracking!
    # puzzle is a list of lists, each inner list is a row in the puzzle
    # returns solution as the puzzle

    # 1) choose a block on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # 1.1) check if empty spaces None puzzle solved
    if row is None:
        return True

    # 2) if spaces is empty guess a number
    for guess in range(1, 10):  # is 1, 2, 3, ... 9
        # 3) check if valid
        if isvalid(puzzle, guess, row, col):
            # 3.1) place guess on the puzzle if valid
            puzzle[row][col] = guess

            # 4) recursively call function
            if solve_sudoku(puzzle):
                return True

        # 5) if not valid OR puzzle unsolved
        #    reset number and try a new number
        puzzle[row][col] = -1  # reset the guess

    # 6) puzzle is unsolved
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print("Puzzle solved?", solve_sudoku(example_board))
    pprint(example_board)
