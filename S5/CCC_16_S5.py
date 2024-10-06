# determine cell state in generation K
# Mathematically: cell[i] = cell[i - 2^K] XOR cell[i + 2^K]
def findCell(gen, i, K, N):
    b = gen[i-(1<<K)%N]
    c = gen[(i+(1<<K)%N)%N] # modulo N to avoid indexError
    a = 0 if b == c else 1 # XOR
    return a

# get number of cells and desired generation as input
N, T = map(int, input().split())
# initial states of cells
generation1 = [*input()]
generation2 = generation1.copy()
switch = False
shift = 0

# iterate through each 1 (right to left) in the binary representation of T
while T != 0:
    if T&1 != 0:
        # iterate through each cell
        for j in range(N):
            if switch:
                generation1[j] = findCell(generation2, j, shift, N)
            else:
                generation2[j] = findCell(generation1, j, shift, N)

        switch = not switch   

    # shift binary representation of T
    T >>= 1
    shift += 1

if switch:
    print(*generation2, sep="")
else:
    print(*generation1, sep="")
