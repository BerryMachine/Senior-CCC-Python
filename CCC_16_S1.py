from collections import Counter

is_wildcard = True
S = Counter(input())
W = Counter(input())

print(S)
print(W)

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
