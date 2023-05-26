import sys
sys.setrecursionlimit(1000)
input = [2,1,1,2,0]
# Find maximal sum of non touching cells
# in this case 2+2=4

def MainAlgo(a):
    # memoization dictionary
    global mem 
    mem = dict()
    # minus one for indexing
    n = len(a)-1
    return AlgoMem(a,n)

# 1. find backtracking solution
# a - array k - length
def AlgoMem(a, k):
    # out of bounds
    if k==-1:
        mem[k] = 0
    # one element in list
    if k==0:
        mem[k] = a[k]
    # if already calcualted take value from dictionary
    if k not in mem:
        
        # check if you want to take k-th number
        # option 1 don take k-th: max value when considering k-1th
        # option 2 take k-th: value of k-th + max value when considering k-2th
        mem[k] = max(AlgoMem(a, k-1), a[k] + AlgoMem(a, k-2))
    return mem[k]

print(MainAlgo(a=input))
