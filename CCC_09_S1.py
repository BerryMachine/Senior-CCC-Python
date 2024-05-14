a = int(input())
b = int(input())

num = 0

for i in range(10000):
  # numbers that are both a cube and square must be an integer to the power of 6.
  if i**6 > b:
    break
  # increase num if i to the 6th power is between a and b
  if a <= i**6 <= b: num += 1;


print(num)
