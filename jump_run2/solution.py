import sys

# transform level to graph in form of list of edges (s,t,c)
def level_to_graph(n, level):
    # init edges
    edges = []
    # add connections
    for i in range(n):
        if level[i] > 0 and i!=n-1:
            edges.append((i,i+1,1))
        if level[i] < 0 and i!=0:
            edges.append((i,i-1,1))
        if level[i]!=1:
            edges.append((i,i+level[i],1))
    
    return edges

# define Floyd-Warshall algorithm from class materials

def FloydWarshall(n, edges):
    # At all times, delta[i][j] will be the upper bound on the cost of the 
    # cheapest path from i to j. 

    # Infinity: Used to signalize that we haven't found any path for 
    # the respective pair yet. Actually, we use a very large number 
    # (one that is surely greater than the cost of any actual cheapest path)
    INF = 1000000000

    # Initially, we do not know anything about any paths...
    delta = [ [INF] * n for v in range(n)]

    # We know that for any edge (s,t,c), a cheapest path from s to t is upper bounded by c. 
    # We use min to deal with the case of multiple edges between the same pair of vertices. 
    for (s,t,c) in edges:
        delta[s][t] = min(delta[s][t], c)

    # We also know that the distance from a vertex to itself is always 0
    for v in range(n):
        delta[v][v] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
            # If delta[i][k] + delta[k][j] (the cost of the best known path from i to j 
            # going through k)
            # is smaller than delta[i][j] (the cost of the best known path from i to j),
            # replace delta[i][j]
                delta[i][j] = min(delta[i][j], delta[i][k] + delta[k][j])

    return delta


def jump_and_run_2(n, m, level, start, target, time_limit):

    # create graph representation
    edges = level_to_graph(n=n, level=level)

    # generate output
    output = [-1]*m

    # run Floyd-Warshal
    delta = FloydWarshall(n=n,edges=edges)

    # iterate over heroes
    for i in range(m):
        output[i] = max(0, time_limit[i] - delta[start[i]][target[i]])

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
m = int(astr[1])
level = [int(val) for val in reader.readline().split()]
start = [int(val) for val in reader.readline().split()]
target = [int(val) for val in reader.readline().split()]
time_limit = [int(val) for val in reader.readline().split()]

# Calls your function
output = jump_and_run_2(n, m, level, start, target, time_limit)

# Writes the output
for i in range(m):
    print(output[i], end=' ')
print()