
import datetime

input = open('input.txt', 'r').readline
t, e = map(int, input().split())
data = []
while True:
	s = input()
	if s == "":
		break
	d = datetime.datetime(
		year=int(s[1:5]),
		month=int(s[6:8]),
		day=int(s[9:11]),
		hour=int(s[12:14]),
		minute=int(s[15:17]),
		second=int(s[18:20])
	)
	status, *message = s[22:].split()
	del message
	if status == 'ERROR':
		data.append(d)

n = len(data)
if n < e:
	print(-1)
	exit(0)
for i in range(e - 1, n):
	if int((data[i] - data[i - e + 1]).total_seconds()) < t:
		print(data[i])
		exit(0)
print(-1)
