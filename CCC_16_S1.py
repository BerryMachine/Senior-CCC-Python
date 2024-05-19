#import string library
import string

#input the word
word1 = [*input()]
word2 = [*input()]

#initialize dictionaries
dicta = {}
dictb = {}

#initialize ans variable
ans = "N"

#create dictionaries with lowercase alphabet keys
for char in string.ascii_lowercase:
	dicta[char] = 0
	dictb[char] = 0

#add number values to the keys
for letter in word1:
	dicta[letter] += 1
  
#add number values to the keys
for letter in word2:
	if letter != "*": dictb[letter] += 1

#determine if anagram is possible by checking if dictb values are less than  or equal dicta
for value in dicta:
	if dictb[value] <= dicta[value]: ans = "A"
	else: ans = "N"; break

#printing answer
print(ans)
