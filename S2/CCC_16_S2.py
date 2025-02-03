question = input()
N = int(input())
d_speeds = list(map(int, input().split()))
p_speeds = list(map(int, input().split()))

d_speeds.sort()
p_speeds.sort()

ans = 0

# minimum total speed
if question == "1":
    for i in range(N):
        ans += max(d_speeds[i], p_speeds[i])

elif question == "2":
    for i in range(N):
        ans += max(d_speeds[i], p_speeds[N-i-1])

print(ans)
