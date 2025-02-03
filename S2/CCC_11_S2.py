N = int(input())

ans_list = []
key_list = []

for i in range(N):
    ans = input()
    ans_list.append(ans)

for n in range(N):
    value = input()
    key_list.append(value)


cor_ans = 0

for i in range(N):
    if (ans_list[i] == key_list[i]):
        cor_ans += 1

print(cor_ans)