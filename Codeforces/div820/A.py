
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    a, b, c = inp()
    a -= 1
    b -= 1
    c -= 1
    s = abs(b - c) + c
    if a == s:
        print(3)
    elif a < s:
        print(1)
    else:
        print(2)
  
