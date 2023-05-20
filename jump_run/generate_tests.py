import random

n=32
m=12
k=5
random.seed(12345)
level = [1]
level.extend([random.randint(0, k) for _ in range(n-7)])
level.extend([1]*6)
random.seed(12345)
time_limit = [random.randint(n/2, 2*n) for _ in range(m)]
stamina = [random.sample(range(0, n), 1)[0] for _ in range(m)]
print(level, len(level))
print(time_limit)
print(stamina)
with open('./jump_run/input.txt', 'w') as file:
    file.write(f"{n} {m} {k} \n")
    file.write(' '.join(str(val) for val in level) + ' \n')
    file.write(' '.join(str(val) for val in time_limit) + ' \n')
    file.write(' '.join(str(val) for val in stamina) + ' \n')

