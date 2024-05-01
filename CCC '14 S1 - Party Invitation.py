#take all input required
k = int(input())
m = int(input())

list = []

#add initial values into to the list
for i in range(1,k+1):
  list.append(i)

#run as many times as the value of m
for i in range(m):
  num = int(input())
  counter = 0

  #uses the for loop values to determine numbers at certain intervals
  for value in range(num, len(list)+1, num):
    #sets the values to be removed to zero
    list[value-1] = 0
    counter += 1

  #remove all the zeros from the list
  for i in range(counter):
    list.remove(0)

#sort the list from least to greatest
list.sort()

#print out all the values in the list
for thing in list:
  print(thing)
