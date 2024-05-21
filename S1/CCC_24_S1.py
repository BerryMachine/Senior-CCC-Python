num_of_people = int(input())
people_dict = {}
diameter = int(num_of_people/2)

for i in range(num_of_people):
  people_dict[str(i+1)] = int(input())

counter = 0

for i in range(num_of_people):
  if i+1 <= diameter:
    if people_dict[str(i+1)] == people_dict[str(i+1+diameter)]:
      counter += 1
  elif i+1 > diameter:
    if people_dict[str(i+1)] == people_dict[str(i+1-diameter)]:
      counter += 1
  
print(counter)
