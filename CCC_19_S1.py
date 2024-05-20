things = [*input()]

#initial list
list = [1, 2, 3, 4]

#dictionary for horizontal and vertical flip commands
dict = {'H': 0, 'V': 0}

#adding to the dict based on things input of H and V
for letter in things: 
  if letter == 'H': dict['H'] += 1
  else: dict['V'] += 1

#determining if the number of H and V is even or odd, because 2 H/V's returns the set to its original state
mod_h = dict['H'] % 2
mod_v = dict['V'] % 2

#brute forced test cases because there are only 4
if mod_h == 1 and mod_v == 1:
  print(4, 3)
  print(2, 1)

elif mod_h == 1:
  print(3, 4)
  print(1, 2)

elif mod_v == 1:
  print(2, 1)
  print(4, 3)

else: 
  print(1, 2)
  print(3, 4)
