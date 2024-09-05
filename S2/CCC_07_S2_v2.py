# function to determine whether an item fits within a box given the dimensions
def check_fit(l, w, h, box_dimensions):
  # loop 3 times to account for rotating the item
  for i in range(3):
    if l <= box_dimensions[i]:
      if w <= box_dimensions[i-1] and h <= box_dimensions[i-2]:
        return True
      elif w <= box_dimensions[i-2] and h <= box_dimensions[i-1]:
        return True
  return False
    
boxes = []
fitting_boxes = []

for n in range(int(input())):
  l, w, h = map(int, input().split())
  v = l*w*h
  boxes.append([v, l, w, h])

boxes.sort(key=lambda x: x[0])

for m in range(int(input())):
  l, w, h = map(int, input().split())
  v = l*w*h
  fit_box = "Item does not fit."
  for box in boxes:
    if v <= box[0]:
      if check_fit(l, w, h, box[1:]):
        fit_box = box[0]
        break

  fitting_boxes.append(fit_box)
  
          

print(*fitting_boxes, sep="\n")
