# Write your code here :-)
def printTable(someTable):
    longestStringLength = 0

    for i in range(0,len(someTable[0])):
        currentStringLength = 0
        for j in range(0,len(someTable)):
            currentStringLength = currentStringLength + len(someTable[j][i])
        if currentStringLength > longestStringLength:
            longestStringLength = currentStringLength

    listOfRows = []

    for i in range(len(someTable[0])):
        currentString = ''
        for j in range(len(someTable)):
            if j == len(someTable) - 1:
                currentString = currentString + someTable[j][i]
            else:
                currentString = currentString + someTable[j][i] + ' '
        listOfRows.append(currentString)

    for i in range(0,len(listOfRows)):
        print(listOfRows[i].ljust(int(longestStringLength),'*'))

printTable([['apples', 'oranges', 'che','ban'],['Alice','Bobbutlonger','Carol','David'],['dogs','cats','moose','goose']])

