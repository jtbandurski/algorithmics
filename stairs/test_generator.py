from random import randint
n = 31
position = [-3]*n
operation = [-3]*n
for i in range(10):
    position[i] = randint(0,4)
    operation[i] = randint(1,10)

for i in range(10,n):
    position[i] = randint(0,n-1)
    operation[i] = randint(-2,6)





with open('test_input.txt', 'w') as file:
    file.write(f"{n} \n")
    file.write(' '.join(str(val) for val in position) + ' \n')
    file.write(' '.join(str(val) for val in operation) + ' \n')