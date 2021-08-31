
#include <bits/stdc++.h>
using namespace::std;

const char *alp = "abcdefghijklmnopqrstuvwxyz";

int index(string &s) {
	for (int i=0; i < s.size(); ++i) {
		if (s[i] == 'a')
			return (i);
	}
	return (-1);
}

bool solve(string &s) {
	int a = index(s);
	int le = a;
	int ri = a + 1;
	int l = s.size();
	bool FL = true;

	if (a == -1)
		return (false);
	for (int i=0; i < s.size(); ++i) {
		if (le >= 0 and s[le] == alp[i]) {
			--le;
		}
		else if (ri < l and s[ri] == alp[i]) {
			++ri;
		}
		else {
			FL ^= 1;
			break;
		}
	}
	return (FL);
}

int main() {
	int t;
	string s;
	cin >> t;
	while (t--) {
		cin >> s;
		cout << (solve(s) ? "YES" : "NO") << endl;
	}
}