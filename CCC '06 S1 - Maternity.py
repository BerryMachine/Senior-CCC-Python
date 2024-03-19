#parent genetic
B = input()
# disecting the list into 5 parts
B = [B[i:i+2] for i in range(0, 10, 2)]
#parent genetic
A = input()
# disecting the list into 5 parts
A = [A[i:i+2] for i in range(0, 10, 2)]

#number of children values to compare
X = input()

#list of letters
letter_list = ["a", "b", "c", "d", "e"]

dict = {"a": [], "b": [], "c": [], "d": [], 'e': []}

# if Capital in atleast one list capital is possibility, and lower in both lists
# lower is possibility
for i in range(len(letter_list)):
  if letter_list[i].upper() in [*B[i]] or letter_list[i].upper() in [*A[i]]:
    dict[letter_list[i]].append(letter_list[i].upper())
  if letter_list[i] in [*B[i]] and letter_list[i] in [*A[i]]:
    dict[letter_list[i]].append(letter_list[i])

#Checking dict list to check is possibility is correct and printing values
for i in range(int(X)):
  thing = [*input()]
  if thing[0] not in dict["a"]: print("Not their baby!")
  elif thing[1] not in dict["b"]: print("Not their baby!")
  elif thing[2] not in dict["c"]: print("Not their baby!")
  elif thing[3] not in dict["d"]: print("Not their baby!")
  elif thing[4] not in dict["e"]: print("Not their baby!")
  else: print("Possible baby.")
