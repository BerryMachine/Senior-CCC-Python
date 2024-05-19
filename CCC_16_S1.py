from collections import Counter

is_wildcard = True
S = Counter(input())
W = Counter(input())

print(S)
print(W)

<<<<<<< HEAD
ans = "A"

for char in string.ascii_lowercase:
  dict_A[char] = 0
  dict_B[char] = 0

# print(dict_A)
# print(dict_B)

for letter in first_word:
  dict_A[letter] += 1

for letter in second_word: 
    dict_B[letter] += 1

if len(first_word) == len(second_word):
    for char in dict_A:
        if dict_A[char] != dict_B[char]:
            print("N")
            break
            
        else: counter += 1

    if counter == 26: print("A")
else: print("N")

=======
for i in W:
  print(i)
  if i != "*":
    if W[i] < S[i]:
      print("what the monkey")
      diff = W[i] - S[i]
      
      try:
        if W["*"] >= diff:
          print("wHatat")
          W["*"] -= diff
        else:
          is_wildcard = False
          print("N")
          break
          
      except KeyError:
        is_wildcard = False
        print("N")
        break

    elif W[i] > S[i]:
      is_wildcard = False
      print("N")
      break

if is_wildcard:
  print("A")
>>>>>>> 4589d9c42436ffb084db36a47a2c655b85bea1fc
