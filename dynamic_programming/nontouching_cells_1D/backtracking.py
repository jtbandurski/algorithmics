input = [2,1,1,2,0]
# Find maximal sum of non touching cells
# in this case 2+2=4

def MainAlgo(a):
    # minus one for indexing
    n = len(a)-1
    return AlgoBack(a,n)

# 1. find backtracking solution
# a - array k - length
def AlgoBack(a, k):
    # out of bounds
    if k==-1:
        return 0
    # one element in list
    if k==0:
        return a[k]
    # check if you want to take k-th number
    # option 1 don take k-th: max value when considering k-1th
    # option 2 take k-th: value of k-th + max value when considering k-2th
    return max(AlgoBack(a, k-1), a[k] + AlgoBack(a, k-2))

print(MainAlgo(a=input))
