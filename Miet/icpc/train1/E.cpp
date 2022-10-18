
#include <cmath>
#include <iostream>
using namespace::std;
typedef long long ll;

ll g(ll a, ll b)
{
	return static_cast<ll>(floor(sqrt(a * b)));
}

int main()
{
	const ll r1 = -25;
	const ll r2 = 26;

	int t;
	cin >> t;
	while (t--) {
		ll x, y, z;
		cin >> x >> y >> z;

		ll a = x * y / z;
		ll b = x * z / y;
		ll c = y * z / x;
		for (ll da=max(r1, -a); da < r2; ++da) {
			for (ll db=max(r1, -b); db < r2; ++db) {
				for (ll dc=max(r1, -c); dc < r2; ++dc) {
					ll aa = a + da;
					ll bb = b + db;
					ll cc = c + dc;
					if (x == g(aa, bb) and y == g(aa, cc) and z == g(bb, cc)) {
						cout << aa << ' ' << bb << ' ' << cc << endl;
						goto NEXT;
					}
				}
			}
		}
		cout << "0 0 0\n";
NEXT:
		continue ;
	}
}
