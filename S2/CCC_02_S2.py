import math

numerator = int(input())
denominator = int(input())

rem = numerator % denominator
if rem == 0:
  print(numerator // denominator)
else:
  gcd = math.gcd(rem, denominator)

  if rem == numerator:
    print(numerator//gcd, "/", denominator//gcd, sep="")
  else:
    print(numerator // denominator, " ", rem//gcd, "/", denominator//gcd, sep="")
