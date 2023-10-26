def printTable(someTable):
  numRows = len(someTable)
  numCols = len(someTable[0])
  longestStringLength = 0
  
  for i in range(0,len(someTable[0])):
    currentStringLength = 0
    for j in range(0,len(someTable)):
      currentStringLength = currentStringLength + len(someTable[j][i])
    if currentStringLength > longestStringLength:
      longestStringLength = currentStringLength
  print(str(longestStringLength))
printTable([['apples', 'oranges', 'che','ban'],['Alice','Bobbutlonger','Carol','David'],['dogs','cats','moose','goose']])
