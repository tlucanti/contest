
l1, r1 = input().split('|')
l2, r2 = input().split('|')
l1 = l1.count('.')
l2 = l2.count('.')
r1 = r1.count('.')
r2 = r2.count('.')
if l1 in (l2, r2) or r1 in (l2, r2):
    print('YES')
else:
    print('NO')

