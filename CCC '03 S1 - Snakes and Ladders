# starting position
pos = 1

while True:
  roll = int(input())

  # end game if roll = 0
  if roll == 0:
    print('You Quit!')
    break

  # limit roll addition if sum exceeds 100
  if pos + roll <= 100:
    pos += roll
    
    # win condition
    if pos == 100:
      print("You are now on square 100")
      print("You Win!")
      break
    
    # ladders
    elif pos == 9: pos = 34;
    elif pos == 40: pos = 64;
    elif pos == 67: pos = 86;
  
    # snakes
    elif pos == 54: pos = 19;
    elif pos == 90: pos = 48;
    elif pos == 99: pos = 78;

  print("You are now on square", pos)
