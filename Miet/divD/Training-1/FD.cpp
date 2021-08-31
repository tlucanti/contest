/**
 *    author:  kostya
 *    created: 2021-07-31 14:12:57
 *    modified 2021-07-31 14:28:43
 **/

#include <bits/stdc++.h>
using namespace::std;
int main() {
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i=0; i < n; ++i) {
			cin >> a[i];
		}
		vector<int> ai(n);
		for (int i=0; i < n; ++i) {
			ai[a[i] - 1] = i;
		}
		int mai, mii;
		mai = ai[0];
		mii = ai[0];
		for (int i=0; i < n; ++i) {
			mai = max(ai[i], mai);
			mii = min(ai[i], mii);
			cout << (int)(mai - mii == i);
		}
		cout << endl;
	}
}
