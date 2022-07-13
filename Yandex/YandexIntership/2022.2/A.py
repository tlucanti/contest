
import json


def inp():
    return list(map(int, input().split()))


n = int(input())
j = []
for i in range(n):
    j += json.loads(input())['offers']

j.sort(key=lambda x: (x['price'], x['offer_id']))
d = {'offers': j}
print(str(d).replace("'", '"'))
