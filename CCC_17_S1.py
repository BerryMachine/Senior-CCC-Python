n = int(input())

swi = input().split()
sema = input().split()

k_list = [0]

swi_total = 0
sema_total = 0

for day in range(n):
  swi_total += int(swi[day])
  sema_total += int(sema[day])

  if swi_total == sema_total:
    k_list.append(day+1)

print(sorted(k_list)[-1])
