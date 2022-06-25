
import csv

f1, f2 = input().split()

market_file = open(f1, 'r')
billing_file = open(f2, 'r')
market_csv = csv.reader(market_file, delimiter=',')
billing_csv = csv.reader(billing_file, delimiter=',')

market_data = dict()

print('order_id,shop_name,shop_id,cost')
try:
	market_csv.__next__()
	billing_csv.__next__()
	sm = market_csv.__next__()
except StopIteration:
	exit(0)
for b in billing_csv:
	shop_id = int(b[1])
	while int(sm[0]) < shop_id:
		try:
			sm = market_csv.__next__()
		except StopIteration:
			exit(0)
	if int(sm[0]) > shop_id:
		continue
	shop_name = sm[1]
	print(','.join((b[0], shop_name, str(shop_id), b[-1])))
