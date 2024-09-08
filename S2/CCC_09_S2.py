num_row = int(input())
num_len = int(input())

rows_list = []
ans_list = []

for rows in range(num_row):
    value = input().split()
    rows_list.append(value)

ans_list.append(rows_list[-1])

for first in range(num_row-1):

    var = rows_list[first]

    for row in rows_list[first+1:]:
        for i in range(num_len):
            if row[i] != var[i]:
                var[i] = "1"
            elif row[i] == "1" and var[i] == "1":
                var[i] = "0"
            elif row[i] == "0" and var[i] == "0":
                var[i] = "0"
            
    if var not in ans_list:
        ans_list.append(var)

print(len(ans_list))
