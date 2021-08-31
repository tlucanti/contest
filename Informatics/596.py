from decimal import Decimal
import math

a, b = input().split()
a, b = Decimal(a), Decimal(b)
i = 1

while (1):
    if a >= b:
        break
    a *= 17
    b *= 10
    i += 1

print(i)
