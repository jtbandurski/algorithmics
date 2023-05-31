import sys

#initiate dictionary
d = dict()
def stairs(n, position, operation):
    output = [0 for _ in range(n)]
    for i in range(n):
        # build
        if operation[i] >= 1:
            # check if no step to the right and invariant satysfied
            if (d.get(str(position[i]+1),0) == 0) and (d.get(str(position[i]-1),0)<d.get(str(position[i]),0)+operation[i]):
                # build step
                d[str(position[i])] = d.get(str(position[i]),0) + operation[i]
                output[i] = d[str(position[i])]
            else:
                # dont build
                output[i] = 0
        
        # delete
        if operation[i] == 0:
            # check if no block to the right
            if (d.get(str(position[i]+1),0) == 0) and (d.get(str(position[i]),0) >= 1):
                # check if any blocks in current position
                # if :
                # remove blocks
                d[str(position[i])] = 0
                output[i] = 1
                # else:
                    # output[i] = 0
            # at least one blokc to the right
            # if d.get(str(position[i]+1),0) >= 1:
                # do nothing
                # output[i] = 0
        
        # operation check if exists
        if operation[i] == -1:
            # check if it is a step and there exists identical value
            if (str(position[i]) in d) and (d.get(str(position[i]),0)>0):
                temp = d.get(str(position[i]),0)
                del d[str(position[i])]
                if temp in d.values():
                    output[i] = 1
                d[str(position[i])] = temp

        # operation find left most step
        if operation[i] == -2:
            # if on the ground then answer is 0
            # if d.get(str(position[i]),0) == 0:
            #     output[i]=0
            # check if starting from a step otherwise leave 0 as answer
            if d.get(str(position[i]),0) > 0:
            # check steps to the left
                k = position[i]
                counter = 0
                # print("k value: ", k)
                while d.get(str(k),0) > 0:
                    # print("step balue: ", d.get(str(k),0))
                    k -=1
                    counter +=1
                    # print("k value: ", k)
                output[i] = counter


        # print("iteration",i," ",output)
        # print("iteration: ", i)
        # print("current position: ", position[i])
        # print("current operation: ", operation[i])
        # print(d)


                
                
    
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
    reader = open("input0b.txt","r")
 
# Reads the input
astr = reader.readline().split()
n = int(astr[0])
positions = [int(val) for val in reader.readline().split()]
operations = [int(val) for val in reader.readline().split()]

# Calls your function
output = stairs(n, positions, operations)

# Writes the output
for i in range(n):
    print(output[i], end=' ')
print()