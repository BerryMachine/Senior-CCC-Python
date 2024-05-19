from math import *
n = int(input())

vils = []
pops = []

for vek in range(n):
  vil = int(input())
  vils.append(vil)

vils = sorted(vils)

for i in range(1, len(vils)-1):
  A = (vils)[i-1]
  B = (vils)[i]
  C = (vils)[i+1]
  pop = abs(B - A)/2 + abs(C-B)/2
  pops.append(pop)

print(float(sorted(pops)[0]))
 

