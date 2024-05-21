columns = int(input())
row_one = input().split()
row_two = input().split()

row_check = 0
column_check = 0
num_of_ones = 0

adj = 0

for i in range(columns):
  if int(row_one[i]) == 1: num_of_ones += 1
  if int(row_two[i]) == 1: num_of_ones += 1

#row one sideways
for i in range(columns-1):
  if int(row_one[i]) == 1:
    if int(row_one[i+1]) == 1: adj += 1

#row two sideways
for i in range(columns-1):
  if int(row_two[i]) == 1:
    if int(row_two[i+1]) == 1: adj += 1


for i in range(0, columns, 2):
  if int(row_one[i]) == 1 and int(row_two[i]) == 1: adj += 1


print(3*num_of_ones - 2*adj)
