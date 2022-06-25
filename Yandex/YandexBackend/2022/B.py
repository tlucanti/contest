import collections

n = int(input())
vak = dict()

for i in range(n):
    v, k = input().split(',')
    vak[v] = int(k)

k = int(input())
data = collections.defaultdict(list)
approved = [''] * k
appr_i = 0

for i in range(k):
    name, v, task, penalty = input().split(',')
    task = int(task)
    penalty = int(penalty)
    data[v].append((name, v, task, penalty))

for v in data:
    lst = data[v]
    lst.sort(key=lambda x: (x[2], -x[3]), reverse=True)
    # lst.sort(key=lambda x: x.task, reverse=True)
    for i in range(min(vak[v], len(lst))):
        approved[appr_i] = lst[i][0]
        appr_i += 1

approved.sort()
for i in approved:
    if i == '':
        continue
    print(i)
