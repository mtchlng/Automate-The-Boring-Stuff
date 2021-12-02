#Take a list of strings
#Display them in an organized table, with each column right justified
#Assume all inner lists will contain the same number of strings

#to justify 10 spaces, it would add one space to 9 letters, 2 to 8 letters, etc

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths=[0]*len(tableData) #length = number of lists in tableData
#creates colWidths=[0][0][0]

index1 = 0
for item in tableData:
    for word in item:
        if len(word)>colWidths[index1]: #check how to index items in tableData
            colWidths[index1] = len(word)
    index1 += 1
index2 = 0
for item in tableData:
    for word in item:
        print(word.rjust(colWidths[index2]))
    index2 += 1


def printTable(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j])> colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    for x in range(len(tableData[0])): #0,1,2,3
        for y in range(len(tableData)):#0,1,2
            print(tableData[y][x].rjust(colWidths[y]), end = ' ')
