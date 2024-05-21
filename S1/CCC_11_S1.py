num_of_s = 0
num_of_t = 0

for N in range(int(input())):
  # split string into array of letters
  line = [*input()]

  # count number of each letter
  for letter in line:
    if letter == "T" or letter == "t":
      num_of_t += 1
    if letter == 'S' or letter == "s":
      num_of_s += 1

# output most likely language
if num_of_t > num_of_s:
  print("English")
else: print("French")
  
