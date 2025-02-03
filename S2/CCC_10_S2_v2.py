k = int(input())

# dictionary with binary codes as keys and respective characters as values
char_dict = {}

# setup encoding
for i in range(k):
    char, code = map(str, input().split())
    char_dict[code] = char

# sequence to decode
sequence = input()
decoded = ""

# substring slice indices
start = 0
end = 1

# loop through binary sequence
for i in range(len(sequence)):
    # get slice
    slice = sequence[start:end]

    # check if slice is valid code
    if slice in char_dict.keys():
        # add to decoded string
        decoded += char_dict[slice]
        start = end # next slice
    
    # increment slice
    end += 1

# output
print(decoded)
