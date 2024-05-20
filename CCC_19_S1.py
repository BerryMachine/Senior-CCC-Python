things = [*input()]

list = [1, 2, 3, 4]

dict = {'H': 0, 'V': 0}

for letter in things: 
  if letter == 'H': dict['H'] += 1
  else: dict['V'] += 1

mod_h = dict['H'] % 2
mod_v = dict['V'] % 2

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
