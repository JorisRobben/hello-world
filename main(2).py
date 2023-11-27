import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3
SYMBOLS = {"A": 2, "B": 4, "C": 6, "D": 8}
SYMBOLS_VALUE = {"A": 5, "B": 4, "C": 3, "D": 2}

def get_slotmachine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
  columns = []
  for _ in range(cols):
    col = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      col.append(value)
      current_symbols.remove(value)
    columns.append(col)
  return columns

def print_slotmachine(columns):
  rows = []
  for row in range(len(columns[0])):
    rows.append([])
    for cols in columns:
      rows[row].append(cols[row]) 
    print(rows[row])

def check_winnings(columns, lines, bet, value):
  winnings = 0
  for line in range(lines):
    symbol = columns[0][line]
    multiplier = value[symbol]
    winning = True
    for i in range(len(columns[0])):
      if symbol != columns[i][line]:
        winning = False
        break
    if winning:
      winnings = winnings + bet*multiplier
  return winnings
      
def deposit():
  while True:
    amount = input("Please enter your deposit: ")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("That's not a valid deposit.")
    else:
      print("That's not a valid deposit.")
  return amount

def get_number_of_lines():
  while True:
    lines = input("Please enter the number of lines you want to bet on (1-" + str(MAX_LINES) +"): " )
    if lines.isdigit():
      lines = int(lines)
      if lines > 0 and lines <= MAX_LINES:
        break
      else:
        print("That's not a valid number of lines.")
    else:
      print("That's not a valid number of lines.")
  return lines

def get_bet():
  while True:
    bet = input(f"Please enter your bet between ${MIN_BET} and ${MAX_BET} on each line: ")
    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else:
        print("That's not a valid bet.")
    else:
      print("That's not a valid bet.")
  return bet

def main():
  bal = 0
  print("Welcome to the slot machine!")
  print(f"Your balance is: ${bal}.")
  print("What would you like to do?")
  while True:
    user_input = input("Press P to play, D to make a deposit, or Q to quit.")
    if user_input.upper() != "P" and user_input.upper() != 'Q' and user_input.upper() != 'D':
      print("Please make a valid selection.")
      continue
    if user_input.upper() == "Q":
      print(f"Thanks for playing! Your balance is: ${bal}.")
      break
    if user_input.upper() == "D":
      bal = bal + deposit()
      print(f"Your balance is: ${bal}.")
      continue
    if user_input.upper() == "P":
      while True:
        bet = get_bet()
        lines = get_number_of_lines()
        total_bet = bet*lines
        if total_bet > bal:
          print(f"You don't have enough money to make that bet. Your balance is: ${bal}")
          continue
        else:
          columns = get_slotmachine_spin(ROWS, COLS, SYMBOLS)
          print("Trrrr!!!! Trrrrr!!!!! The slotmachine is spinning! Trrrr!!!! PINGGGGGGGGG")
          print_slotmachine(columns)
          winnings = check_winnings(columns, lines, bet, SYMBOLS_VALUE)
          if winnings > 0:
            bal = bal + winnings
            print(f"You've won ${winnings}! You're new balance is {bal}.")
          else:
            bal = bal - total_bet
            print(f"You've got no lines. You've lost your ${total_bet}. You're new balance is {bal}.")
          break
main()
  