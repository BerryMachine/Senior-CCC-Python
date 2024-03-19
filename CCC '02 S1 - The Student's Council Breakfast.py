# get cost of each ticket as input
cost_pink = int(input())
cost_green = int(input())
cost_red = int(input())
cost_orange = int(input())

# get desired amount of money as input
money_req = int(input())
overall_min = 200000000

# keep track of total amount combinations
count = 0

# loop through all possible combinations of tickets
for orange in range(money_req//cost_orange + 1):
  # get remainder after orange tickets
  rem = money_req - orange*cost_orange

  for red in range(rem//cost_red + 1):
    # get remainder after orange & red tickets
    rem2 = rem - red*cost_red

    for green in range(rem2//cost_green + 1):
      # get remainder after orange, red, & green tickets
      rem3 = rem2 - green*cost_green

      for pink in range(rem3//cost_pink + 1):  
        # if total cost of tickets is equal to desired amount of money
        if rem3 - pink*cost_pink == 0: 
          count += 1
          # calculate minimum number of tickets needed
          overall_min = min(overall_min, (pink + green + red + orange))
          print(f"# of PINK is {pink} # of GREEN is {green} # of RED is {red} # of ORANGE is {orange}")

print(f"Total combinations is {count}.")
print(f"Minimum number of tickets to print is {overall_min}.")
