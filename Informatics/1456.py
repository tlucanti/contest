
n = input()
s = list(map(int, input().split()))
p = int(input())
s.append(p)
print(len(s) - sorted(s).index(p))
