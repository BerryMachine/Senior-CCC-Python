flip_seq = input()

# count number of each H and V flips
H_count = flip_seq.count("H")
V_count = flip_seq.count("V")

# every 2 flips in the same direction cancel out
# therefore, we only need to consider the (count mod 2) flip(s) in each direction
# output the respective grid layout
if H_count % 2 == 0:
    if V_count % 2 == 0:
        print("1 2")
        print("3 4")
    else:
        print("2 1")
        print("4 3")

else:
    if V_count % 2 == 0:
        print("3 4")
        print("1 2")
    else:
        print("4 3")
        print("2 1")
