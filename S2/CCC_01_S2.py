import math

start_int = int(input())
end_int = int(input())
width = 0
check_width = 0
height = 1
check_height = 1

while True:
  width += 1
  check_width += width * 2
  if end_int - start_int < check_width:
    break

while True:
  if end_int - start_int < check_height:
    break
  check_height += height * 2 + 1
  height += 1

x_mid = math.ceil(width/2)
y_mid = math.ceil(height/2)

nums = {}
nums[start_int] = [x_mid, y_mid]

w = 2
ww = 1
h = 1
hh = 1
direction_w = 1
direction_h = 1
horizontal = -1
n = start_int
x = x_mid
y = y_mid

for i in range(end_int - start_int):
  n += 1
  if horizontal == 1:
    x += direction_w
  else:
    y += direction_h

  nums[n] = [x, y]

  if n - start_int == w:
    ww += 1
    w = w + ww*2
    horizontal *= -1
    direction_w *= -1

  elif n - start_int == h:
    h = h + hh*2 + 1
    hh += 1
    horizontal *= -1
    direction_h *= -1

for i in range(1, height+1):
  list = []
  for j in range(1, width+1):
    coordinates = [j, i]
    for num in nums:
      if coordinates == nums[num]:
        list.append(num)


  print(*list)
