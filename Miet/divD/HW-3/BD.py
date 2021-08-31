maxx = 30000000
reseto = [1 for i in range(maxx + 2)]
reseto[0] = 0
reseto[1] = 0
i = 2

while i * i <= maxx:
    while reseto[i] == 0:
        i += 1

    for j in range(i + i, maxx + 1, i):
        reseto[j] = 0
    i += 1

pr_sum = 0
for i in range(maxx):
    if reseto[i]:
        pr_sum += i
    reseto[i] = pr_sum

# __input__ = open('input.txt', 'r')
# __output__ = open('outputpy.txt', 'w')
# input = __input__.readline
# print = lambda *args, sep=' ', end='\n': __output__.write(sep.join(map(str, args)) + end)

for q in range(int(input())):
    l, r = input().split()
    l, r = int(l), int(r)
    print(reseto[r] - reseto[l - 1])
