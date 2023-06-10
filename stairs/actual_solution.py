import sys

#initiate dictionary
d = dict()
def stairs(n, position, operation):
    output = [0 for _ in range(n)]
    for i in range(n):
        # build
        if operation[i] >= 1:
            # check if no step to the right and invariant satysfied
            if (d.get(str(position[i]+1),[0,0])[0] == 0) and (d.get(str(position[i]-1),[0,0])[0]<d.get(str(position[i]),[0,0])[0]+operation[i]):
                # build step
                # if previous step zero then length to go left 1 otherwise previous plus 1
                if d.get(str(position[i]-1),[0,0])[0] == 0:
                    d[str(position[i])] = [d.get(str(position[i]),[0,0])[0] + operation[i],1]
                else:
                    d[str(position[i])] = [d.get(str(position[i]),[0,0])[0] + operation[i], d.get(str(position[i]-1),[0,0])[1]+1]

                output[i] = d[str(position[i])][0]
            else:
                # dont build
                output[i] = 0
        
        # delete
        if operation[i] == 0:
            # check if no block to the right
            if (d.get(str(position[i]+1),[0,0])[0] == 0) and (d.get(str(position[i]),[0,0])[0] >= 1):
                
                # remove blocks and update length to go left
                d[str(position[i])] = [0, 0]
                output[i] = 1
        
        # operation check if exists
        if operation[i] == -1:
            # check if it is a step and there exists identical value
            if (str(position[i]) in d) and (d.get(str(position[i]),[0,0])[0]>0):
                temp = d.get(str(position[i]),[0,0])
                del d[str(position[i])]
                if temp[0] in [x[0] for x in d.values()]:
                    output[i] = 1
                d[str(position[i])] = temp

        # operation find left most step 
        # which means read the second value of the stored list rperesenting step
        if operation[i] == -2:
            output[i] = d.get(str(position[i]),[0,0])[1]

                
                
    
    return output
  
    
        
# Set SUBMIT_TO_SZKOPUL=True when submitting
# your solution to the Szkopul webserver.
# Set SUBMIT_TO_SZKOPUL=False in order
# to test your code by reading the input from
# a test file ("input0.txt").
SUBMIT_TO_SZKOPUL = False

if SUBMIT_TO_SZKOPUL:
    reader = sys.stdin
else:
    reader = open("test_input.txt","r")
 
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