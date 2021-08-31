for i in range(int(input())):
    odd = False  # !% 2
    even = False  # % 2
    n = int(input())
    ar = list(map(int, input().split()))
    for i in range(n):
        if ar[i] % 2 == 0:
            even = True
        else:
            odd = True
    if n % 2 == 0:
        if odd and even:
            print("YES")
        else:
            print("NO")
    else:
        if odd:
            print("YES")
        else:
            print("NO")
