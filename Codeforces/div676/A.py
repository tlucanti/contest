for t__ in range(int(input())):
    a, b = input().split()
    a, b = int(a), int(b)
    print(min(a, b) ^ max(a, b))
