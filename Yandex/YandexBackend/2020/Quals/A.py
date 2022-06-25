
import json

def absnull(n):
	if n < 0:
		return 0
	return n

jin = json.load(open('input.txt', 'r'))
jin.sort(key=lambda x: x['event_id'])
d = dict()
# {
# 	(int) ord -> {
# 	    (int) item_id -> [(int) count, (bool) status]
# 	}
# }
for ev in jin:
	id = ev['order_id']
	ord = d.get(id, None)
	if ord == None:
		ord = dict()
	ord[ev['item_id']] = [absnull(ev['count'] - ev['return_count']), ev['status'] == 'OK']
	d[id] = ord

# print(d)
jout = []
for ord in d:
	new_items = list()
	new_ord = {"id": ord, "items": new_items}
	jout.append(new_ord)
	for item in d[ord]:
		if not d[ord][item][1]:
			continue
		if d[ord][item][0] > 0:
			new_items.append({"id": item, "count": d[ord][item][0]})
	if len(new_ord["items"]) == 0:
		jout.pop()

with open('output.txt', 'w') as out:
	out.write(json.dumps(jout))