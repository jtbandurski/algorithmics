from random import randint

n = 31
m = 11
start      = [0]*m
target     = [ i for i in range(m)]
level = [0]*n
for i in range(n):
    while ((i + level[i]) < 0 or (i + level[i]) > n-1) or (level[i]==0):
        level[i] = randint(-n//2,n//2)

print(level)

time_limit = [n//2+1]*m

with open('test_input.txt', 'w') as file:
    file.write(f"{n} {m} \n")
    file.write(' '.join(str(val) for val in level) + ' \n')
    file.write(' '.join(str(val) for val in start) + ' \n')
    file.write(' '.join(str(val) for val in target) + ' \n')
    file.write(' '.join(str(val) for val in time_limit) + ' \n')