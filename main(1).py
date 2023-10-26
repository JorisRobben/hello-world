def printTable(someTable):
  numRows = len(someTable)
  numCols = len(someTable[0])
  longestStringLength = 0
  
  for i in range(0,len(someTable)):
    currentStringLength = len(someTable[i][0]) + len(someTable[i][1]) + len(someTable[i][2])
    
  if currentStringLength > longestStringLength:
    longestStringLength = currentStringLength
  print(str(longestStringLength))
printTable([['apples', 'oranges', 'cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']])