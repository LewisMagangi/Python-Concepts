row, col = (13, 25)
board = [[0]*col]*row

for i in range(row):
    for j in range(col):
        if j == 0 or j == 8 or j == 16 or j == 24:
            if i == 0 or i == 4 or i == 8 or i == 12:
                board[i][j] = "+"
            elif i != 0 or i != 4 or i != 8 or 1 != 12:
                board[i][j] = "|"
        elif j != 0 or j != 8 or j != 16 or j != 24:
            if i == 0 or i == 4 or i == 8 or i == 12:
                board[i][j] = "-"
        """elif i != 0 or i != 4 or i != 8 or i != 12:
            if j != 0 and row != 8 and row != 16 and row != 24:
                board.insert(row, "-") 

#print(board[row][l])
print(board)"""
print(row, col)
print(board)
