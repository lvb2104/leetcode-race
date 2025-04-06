x = [0] * 15
def solve(i):
    for j in range(2): # x[i] can be 0 or 1
        x[i] = j # set x[i] to 0 or 1
        if i == 4: # if we are at the last index
            print(x[:5]) # print the first 5 elements
        else: # if we are not at the last index
            solve(i + 1) # recursively call solve for the next index


solve(0) # start with x[0]