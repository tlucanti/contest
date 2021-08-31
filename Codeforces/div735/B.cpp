#include <iostream>
#include <vector>
#include <algorithm>
using namespace::std;

#define f(i, j) (a[i].second+1)*(a[j].second+1) - k * (a[i].first | a[j].first)


int comp(pair<long long, int> &v1, pair<long long, int> &v2) {
	if (v1.first == v2.first) {
		return v2.second > v1.second;
	}
	else {
		return v2.first < v1.first;
	}
}

int main() {
	long long t;

	cin >> t;
	while (t--) {
			long long n, k;
			long long m;
			long long mi = 0;
			bool flag = 0;
			cin >> n >> k;
			vector<pair<long long, int>> a;
			a.resize(n);
			for (long long i=0; i < n; ++i) {
				cin >> a[i].first;
				a[i].second = i;
			}
			sort(a.begin(), a.end(), comp);
			for (int i=0; i < n-1; ++i) {
				mi = f(i, i+1);
				if (!flag) {
					m = mi;
					flag = 1;
				}
				else
					m = max(mi, m);
			}
			cout << m << endl;
	}
}