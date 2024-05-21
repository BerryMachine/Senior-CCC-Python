from math import *
n = int(input())

#villages coordinate list
vils = []

#populations of the villages list
pops = []

#adding values into the villages list from input
for vek in range(n):
  vil = int(input())
  vils.append(vil)

#sorteding village coordinates to resemble numberline
vils = sorted(vils)

#A is the city before B
#B is the city being compared
#C is the city after B
#note: the first and last city in the village list don't matter
for i in range(1, len(vils)-1):
  A = (vils)[i-1]
  B = (vils)[i]
  C = (vils)[i+1]

  #used the difference of the values to get population
  pop = abs(B - A)/2 + abs(C-B)/2

  #added to the population list
  pops.append(pop)

#printed the sorted version fo pops, the smallest value
print(float(sorted(pops)[0]))
 

