
def inp():
    return list(map(int, input().split()))


for _t in range(int(input())):
    n, z = inp()
    a = inp()
    print(max([z | x for x in a]))