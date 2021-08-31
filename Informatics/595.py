from decimal import Decimal

x, y, z = input().split()
x, y, z = Decimal(x), Decimal(y), Decimal(z)
for i in range(int(input())):
    a, b, c, q = input().split()
    a, b, c, q = Decimal(a), Decimal(b), Decimal(c), Decimal(q)
    x, y, z = x - a*q, y - b*q, z - c*q

if x <= 0 and y <= 0 and z <= 0:
    print("YES")
else:
    print("NO")
