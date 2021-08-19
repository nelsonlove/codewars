"""
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return
'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only
once.

Rows:

|_5_|_3_|_8_||_6_|_9_|_7_||_4_|_1_|_2_|

There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in
black are the numbers that you fill in to complete the row.

Columns:

 ___
| 7 |
| 4 |
|_8_|
| 5 |
| 9 |
|_2_|
| 1 |
| 3 |
|_6_|

There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the
numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be
unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining
numbers as shown in black to complete the column.

Regions

 | 4 | 5 | 1 |
 | 6 | 9 | 7 |
 |_3_|_2_|_8_|

A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8,
and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as
shown in black to complete the region.

Valid board example:

| 5 | 3 | 4 || 6 | 7 | 8 || 9 | 1 | 2 |
| 6 | 7 | 2 || 1 | 9 | 5 || 3 | 4 | 8 |
|_1_|_9_|_8_||_3_|_4_|_2_||_5_|_6_|_7_|
| 8 | 5 | 9 || 7 | 6 | 1 || 4 | 2 | 3 |
| 4 | 2 | 6 || 8 | 5 | 3 || 7 | 9 | 1 |
|_7_|_1_|_3_||_9_|_2_|_4_||_8_|_5_|_6_|
| 9 | 6 | 1 || 5 | 3 | 7 || 2 | 8 | 4 |
| 2 | 8 | 7 || 4 | 1 | 9 || 6 | 3 | 5 |
|_3_|_4_|_5_||_2_|_8_|_6_||_1_|_7_|_9_|

For those who don't know the game, here are some information about rules and how to play
Sudoku: http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/
"""


def done_or_not(board):
    rows = []
    cols = []
    squares = []
    for y in range(9):
        rows.append(board[y])
        col = []
        for x in range(9):
            col.append(board[x][y])
        cols.append(col)

    for a in range(3):
        i = a * 3
        for b in range(3):
            j = b * 3
            square = []
            for x in range(3):
                for y in range(3):
                    square.append(board[x + i][y + j])
            squares.append(square)

    for seq in cols + rows + squares:
        for i in range(9):
            if seq.count(i + 1) != 1:
                return 'Try again!'
    return 'Finished!'
