
for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    s = s[::-1]
    Alice = 0
    Bob = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] % 2 == 0:
                Alice += s[i]
        else:
            if s[i] % 2 != 0:
                Bob += s[i]
    if Bob == Alice:
        print('Tie')
    elif Bob > Alice:
        print('Bob')
    else:
        print("Alice")
