
#include <bits/stdc++.h>

typedef long long ll;
int main()
{
	ll n;

	std::cin >> n;
	std::vector<ll> a(n);

	for (ll i = 0; i < n; ++i) {
		std::cin >> a.at(i);
	}

	std::vector<ll> c1(n);
	std::vector<ll> c2(n);

	c1.at(0) = a.at(0);
	for (ll i = 1; i < n; ++i) {
		c1.at(i) = c1.at(i - 1) + a.at(i);
	}

	c2.at(n - 1) = a.at(n - 1);
	for (ll i = n - 2; i >= 0; --i) {
		c2.at(i) = c2.at(i + 1) + a.at(i);
	}

	std::vector<ll> ans(n);
	for (ll i = 0; i < n; ++i) {
		ll left = 0;
		ll right = 0;
		ll x = a.at(i);

		if (i != 0) {
			left = x * i - c1.at(i - 1);
		}
		if (i != n - 1) {
			right = c2.at(i + 1) - x * (n - i - 1);
		}
		ans.at(i) = left + right;
	}

	for (ll i = 0; i < n; ++i) {
		std::cout << ans.at(i) << ' ';
	}
	std::cout << '\n';
}
