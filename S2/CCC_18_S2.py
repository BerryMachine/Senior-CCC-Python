def output(arr, degrees):
    # print(degrees)
    if degrees == 0:
        for i in range(N):
            print(*arr[i])
    if degrees == 180:
        for i in range(N):
            row = arr[N-i-1]
            row.sort()
            print(*row)
    if degrees == 90:
        for i in range(N):
            row = []
            for j in range(N):
                row.append(arr[j][N-i-1])
            print(*row)
    if degrees == 270:
        for i in range(N):
            row = []
            for j in range(N):
                row.append(arr[N-j-1][i])
            print(*row)

N = int(input())
arr = [[0]]*N

for i in range(N):
    arr[i] = list(map(int, input().split()))

if arr[0][0] < arr[0][N-1]:
    if arr[0][0] < arr[N-1][0]:
        output(arr, 0)
    else:
        output(arr, 270)
else:
    if arr[0][0] < arr[N-1][0]:
        output(arr, 90)
    else:
        output(arr, 180)
