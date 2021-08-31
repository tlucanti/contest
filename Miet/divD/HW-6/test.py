
from random import randint as r
num = r(1000, 2000)
with open('input.txt', 'w') as f:
    f.write("{}\n".format(num))
    for t in range(num):
        n, m = r(1, 10000), r(1, 10000)
        f.write("{} {}\n".format(n, m))
        for _ in range(m):
            f.write("{} {}\n".format(r(1, n), r(1, n)))
