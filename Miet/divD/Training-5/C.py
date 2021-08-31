def digit_num(nn):
    if nn == 0:
        return 1
    ans = 0
    while nn:
        ans += 1
        nn //= 10
    return ans


def count(tab, dic, it):
    ans = 1
    needle = dic[tab[it]]
    for i in range(it + 1, len(tab)):
        if dic[tab[i]] == needle:
            ans += 1
        else:
            break
    return ans


n = int(input())
d_names = {}
d_scores = {}
for i in range(n):
    s, sc = input().split()
    d_scores[s.lower()] = int(sc)
    d_names[s.lower()] = s
table = sorted(d_scores.keys())
table = sorted(table, key=lambda x: 10000001 - d_scores[x])
# print(table)
max_score = max(digit_num(max(d_scores.values())), 5)
max_name = 4
for i in table:
    max_name = max(max_name, len(i))
max_place = 5
i = 0
while i < len(table):
    an = count(table, d_scores, i)
    if an == 1:
        table[i] = (d_names[table[i]], str(i + 1), str(d_scores[table[i]]))
    else:
        for j in range(i, i + an):
            table[j] = (d_names[table[j]], str(i + 1) + '-' + str(i + an), str(d_scores[table[j]]))
    max_place = max(max_place, len(table[i][1]))
    i += an

print('|', '.' * (max_place - 5), 'Place|Name', '.' * (max_name - 4), '|Score', '.' * (max_score - 5), '|', sep='')
for i in table:
    print('|', '.' * (max_place - len(i[1])), i[1],
          '|', i[0], '.' * (max_name - len(i[0])),
          '|', i[2], '.' * (max_score - len(i[2])),
          '|', sep='')
