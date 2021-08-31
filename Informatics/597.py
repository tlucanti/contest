from decimal import Decimal

inp = input().split()
if len(inp) == 1:
    a = Decimal(inp[0])
    b = Decimal(input())
else:
    a, b = Decimal(inp[0]), Decimal(inp[1])
s = Decimal(a)
i = 1

while 1:
    if s >= b:
        break
    a *= 17
    b *= 10
    s *= 10
    i += 1
    s += a

print(i)
