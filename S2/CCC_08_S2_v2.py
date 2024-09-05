import math

while True:
    # get radius as input
    r = int(input())

    # exit program
    if r == 0:
        break

    quarter_count = 0
    # calculate number of integer points in a quadrant of the circle
    for x in range(0, r, 1):
        # for each integer x, determine the highest y coordinate that stays within the circle
        quarter_count += math.floor(math.sqrt(r**2 - x**2))

    print(quarter_count*4 + 1)
