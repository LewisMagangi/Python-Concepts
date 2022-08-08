board = []
null = " "
value = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for col in range(13):
    row = [null for i in range(25)]
    board.append(row)

for col in range(13):
    if row[0] or row[8] or row[16] or row[24]:
        if col == 0 or col == 4 or col == 8 or col == 12:
            board.insert( , "+")
    elif col == 0 or col == 4 or col == 8 or col == 12:
        if row != 0 and row != 8 and row != 16 and row != 24:
            board.insert(row, "-") 

#print(board[row][l])
print(board)
