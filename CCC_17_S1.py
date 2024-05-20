n = int(input())

swi = input().split()
sema = input().split()

#the same score it always possible on day 0
k_list = [0]

#counting variables
swi_total = 0
sema_total = 0

#determine the sum for every day and check if the score was the same or not
for day in range(n):
  swi_total += int(swi[day])
  sema_total += int(sema[day])

  if swi_total == sema_total:
    k_list.append(day+1)

#sorted the days list and use the largest value
print(sorted(k_list)[-1])
