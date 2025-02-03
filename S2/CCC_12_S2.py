dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

stringin = input()

total_value = 0

for i in range(0, len(stringin)-3, 2):
    if dict[stringin[i+1]] < dict[stringin[i+3]]:
        total_value -= int(stringin[i])*dict[stringin[i+1]]
    else:
        total_value += int(stringin[i])*dict[stringin[i+1]]

total_value += int(stringin[-2])*dict[stringin[-1]]

print(total_value)