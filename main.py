def displayInventory(someDict):
  itemsTotal = 0
  display = 'Inventory: '
  for k, v in someDict.items():
    itemsTotal += v
    display = display + k + ' ' + str(v) + ', '
  display = display + 'Totaal aantal wapens: ' + str(itemsTotal)
  print(display)
spam = {'Katapulten': 6, 'Pijlen': 42}
displayInventory(spam)