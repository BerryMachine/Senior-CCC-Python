# get number of quarters as input
quarters = int(input())

# get number of times each machine has been played
first = int(input())
second = int(input())
third = int(input())

#Keeping track of plays
plays = 0

while True:
  #Adding plays to each machine based on number of quarters
  remainder = quarters % 3
  first += quarters // 3 
  second += quarters // 3
  third += quarters // 3

  #Dealing with left over plays after distribution
  if remainder == 1: first += 1
  if remainder == 2: first += 1; second += 1

  #The plays is basically the amount of quarters
  plays += quarters

  #making quarters zero because the quarter are used up in the plays
  quarters = 0

  
  #checking for wins if get more squart to distribute again
  if first // 35 > 0:
    quarters += (first // 35)*30
    first -= 35*(first // 35)


  if second // 100 > 0:
    quarters += (second // 100)*60
    second -= 100*(second // 100)


  if third // 10 > 0:
    quarters += (third // 10)*9
    third -= 10*(third // 10)

  #If there are no more quarter, there can be no plays
  if quarters == 0:
    break

#after the plays are summed up, this is printing it
print(f"Martha plays {plays} times before going broke.")

