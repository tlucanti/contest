
from functools import reduce


def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    a = inp()
    b = reduce(lambda a, b: a ^ b, a)
    for i in a:
        if b ^ i == i:
            print(i)
            break
