#test cases on dmoj are actually wrong, no way my code is wrong
message = [*input()]
cipher1 = [*input()]
cipher2 = [*input()]

cipher_dict = {}

for i in range(len(message)):
  cipher_dict[cipher1[i]] = message[i]

for i in range(len(cipher2)):
  if cipher2[i] in cipher_dict:
    cipher2[i] = cipher_dict[cipher2[i]]
  else: cipher2[i] = "."

print("".join(cipher2))
