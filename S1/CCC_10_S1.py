# keep track of best and second best computer and their corresponding scores
first = [False, 0]
second = [False, 0]

# loop through each computer
for n in range(int(input())):
  # get name, ram, cpu, and disk space as input
  name, R, S, D = input().split()
  # calculate score
  P = 2*int(R) + 3*int(S) + int(D)

  if P > second[1]:
    # if score is better than first, replace first with second and first with current
    if P > first[1]:
      second = first
      first = [name, P]

    # if score is equal to first...
    elif P == first[1]:
      # find lexicographically smallest name between first and current and set as first. Replace the second with the other.
      if name == min(name, first[0]):
        second = first
        first = [name, P]
      else:
        second = [name, P]

    # if score is only better than second, replace second with current
    else:
      second = [name, P]

    # if score is equal to second...
  elif P == second[1]:
    # find lexicographically smallest name between second and current and set as second
    if name == min(name, second[0]):
      second = [name, P]

# output the names of the two computers
if first[0] != False:
  print(first[0])
if second[0] != False:
  print(second[0])
