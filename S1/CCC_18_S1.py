# number of villages
N = int(input())

# villages coordinate list
V = []
for i in range(N):
  V.append(int(input()))

# sort villages' coordinates ascending
V.sort()

# keep track of smallest village size
min_size = -1

# A is the city before B
# B is the city in question
# C is the city after B
# **note**: we can disregard the first and last city in the village list 
for i in range(1, len(vils)-1):
  A = V[i-1]
  B = V[i]
  C = V[i+1]

  # determine size of village
  size = (B - A)/2 + (C - B)/2
  # determine whether it is the smallest thus far
  if vil_size < min_size or min_size == -1:
        min_size = vil_size

print(min_size)
