import math

# get fraction as input
numerator = int(input())
denominator = int(input())

# calculate remainder after division
rem = numerator % denominator

# if fraction is integer, output integer
if rem == 0:
  print(numerator // denominator)
  
else:
  # calculate gcd to reduce fraction
  gcd = math.gcd(rem, denominator)

  # if fraction < 1, output reduced fraction
  if rem == numerator:
    print(numerator//gcd, "/", denominator//gcd, sep="")
    
  # if fraction > 1, output reduced mixed fraction
  else:
    print(numerator // denominator, " ", rem//gcd, "/", denominator//gcd, sep="")
