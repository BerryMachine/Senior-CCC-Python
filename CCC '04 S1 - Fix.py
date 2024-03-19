# loop N times
for N in range(int(input())):
  word1 = input() 
  word2 = input()
  word3 = input()
  # store lengths or each word
  len1 = len(word1)
  len2 = len(word2)
  len3 = len(word3)
  # keep track of if they are fixfree
  fixfree = True

  # check if 1st or 2nd word are a fix of each other
  if word2[:len1] == word1 or word2[-len1:] == word1 or word1[:len2] == word2 or word1[-len2:] == word2:
    fixfree = False
    
  # check if 1st or 3rd word are a fix of each other
  if word3[:len1] == word1 or word3[-len1:] == word1 or word1[:len3] == word3 or word1[-len3:] == word3:
    fixfree = False
    
  # check if 2nd or 3rd word are a fix of each other
  if word3[:len2] == word2 or word3[-len2:] == word2 or word2[:len3] == word3 or word2[-len3:] == word3:
    fixfree = False

  # if not, they are fixfree
  print("Yes" if fixfree else "No")
