TP = []
X = 0
max_X = 0

N = int(input())

# append all time (T) and corresponding position (P) values into an array
for n in range(N):
  TP.append(list(map(int, input().split())))

# sort the array by time
TP.sort(key=lambda x: x[0])

# iterate through each adjacent pair of TP in the array
for i in range(N-1):
  # calculate speed
  diff_T = TP[i+1][0] - TP[i][0]
  diff_P = abs(TP[i+1][1] - TP[i][1])
  X = diff_P / diff_T

  # store lowest speed
  if X > max_X:
    max_X = X

print(max_X)
