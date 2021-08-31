/**
 *    author:  kostya
 *    created: 2021-07-31 17:23:17
 *    modified 2021-08-01 23:23:11
 **/

#include <bits/stdc++.h>
using namespace::std;

int main() {
	int w, h, n;
	cin >> w >> h >> n;
	char c;
	int a;
	map<int, int> Wm;
	map<int, int> Hm;
	Wm.emplace(0, w);
	Hm.emplace(0, h);
	set<int> Ws;
	set<int> Hs;
	int size;
	while (n--) {
		cin >> c >> a;
		if (c == 'H') {
			const auto *found = Wm.lower_bound(a);
			size = found.second;
		}
		else {

		}
	}
}

>
