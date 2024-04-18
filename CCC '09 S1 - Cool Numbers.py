a = int(input())
b = int(input())

num = 0

for i in range(10000):
  #For a number to a cube and square, it had to be a number with a power of 6
  if i**6 > b:
    break
  #adding to the num value if i to the 6th power is between a and b
  if a <= i**6 <= b: num += 1;


print(num)
