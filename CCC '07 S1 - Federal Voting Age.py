for n in range(int(input())):
  # get year, month, day as input
  y, m, d = map(int, input().split())

  # check if age is under 18
  if y > 1989:
    print("No")

  elif y == 1989 and m > 2:
    print("No")

  elif y == 1989 and m == 2 and d > 27:
    print("No")

  else: print("Yes")
