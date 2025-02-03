# current cursor coordinates
xcursor = 0
ycursor = 0

# window dimensions
c, r = map(int, input().split())

# loop until (0, 0) input
while True:
    # get mouse movement
    x, y = map(int, input().split())

    # exit
    if x == 0 and y == 0:
        break

    # move cursor
    xcursor += x
    ycursor += y

    # boundary handling for x
    if xcursor > c: xcursor = c
    elif xcursor < 0: xcursor = 0
    # boundary handling for y
    if ycursor > r: ycursor = r
    elif ycursor < 0: ycursor = 0

    # output
    print(xcursor, ycursor)

