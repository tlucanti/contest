
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    a, b = input().split()
    mp = {'S':1, 'M':2, 'L':3}
    s1 = [mp[a[-1]], a.count('X')]
    s2 = [mp[b[-1]], b.count('X')]
    if a[-1] == 'S':
        s1[1] = -s1[1]
    if b[-1] == 'S':
        s2[1] = -s2[1]
    if (s1 > s2):
        print('>')
    elif (s1 < s2):
        print('<')
    else:
        print('=')
