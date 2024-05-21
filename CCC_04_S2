n, k = input().split()
n, k = int(n), int(k)

dict = {}

for i in range(n):
  dict[i] = {"rank": 0, "score": 0, "badrank": 0}

for round in range(k):
  scores = input().split()
  rank_list = []
  
  for change in range(n):
    dict[change]["score"] += int(scores[change])
    rank_list.append([change, dict[change]["score"]])
    
  rank_list.sort(key=lambda x: x[1])
  
  for value in rank_list:
    dict[value[0]]["rank"] = n - (rank_list.index(value))
    
    if dict[value[0]]["rank"]> dict[value[0]]['badrank']:
      dict[value[0]]["badrank"] = dict[value[0]]['rank']

win_list = []

for i in range(n-1, 1, -1):
  if rank_list[i][1] == rank_list[i-1][1]:
    win_list.append(rank_list[i-1][1])
  else: break


win_list.append(rank_list[-1])
win_list.sort(key=lambda x: x[0])

x = win_list[0][0] + 1
y = dict[win_list[0][0]]["score"]
z = dict[win_list[0][0]]["badrank"]
print(f"Yodeller {x} is the TopYodeller: score {y}, worst rank {z}")




      
    
  
    
  

  
