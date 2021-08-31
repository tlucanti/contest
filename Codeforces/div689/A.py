
st = 'abc' * 333 + 'a'
for t in range(int(input())):
    n, k = map(int, input().split())
    print(st[:n])
