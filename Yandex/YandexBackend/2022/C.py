
import json
import datetime

j = json.loads(input())
d = dict()

for i in range(5):
    f, q = input().split()
    if f == 'NAME_CONTAINS':
        d['name'] = q
    elif f == 'PRICE_GREATER_THAN':
        d['price>'] = int(q)
    elif f == 'PRICE_LESS_THAN':
        d['price<'] = int(q)
    elif f == 'DATE_AFTER':
        d['after'] = datetime.datetime.strptime(q, "%d.%m.%Y")
    elif f == 'DATE_BEFORE':
        d['before'] = datetime.datetime.strptime(q, "%d.%m.%Y")


ans = []
for t in j:
    date = datetime.datetime.strptime(t['date'], "%d.%m.%Y")
    if (
            d['name'] in t['name'] and
            d['price>'] < t['price'] < d['price<'] and
            d['after'] <= date <= d['before']
    ):
        ans.append(t)

ans.sort(key=lambda x: x['id'])
print(str(ans).replace("'", '"'))
