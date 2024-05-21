n, k = input().split()
n, k = int(n), int(k)
dict = {}

for value in range(n):
  dict[value] = {"rank": 0, "score": 0, "low_rank": 0}

for round in range(k):
  scores  = input().split()

  #adding the score into the dictionary
  for value in range(n):
    dict[value]["score"] += int(scores[value])

  #determine the rank after every round
  rank_list = []
  
  for rank in range(n):
    rank_list.append([rank, dict[rank]["score"]])

  for x in rank_list:
    j = 0
    
    for i in rank_list:
      if x[1] < i[1]: j += 1

    dict[x[0]]["rank"] = j + 1
    if dict[x[0]]["rank"] > dict[x[0]]["low_rank"]:
      dict[x[0]]["low_rank"] = dict[x[0]]["rank"] 

  #determine the printing for the winner
rank_list.sort(key=lambda x: x[1])
win_list = []

for value in range(len(rank_list)-1):
  if rank_list[-1][1] == rank_list[value][1]:
    win_list.append(rank_list[value])

win_list.append(rank_list[-1])

win_list.sort(key=lambda x: x[0])

for i in range(len(win_list)):
  x = win_list[i][0] + 1
  y = win_list[i][1]
  z = dict[win_list[i][0]]["low_rank"]
  print(f"Yodeller {x} is the TopYodeller: score {y}, worst rank {z}")
