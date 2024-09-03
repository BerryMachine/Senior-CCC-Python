from math import *
n = int(input())

# villages coordinate list
vils = []

# populations of the villages list
pops = []

# add values into the villages list from input
for vek in range(n):
  vil = int(input())
  vils.append(vil)

# sort village coordinates to resemble numberline
vils = sorted(vils)

# A is the city before B
# B is the city in question
# C is the city after B
# **note**: we can disregard the first and last city in the village list 
for i in range(1, len(vils)-1):
  A = (vils)[i-1]
  B = (vils)[i]
  C = (vils)[i+1]

  # use the difference of the values to get population
  pop = abs(B - A)/2 + abs(C-B)/2

  # add to the population list
  pops.append(pop)

# output the sorted version fo pops, the smallest value
print(float(sorted(pops)[0]))
 

