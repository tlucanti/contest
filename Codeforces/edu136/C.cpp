#include <bits/stdc++.h>
using namespace::std;
typedef unsigned long long ull;

vector<vector<ull>>binom;
inline constexpr MOD = 998244353ull;

pair<ull, ull> solve(ull n)
{
	if (n > 2)
	{
		auto prev = solve(n - 2);
		ull w = comb.at(n - 1).at(n / 2) + prev.second;
		ull l = comb.at(n, n / 2) - w - 1;
		return {w, l};
	}
	return {1, 0};
}

int main()
{
	for (int n=0; n <= 60; ++n)
	{
		binom.at(n).at(0) = 1;
		for (int k=1; k < n; ++k)
			binom.at(n).at(k) =
				(binom.at(n - 1) + binom.at(k - 1).at(k)) % MOD;
		binom.at(n).at(n) = 1;
	}

	int t;
	cin >> t;
	while (t--)
	{
		int n;
		auto s = solve(n);
		cout << solve.first % MOD << ' ' << solve.second % MOD << endl;
	}
}
