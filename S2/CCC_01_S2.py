# adjust direction matrix to make a left turn in spiral
def leftTurn(directions, count_to_turn):
  if directions[0] == 0:
    directions[0] = -directions[1]
    directions[1] = 0
    return directions, count_to_turn
  
  else:
    directions[1] = directions[0]
    directions[0] = 0
    # increase length of countdown to next left turn by 1 after moving horizontally
    return directions, count_to_turn + 1

# get start and end integer as input
start = int(input())
end = int(input())
# starting coordinates
x = 0
y = 0
# keep track of numbers in each row to facilitate output formatting
rows = {y: [start]}
# adjusting matrix to generate spiral
directions = [0, -1]
# count to left turn in spiral
count = 0
count_to_turn = 1

# generate spiral using coordinates
for i in range(start+1, end+1):
  # add adjusting matrix
  x += directions[0]
  y += directions[1]
  
  # save integer in its corresponding row
  if y in rows.keys():
    # **Note**: an integer is always placed on the far right or left in its row
    # determine where to store the integer in the row
    if directions[0] == 1 or directions[1] == 1:
      rows[y].append(i)
    else:
      rows[y].insert(0, i)

  else:
    rows[y] = [i]

  # increment count
  count += 1

  # perform left turn
  if count == count_to_turn:
    directions, count_to_turn = leftTurn(directions, count_to_turn)
    count = 0
  
# output each row from top to botom
min_x = -(len(rows)//2) - 1
max_x = len(rows) + min_x
for j in range(max_x, min_x, -1):
  print(*rows[j])
