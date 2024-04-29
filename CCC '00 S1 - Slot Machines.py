# get number of quarters as input
quarters = int(input())

# get number of times each machine has been played
first = int(input())
second = int(input())
third = int(input())

# keep track of plays
plays = 0

while True:
  # add plays to each machine based on number of quarters
  remainder = quarters % 3
  first += quarters // 3 
  second += quarters // 3
  third += quarters // 3

  # deal with left over plays after distribution
  if remainder == 1: first += 1
  if remainder == 2: first += 1; second += 1
  plays += quarters
  quarters = 0

  # calculate quarters gained through wins
  if first // 35 > 0:
    quarters += (first // 35)*30
    first -= 35*(first // 35)


  if second // 100 > 0:
    quarters += (second // 100)*60
    second -= 100*(second // 100)


  if third // 10 > 0:
    quarters += (third // 10)*9
    third -= 10*(third // 10)

  # stop when the number of quarters reach 0
  if quarters == 0:
    break

print(f"Martha plays {plays} times before going broke.")

