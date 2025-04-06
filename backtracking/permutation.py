x = [0] * 10
used = [0] * 10 # used[j] = 1 means j is used
def solve(i):
    for j in range(10): # x[i] can be 0 to 9
        if used[j] == 0: # if j is not used
            used[j] = 1 # mark j as used
            x[i] = j # set x[i] to j
            if i == 9: # if we are at the last index
                print(x) # print the entire array
            else: # if we are not at the last index
                solve(i + 1) # recursively call solve for the next index
            used[j] = 0 # unmark j because we are done with x[i] = j

solve(1)
