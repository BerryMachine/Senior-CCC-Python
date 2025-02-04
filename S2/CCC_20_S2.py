M = int(input())
N = int(input())


array_list = []

for i in range(M):
    value = input().split()
    array_list.append(value)


ans = N*M

print(ans)

ans_list = []


for m in range(M):
    for n in range(N):
        if array_list[m][n] == ans:
            ans_list.append([m, n])




#1. Determine the squares I can jumps
#2. Determine the validity of the jumps

#6 determine all factors
# ans = M*N

# determine the value I need to get to the last square
# then determine the squares that have the x value
# this determine if 