
#include <iostream>
#include <vector>
#include <algorithm>

using namespace::std;

int main()
{
	int n;
	cin >> n;
	vector<pair<int, int> > a(2 * n);
	for (int i=0; i < 2 * n; ++i)
	{
		cin >> a[i].first;
		a[i].second = i;
	}
	sort(a.begin(), a.end(), [](const std::pair<int, int> &p1, const std::pair<int, int> &p2) { return p1.first <= p2.first; });
	int ans = 0;
	int prev = 0;
	for (int i=0; i < a.size(); i += 2)
	{
		ans += abs(a[i].second - prev);
		prev = a[i].second;
	}
	prev = 0;
	for (int i=1; i < a.size(); i += 2)
	{
		ans += abs(a[i].second - prev);
		prev = a[i].second;
	}
	cout << ans << endl;
}

