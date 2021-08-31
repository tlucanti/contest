/**
 *    author:  kostya
 *    created: 2021-07-31 14:46:33
 *    modified 2021-07-31 14:59:01
 **/

#include <bits/stdc++.h>
using namespace::std;
#define ll long long
#define _tn typename
template <_tn type_t>
void print(type_t v, const string &end="\n", const string &sep=" ") {
	for (const auto &i : v) {
		cout << i << sep;
	}
	cout << end;
}

int d_sum(ll n) {
	int ans = 0;
	for (auto i:to_string(n)) {
		ans += (int)(i - 48);
	}
	return ans;
}

int main() {
	ll a, b, c, x;
	cin >> a >> b >> c;
	vector<ll> ans(0);
	for (int i=0; i < 83; ++i) {
		x = b * pow(i, a) + c;
		if (x <= 0 or x >= (int)1e9) {
			continue;
		}
		if (d_sum(x) == i) {
			ans.push_back(x);
		}
	}
	cout << ans.size() << endl;
	print(ans);
}
