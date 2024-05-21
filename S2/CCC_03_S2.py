N = int(input())

for i in range(N):
  list = []
  for i in range(4):
    line = [*input().lower().split()[-1]]
    
    for x in range(len(line)-1, 0, -1):
      if line[x] in ["a", "e", "i", "o", "u"]:
        list.append("".join(line[x:]))
        break

    if len(list) != i + 1:
      list.append("".join(line))
      
  if list[0] == list[1] == list[2] == list[3]:
    print("perfect")
  elif list[0] == list[1] and list[2] == list[3]:
    print("even")
  elif list[0] == list[2] and list[1] == list[3]:
    print("cross")
  elif list[0] == list[3] and list[1] == list[2]:
    print("shell")
  else: print("free")


    
