class request(object):
	def __init__(self, time, req):
		self.time = time
		self.req = req

	def __hash__(self):
		return hash(self.req)


class pair(object):
	def __init__(self, a, b):
		self.time = a
		self.obj = b
	def __eq__(self, other):
		return hash(self) == hash(other)
	def __hash__(self):
		return self.time
	def __repr__(self):
		return f'({self.time}, {self.obj.req})'


i = 1
str_dict = dict()
time_set = set()
n, m = map(int, input().split())
for cnt in range(n):
	req, t = input().split()
	t = int(t)
	old = str_dict.get(req, None)
	new = request(t, req)
	if old is None:
		str_dict[req] = new
		time_set.add(pair(t, new))
		for rm_pair in time_set:
			break
		rm_req = rm_pair.obj
		# if rm_req.time >= t:
		# 	print('removing added request')
		# 	del str_dict[rm_req.req]
		# 	time_set.remove(t)
		# 	continue
		if len(str_dict) > m:
			del str_dict[rm_req.req]
			time_set.remove(rm_req.time)
			print(i, 'DELETE', rm_req.req)
			print(i, 'PUT', new.req)
			i += 1
		else:
			print(i, "PUT", new.req)
			i += 1
	else:
		for rm_pair in time_set:
			break
		rm_req = rm_pair.obj
		if rm_req.time >= t:
			# print('do not update', req)
			continue
		time_set.remove(old.time)
		time_set.add(pair(t, new))
		print(i, 'UPDATE', req)
		i += 1
