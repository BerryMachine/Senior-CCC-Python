# get year as input
Y = int(input())
D = Y

while True:
  # increment by 1 year
  D += 1
  next_year = str(D)
  
  # keep track of unique digits
  unique = []
  
  # loop through each digit in the year
  for char in next_year:
    # if digit is not unique, check next year
    if char in unique:
      break
    # track existing digits
    else:
      unique.append(char)

  # stop if year is has all unique digits
  if len(unique) == len(next_year):
    break

print(D)
  
