n = 13
m = 5
level =[12, 1, 1, 6, 1, 1, 1, -4, 1, -3, -1, -3, -9]
start      = [ 0, 0, 0,  6, 11]
target     = [ 0, 6, 6,  0,  9]
time_limit = [10, 1, 7, 26,  3]

edges = []

for i in range(n):
    if level[i] > 0 and i!=n-1:
        edges.append((i,i+1,1))
    if level[i] < 0 and i!=0:
        edges.append((i,i-1,1))
    if level[i]!=1:
        edges.append((i,i+level[i],1))

for e in edges:
    print("source, target, cost: ", e)
print(len(edges))

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

# At then end, for every (s,t), 
# delta[s][t] will be the cost of the cheapest path from s to t, 
# or INF if no s-t-path exists at all.

for row in delta:
    print(row)

for i in range(m):
    print(max(0, time_limit[i] - delta[start[i]][target[i]]))
