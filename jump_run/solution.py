import sys
import os
import numpy as np

# global variables
INF = 100000
# N = 4510

def calculate_dp(n, k, level):
    # create dp array large enough for all cases
    dp = np.zeros([k+2, n+2])
    # iterate in reverse from the second to last space
    for i in range(n - 2, -1, -1):
        # iterate in reverse
        for j in range(n, 0, -1):
            if level[i] == 0:
                # if on 0 loose 
                dp[i%k][j] = 2 * INF
            else:
                # else calculate dp based on min number of moves if got to i with run or jump
                dp[i%k][j] = min(dp[(i + 1)%k][j] + 1, dp[(min(i + level[i], n - 1))%k][j - 1] + 1)
        if level[i] == 0:
            # if on 0 loose 
            dp[i%k][0] = 2 * INF
        else:
            # else min moves is min moves from spot ahead plus 1
            dp[i%k][0] = dp[(i + 1)%k][0] + 1
    return dp

def check_level(n, m, k, level, time_limit, stamina):
    # initial output distinc from possible answers -2
    output = [-2] * m
    # dynamic caluclation of array
    dp = calculate_dp(n, k, level)
    # iterate over heroes
    for i in range(m):
        # check if there is enough stamina
        if dp[0][stamina[i]] > INF:
            output[i] = -1
        else:
            # retrieve answer for stamina level
            output[i] = int(max(0, time_limit[i] - dp[0][stamina[i]]))
    return output
  
    
        
# Set SUBMIT_TO_SZKOPUL=True when submitting
# your solution to the Szkopul webserver.
# Set SUBMIT_TO_SZKOPUL=False in order
# to test your code by reading the input from
# a test file ("input0.txt").
SUBMIT_TO_SZKOPUL = True

if SUBMIT_TO_SZKOPUL:
    reader = sys.stdin
else:
    reader = inputReader = open("input0.txt","r")
 
# Reads the input
astr = reader.readline().split()
n = int(astr[0])
m = int(astr[1])
k = int(astr[2])
level = [int(val) for val in reader.readline().split()]
time_limit = [int(val) for val in reader.readline().split()]
stamina = [int(val) for val in reader.readline().split()]

# Calls your function
output = check_level(n, m, k, level, time_limit, stamina)

# Writes the output
for i in range(m):
    print(output[i], end=' ')
print()