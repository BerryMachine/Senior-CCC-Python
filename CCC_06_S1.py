# get parent alleles as input
B = input()
A = input()
# get number of test cases as input
X = int(input())

# find all possible traits of baby
possible_traits = [[], [], [], [], []]

# check each pair in B and A
for i in range(0, 10, 2):
  # if there are any uppercase letters, the attribute of the dominant allele is possible
  if not B[i:i+2].islower() or not A[i:i+2].islower():
    possible_traits[i//2].append(True)

  # if there are lowercase letters in both alleles, the attribute of the recessive allele is possible
  if not B[i:i+2].isupper() and not A[i:i+2].isupper():
    possible_traits[i//2].append(False)

# if all traits of baby are possible, print "Possible baby."
for j in range(X):
  baby = input()
  if baby[0].isupper() not in possible_traits[0]: print("Not their baby!")
  elif baby[1].isupper() not in possible_traits[1]: print("Not their baby!")
  elif baby[2].isupper() not in possible_traits[2]: print("Not their baby!")
  elif baby[3].isupper() not in possible_traits[3]: print("Not their baby!")
  elif baby[4].isupper() not in possible_traits[4]: print("Not their baby!")
  else: print("Possible baby.")
