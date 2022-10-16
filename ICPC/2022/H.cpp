
#include <iostream>
#include <map>

using namespace::std;
typedef long long ll;
ll MOD = 998244353;

map<pair<ll,ll>, int> s;

void dfs(const pair<ll,ll> &xy) {
	s[xy] = 1;
	const ll X[] = {-1, 1, 0, 0};
	const ll Y[] = {0, 0, -1, 1};
	for (int i=0; i < 4; ++i) {
			auto pp = pair<ll,ll>(xy.first + X[i], xy.second + Y[i]);
			auto it = s.find(pp);
			if (it != s.end() and (*it).second == 0) {
				dfs(pp);
			}
	}
}

int main()
{
	ll n;
	cin >> n;
	for (ll i=0; i < n; ++i) {
		ll a, b;
		cin >> a >> b;
		s[pair<ll,ll>(a, b)] = 0;
	}
	ll gr = 0;
	for (const auto &p : s) {
		if (p.second == 0) {
			dfs(p.first);
			++gr;
		}
	}
	ll ans = 1;
	for (ll i=0; i < gr; ++i) {
		ans = (ans * 2) % MOD;
	}
	//cout << gr << endl;
	cout << ans << endl;
}
