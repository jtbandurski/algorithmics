import sys
import numpy as np
sys.setrecursionlimit(1000)
input = [2,1,1,2,0]
# Find maximal sum of non touching cells
# in this case 2+2=4

def MainAlgo(a):
    # minus one for indexing
    n = len(a)
    # memoization dictionary
    global mem 
    mem = np.zeros(n)
    for k in range(n):
        AlgoDP(a,k)
    return int(mem[n-1])

# 1. find backtracking solution
# a - array k - length
def AlgoDP(a, k):
    # out of bounds
    if k==-1:
        mem[k] = 0
    # one element in list
    elif k==0:
        mem[k] = a[k]
    else:
        # check if you want to take k-th number
        # option 1 don take k-th: max value when considering k-1th
        # option 2 take k-th: value of k-th + max value when considering k-2th
        mem[k] = max(mem[k-1], a[k] + mem[k-2])
    return mem[k]

print(MainAlgo(a=input))
