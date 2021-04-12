# The sudoku grid is defined as a list of lists. Each list element represents a row on the sudoku grid.
# Included template values and grid for test, before GUI implementation

grid = [
       [7, 8, 0, 4, 0, 0, 1, 2, 0],
       [6, 0, 0, 0, 7, 5, 0, 0, 9],
       [0, 0, 0, 6, 0, 1, 0, 7, 8],
       [0, 0, 7, 0, 4, 0, 2, 6, 0],
       [0, 0, 1, 0, 5, 0, 9, 3, 0],
       [9, 0, 4, 0, 6, 0, 0, 0, 5],
       [0, 7, 0, 3, 0, 0, 0, 1, 2],
       [1, 2, 0, 0, 0, 7, 4, 0, 0],
       [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# The solve calls findEmptySpace on the current grid to locate the next empty space to try.
# If there are no empty spaces, the method returns true and the puzzle is solved. Else:
# Iterates through numbers 1 to 9 and runs checkBoardValid method to verify the new number.
# If the board is valid, the number is entered into the grid, and the method is called again on the next empty space.
# If the board is not valid, the next number will be attempted.
# If numbers 1-9 are not valid, the


def solve(grid):
    find = findEmptySpace(grid)
    if not find:
        return True
    else:
        row, column = find

    for number in range(1, 10):
        if checkBoardValid(grid, number, (row, column)):
            grid[row][column] = number

            if solve(grid):
                return True

            grid[row][column] = 0

    return False

# Method verifies the new number tried is not already in the row, column or square of the space the number has been entered into.


def checkBoardValid(grid, number, space):
    for column in range(len(grid[0])):
        if grid[space[0]][column] == number and space[1] != column:
            return False

    for row in range(len(grid)):
        if grid[row][space[1]] == number and space[0] != row:
            return False

    square_x = space[1] // 3
    square_y = space[0] // 3

    for row in range(square_y*3, square_y*3 + 3):
        for column in range(square_x*3, square_x*3 + 3):
            if grid[row][column] == number and (row, column) != space:
                return False

    return True

# Locates the next empty space on the grid.
# Takes the grid as an input parameter and searches for the next zero.


def findEmptySpace(grid):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 0:
                return (row, column)

    return None

print("ORIGINAL:")
print(grid)
solve(grid)
print("COMPLETED:")
print(grid)