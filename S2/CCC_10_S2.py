
#rewrite this in list format instead of dictionary
num_of_char = int(input())

char_dict = {}
char_list = []

for i in range(num_of_char):
    value = input().split()
    char_dict[value[0]] = value[1]
    char_list.append(value[0])

binary_input = input()

slice_start = 0
slice_end = 1
button = 1

while True:
    input_portion = binary_input[slice_start: slice_end]

    for keys in char_dict:
        if char_dict[keys] == input_portion:
            slice_start += len(input_portion)
            slice_end = slice_start  + 1
            button = 1
            print(keys, end = '')
        else: button = 0

    if button == 0:
        slice_end += 1

    if slice_start == len(binary_input):
        break
