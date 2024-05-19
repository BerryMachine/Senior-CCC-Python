import string

first_word = [*input()]
second_word = [*input()]

dict_A = {}
dict_B = {}

ans = "A"

for char in string.ascii_lowercase:
    dict_A[char] = 0
    dict_B[char] = 0

for letter in first_word:
    dict_A[letter] += 1

for letter in second_word: 
    if letter != "*":
        dict_B[letter] += 1

if dict_A == dict_B:
    ans = "A"
else: ans = "N"

print(ans)




