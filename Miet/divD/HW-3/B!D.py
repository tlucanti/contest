
def is_prime(a):
    i = 2
    if a == 1:
        return 0
    while i * i <= a:
        if a % i == 0:
            return 0
        i += 1
    return 1


maxx = 30000002
s = []
for i in range(2, maxx):
    if i % 10000 == 0:
        print(i)
    if is_prime(i):
        s.append(i)
print(s)
