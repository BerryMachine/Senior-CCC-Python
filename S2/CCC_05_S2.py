c, r = input().split()
c, r = int(c), int(r)

new_x = 0
new_y = 0

while True: 
  x, y = input().split()
  x, y = int(x), int(y)
  
  new_x +=  x
  new_y += y
  
  if new_x > c: new_x = c;
  if new_x < 0: new_x = 0;
  if new_y > r: new_y = r;
  if new_y < 0: new_y = 0;

  if x == 0 and y == 0:
    break

  print(new_x,new_y)
