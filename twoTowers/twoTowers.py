import sys


def secret_tunnel_length(n, heights):
    first = max(heights)
    id_first = heights.index(first)
    heights[id_first] = 0
    second = max(heights)
    id_second = heights.index(second)
    ret = abs(id_second - id_first) + 1

    # WRITE YOUR CODE HERE 
    # (and also feel free to write outside this function, 
    # for example, if you want to write new functions).
    
            
    return ret
 

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
astr = reader.readline()
n=int(astr)
heights = [int(val) for val in reader.readline().split()]

# Calls your function
ret = secret_tunnel_length(n, heights)

# Writes the output
print(ret)