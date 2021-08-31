
n = int(input())
s = set()

for i in range(n):
    op = input().split()
    if op[0] == "ADD":
        s.add(int(op[1]))
    elif op[0] == "PRESENT":
        print("YES" if int(op[1]) in s else "NO")
    elif op[0] == "COUNT":
        print(len(s))
