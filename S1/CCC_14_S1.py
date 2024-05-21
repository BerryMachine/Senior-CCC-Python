# get number of friends and rounds as input
K = int(input())
m = int(input())

# create a list of friends from 1 to K
prev_list = []
updated_list = [friend for friend in range(1,K+1)]

# iterate through the rounds
for i in range(m):
  # set updated_list to empty list
  prev_list = updated_list
  updated_list = []

  # get interval for removal as input
  r = int(input())

  # iterate through the list and omit every rth element
  for j in range(len(prev_list)):
    if (j+1) % r != 0:
      updated_list.append(prev_list[j])

# print the remaining friends
for i in updated_list:
  print(i)
