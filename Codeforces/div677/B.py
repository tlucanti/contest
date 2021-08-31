
for t__ in range(int(input())):
    n = int(input())
    s = input()
    print(s[s.index('1'):s.rindex('1')].count('0'))
