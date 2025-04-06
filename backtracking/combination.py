x = [0] * 15
n = 10
k = 5
def solve(i):
    for j in range(x[i - 1] + 1, n - (k - i) + 1): # x[i] can be from x[i - 1] + 1 to n - (k - i)
        x[i] = j # set x[i] to j
        if i == k: # if we are at the last index
            print(x[1:k + 1]) # print the first k elements
        else: # if we are not at the last index
            solve(i + 1) # recursively call solve for the next index

solve(1) # start with x[1]