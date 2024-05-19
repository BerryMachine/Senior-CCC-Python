from collections import Counter

# store the count of each letter using Counter module
S = Counter(input())
W = Counter(input())

# question states both words have same amount of characters
# thus its not possible for the amount of a certain letter in the wildcard word to be greater than the original string: 
ans = "A"
for value in S:
	if W[value] > S[value]: ans = "N"; break

print(ans)
