n = int(input())

height = input().split()

width = input().split()

trap_dict = {}

total_area = 0

for i in range(0, n, 1):
  trap_dict[i] = {'h1': int(height[i]), 'h2':int(height[i+1]) , 'w1': int(width[i]) }

for key in trap_dict:
  h1 = trap_dict[key]["h1"]
  h2 = trap_dict[key]["h2"]
  w1 = trap_dict[key]["w1"]
  if h1 > h2: 
    rec_area = h2*w1
    tri_area = ((h1 - h2)*w1)/2
  else: 
    rec_area = h1*w1
    tri_area = ((h2 - h1)*w1)/2

  total_area += rec_area
  total_area += tri_area

print(total_area)
