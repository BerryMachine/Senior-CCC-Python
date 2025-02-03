N = int(input())
ordered = []
measurements = list(map(int, input().split()))
measurements.sort()

if N%2 == 0:
    half_N = N//2

    low = measurements[:half_N]
    high = measurements[half_N:]

    for i in range(half_N):
        ordered.append(low[half_N-i-1])
        ordered.append(high[i])

if N%2 != 0:
    half_N = N//2 + 1

    low = measurements[:half_N]
    high = measurements[half_N:]

    for i in range(half_N - 1):
        ordered.append(low[half_N-i-1])
        ordered.append(high[i])

    ordered.append(low[0])

print(*ordered)
