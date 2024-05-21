n = int(input())
ways = 0

for i in range(n//4 + 1):
  rem = n - i*4
  if rem % 5 == 0:
    ways += 1

print(ways)

