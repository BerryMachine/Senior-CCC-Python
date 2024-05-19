from collections import Counter

is_wildcard = True
S = Counter(input())
W = Counter(input())


for i in W:

  if i != "*":
    if W[i] > S[i]:
      is_wildcard = False
      print("N")
      break
      
    elif W[i] < S[i]:
      diff = S[i] - W[i]
      
      try:
        if W["*"] >= diff:
          W["*"] -= diff
        else:
          is_wildcard = False
          print("N")
          break
          
      except KeyError:
        is_wildcard = False
        print("N")
        break

if is_wildcard:
  print("A")
