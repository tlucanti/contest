
#include <iostream>
#include <map>
#include <vector>

using namespace::std;
typedef unsigned long long ull;
int main()
{
	ull t;
	cin >> t;
	while (t--)
	{
		ull n, q;
		cin >> n >> q;
		vector<ull> a(n);
		vector<ull> s(q);
		for (ull i=0; i < n; ++i)
			cin >> a.at(i);
		for (ull i=0; i < q; ++i)
			cin >> s.at(i);

		map<ull, ull> m;
		ull maxh = 0;
		ull step = 0;
		for (ull i=0; i < n; ++i) {
			maxh += a.at(i);
			step = max(step, a.at(i));
			m[step] = maxh;
		}
		for (ull i=0; i < q; ++i) {
			auto it = m.lower_bound(s.at(i));
			if (it == m.end())
				cout << maxh << ' ';
			else if (it->first > s.at(i)) {
				if (it == m.begin())
					cout << "0 ";
				else
					cout << (--it)->second << ' ';
			}
			else
				cout << it->second << ' ';
		}
		//for (const auto &i : m){
		//	cout << '(' << i.first << ',' << i.second << ')' << ' ';
		//}
		cout << endl;
	}
}
