for i in range(int(input())):
  # get phone number as input
  x = input()
  
  # make new string with the converted phone number
  num = ""
  for i in range(len(x)):
    char = x[i]

    # ignore hyphens
    if char == "-":
      continue
  
    # add the corresponding number of each letter
    if char in ["A", "B", "C"]: num += "2"
    elif char in ["D", 'E', 'F']: num += "3"
    elif char in ["G", "H", "I"]: num += "4"
    elif char in ["J", "K", "L"]: num += "5"
    elif char in ["M", "N", "O"]: num += "6"
    elif char in ["P", "Q", "R", "S"]: num += "7"
    elif char in ["T", "U", "V"]: num += "8"
    elif char in ["W", "X", "Y", "Z"]: num += "9"
  
    # otherwise keep the same number
    else: num += char

  # add hyphens
  num = num[:3] + "-" + num[3:6] + "-" + num[6:10]
    
  print(num)
