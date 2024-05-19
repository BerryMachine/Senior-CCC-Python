import string

first_word = [*input()]
second_word = [*input()]

dict_A = {}
dict_B = {}

counter = 0

for char in string.ascii_lowercase:
    dict_A[char] = 0
    dict_B[char] = 0

for letter in first_word:
    dict_A[letter] += 1

for letter in second_word: 
    dict_B[letter] += 1

if len(first_word) == len(second_word):
    for char in dict_A:
        if dict_A[char] != dict_B[char]:
            print("N")
            break
            
        else: counter += 1

    if counter == 26: print("A")
else: print("N")

