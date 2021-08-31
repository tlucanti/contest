##
#    author:  kostya
#    created: 2021-08-01 16:59:38
#    modified 2021-08-01 23:19:12
##

class Command(object):
	"""
	"""
	def __init__(self, _name, _cnt, _sc):
		self.name = _name
		self.cnt = _cnt
		self.score = _sc

	def __eq__(self, other):
		return self.score == other

	def __repr__(self):
		return '{' + self.name + ', ' + str(self.cnt) + ', ' + str(self.score) + '}'


n, k = map(int, input().split())
cmd_names = []
cmd_ans_cnt = [0] * n
cmd_scores = [0] * n
qu_scores = [1] * k
ans_mat = [[0] * k for i in range(n)]

for i in range(n):
	cmd_name_, *ans_ar_ = input().split()
	cmd_names.append(cmd_name_)
	for j in range(k):
		cmd_ans_cnt[i] += ans_ar_[j] == '+'
		qu_scores[j] += ans_ar_[j] == '-'
		ans_mat[i][j] = ans_ar_[j] == '+'
for i in range(n):
	for j in range(k):
		cmd_scores[i] += qu_scores[j] * ans_mat[i][j]

Commands = []
for i in range(n):
	Commands.append(Command(cmd_names[i], cmd_ans_cnt[i], cmd_scores[i]))

commands_bins = [[] for _i in range(k + 1)]
for i in range(n):
	commands_bins[cmd_ans_cnt[i]].append(Commands[i])
place = 1
for cmd_bin_ in commands_bins[::-1]:
	cmd_bin_.sort(key=lambda _Cmd: _Cmd.name)
	cmd_bin_.sort(key=lambda _Cmd: _Cmd.score, reverse=True)
	cmd_ = 0
	while cmd_ < len(cmd_bin_):
		cnt = cmd_bin_.count(cmd_bin_[cmd_].score)
		if cnt == 1:
			place_str = str(place)
			print(place_str, cmd_bin_[cmd_].name)
			cmd_ += 1
		else:
			for place_tmp in range(cnt):
				place_str = str(place) + '-' + str(place + cnt - 1)
				print(place_str, cmd_bin_[cmd_].name)
				cmd_ += 1
		place += cnt

