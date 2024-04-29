# get goal scorer's jersey number as input
J = int(input())

# the number of possible combinations is the (J - 3)th tetrahedral number.
# the formula for the nth tetrahedral number is n(n+1)(n+2)/6
print((J - 3) * ((J - 3) + 1) * ((J - 3) + 2) // 6)
