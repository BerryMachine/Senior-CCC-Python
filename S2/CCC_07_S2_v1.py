n = int(input())
box_list = []

for i in range(n):
  box = input().split()
  box = [int(i) for i in box]
  box_list.append(sorted(box))

m = int(input())

item_list = []

for i in range(m):
  item = input().split()
  item = [int(i) for i in item]
  item_list.append(sorted(item))


for item in item_list:
  size_list = []
  for box in box_list:
    
    if item[1] <= box[1] and item[0] <= box[0] and item[2] <= box[2]:
      size_list.append(box[0]*box[1]*box[2])

  if len(size_list) > 0:
    print(sorted(size_list)[0])
  else: print("Item does not fit.")
