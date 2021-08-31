/**
 *    author:  kostya
 *    created: 2021-08-01 22:33:10
 *    modified 2021-08-02 00:10:36
 **/

#include <utility>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

class Command {
public:
		std::string	name;
		int			cnt;
		int			score;

		Command (std::string  _name, int _cnt, int _score)
				: name(std::move(_name)), cnt(_cnt), score(_score) {}

		[[nodiscard]]bool operator ==(int other) const {
			return (other == score);
		}
};

template <typename _Bidirect_Iter_Tp, typename _Cmp_Tp>
int cmd_count(_Bidirect_Iter_Tp __first, const _Bidirect_Iter_Tp &__last, _Cmp_Tp __cmp) {
	_Cmp_Tp cnt = {};
	while (__first != __last) {
		if (*__first == __cmp)
			++cnt;
		++__first;
	}
	return cnt;
}

int main() {
	int n, k;
	std::cin >> n >> k;
	std::vector<std::string> cmd_names(n);
	std::vector<int> cmd_ans_cnt(n);
	std::vector<int> cmd_scores(n);
	std::vector<int> qu_scores(n, 1);
	std::vector<std::vector<bool>>ans_mat(n);
	char ans;

	for (int i=0; i < n; ++i) {
		std::cin >> cmd_names[i];
		ans_mat[i].resize(k);
		for (int j=0; j < k; ++j) {
			std::cin >> ans;
			cmd_ans_cnt[i] += ans == '+';
			qu_scores[j] += ans == '-';
			ans_mat[i][j] = ans == '+';
		}
	}
	for (int i=0; i < n; ++i) {
		for (int j=0; i < k; ++j) {
			cmd_scores[i] += qu_scores[j] * ans_mat[i][j];
		}
	}

	std::vector<Command> Commands;
	for (int i=0; i < n; ++i) {
		Commands.emplace_back(Command(cmd_names[i], cmd_ans_cnt[i], cmd_scores[i]));
	}

	std::vector<std::vector<Command>> commands_bins;
	for (int i=0; i < n; ++i) {
		commands_bins[cmd_ans_cnt[i]].emplace_back(Commands[i]);
	}

	int place = 1;
	for (const auto &cmd_bin_ : commands_bins) {
		std::sort(cmd_bin_.begin(), cmd_bin_.end(), [](const Command &_Cmd){return _Cmd.name;});
		std::sort(cmd_bin_.begin(), cmd_bin_.end(), [](const Command &_Cmd){return _Cmd.score;});
		int cmd_ = 0;
		while (cmd_ < cmd_bin_.size()) {
			int cnt = cmd_count(cmd_bin_.begin(), cmd_bin_.end(), cmd_bin_[cmd_].score);
			if (cnt == 1) {
				cout << place << ' ' << cmd_bin_[cmd_].name << endl;;
				++cmd_;
			} else {
				for (int place_tmp_ = 0; place_tmp_ < cnt; ++place_tmp_) {
					cout << place << '-' << place + cnt - 1 << ' ' << cmd_bin_[cmd_].name << endl;
				}
			}
			place += cnt;
		}
	}
}
