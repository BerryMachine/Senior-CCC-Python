numbers = []
for i in range(int(input())):
  if not (number := int(input())):
    numbers.pop()
  else:
    numbers.append(number)
print(sum(numbers))
