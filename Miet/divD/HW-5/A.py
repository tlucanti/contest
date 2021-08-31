
d = {}
for i in range(int(input())):
    a = input()
    n = d.get(a, 0)
    if n:
        print(a + str(n))
        d[a] += 1
    else:
        print('OK')
        d[a] = 1
