
k, n = input().split()
k, n = int(k), int(n)
v, p = 0, 0
cards = input().split()
end = 0
for i in range(n):
    c = int(cards[i])
    if c % 3 == 0 and c % 5 == 0:
        continue
    elif c % 3 == 0:
        p += 1
        if p == k:
            print("Petya")
            end = 1
            break
    elif c % 5 == 0:
        v += 1
        if v == k:
            print("Vasya")
            end = 1
            break
if end == 0:
    if p > v:
        print("Petya")
    elif v > p:
        print("Vasya")
    else:
        print("Draw")
