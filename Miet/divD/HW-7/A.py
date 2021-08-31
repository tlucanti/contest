
l1, r1 = map(int, input().split())
l2, r2 = map(int, input().split())
if r1 <= l2 or r2 <= l1:
    print(0)
elif l1 >= l2 and r1 <= r2:
    print(r1 - l1)
elif l2 >= l1 and r2 <= r1:
    print(r2 - l2)
elif l1 <= l2:
    print(r1 - l2)
else:
    print(r2 - l1)
