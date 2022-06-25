def inp():
    return list(map(int, input().split()))
 
 
for _ in range(int(input())):
    n = int(input())
    s = set(inp())
    ns = len(s)
    print(ns - (n - ns) % 2)
