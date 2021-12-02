#rotate the grid clockwise 90 degrees
#need to use a loop in a loop in order to
#print grid[0][0], then grid[1][0], then grid[2][0], etc up to grid[8][0].
#This will finish the first row, so then print a newline.
#Then your program should print grid[0][1], grid[1][1],  grid[2][1], so on.
#The last thing to print is grid[8][5].

#didnt actually do this one, since i had to look up what the instructions were
#even trying to say (it didnt mention you needed to rotate the image)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(6):
    for j in range(9):
        print(grid[j][i], end='')
    print('')
