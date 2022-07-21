
for _ in range(int(input())):
    n = input()
    k = len(n) - 1
    n = int(n)
    if n == 1:
        print(0)
    else:
        print(n - 10**k)
