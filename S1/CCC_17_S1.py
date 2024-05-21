N = int(input())

# store the number of runs each day by each time in a list
Sw_runs = list(map(int, input().split()))
Se_runs = list(map(int, input().split()))

# store all possible days K
K_list = [0]

# counting variables
Sw_total = 0
Se_total = 0

for day in range(N):
  # add the runs of each team for each day
  Sw_total += Sw_runs[day]
  Se_total += Se_runs[day]

  # store day if the total runs of each team is equal
  if Sw_total == Se_total:
    K_list.append(day + 1)

# output largest value
print(K_list[-1])
