import math

# get fraction as input
numerator = int(input())
denominator = int(input())

# calculate remainder
rem = numerator % denominator

# output if integer
if rem == 0:
  print(numerator // denominator)
  
else:
  # calculate gcd to reduce fraction
  gcd = math.gcd(rem, denominator)

  # if fraction < 1, output reduced fraction
  if rem == numerator:
    print(f"{numerator//gcd}/{denominator//gcd}")
    
  # if fraction > 1, output reduced mixed fraction
  else:
    print(f"{numerator//denominator} {rem//gcd}/{denominator//gcd}")
#jlkdfjlakdjf