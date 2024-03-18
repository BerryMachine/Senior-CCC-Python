# get number of quarters as input
quarters = int(input())

# get number of times each machine has been played
first = 35 - int(input())
second = 100 - int(input())
third = 10 - int(input())
plays = 0
cycle = 1

# loop until quarters are 0
while quarters > 0:
  # play first machine
  if cycle == 1:
    first += 1
    if first == 35:
      quarters += 30
      first = 0
    cycle = 2

  # play second machine
  elif cycle == 2:
    second += 1
    if second == 100:
      quarters += 60
      second = 0
    cycle = 3

  # play third second machine
  else:
    third += 1
    if third == 10:
      quarters += 9
      third = 0
    cycle = 1

  plays += 1
  quarters -= 1
  
print(f"Martha plays {plays} times before going broke.")
