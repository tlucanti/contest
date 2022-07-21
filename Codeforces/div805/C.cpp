
#include <iostream>
#include <map>
#include <vector>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, k;
		cin >> n >> k;
		vector<int> a(n);
		for (int i=0; i < n; ++i)
			cin >> a[i];
		map<int, int> first;
		map<int, int> last;
		for (int i=0; i < n; ++i)
		{
			if (not first.contains(a[i]))
				first[a[i]] = i;
			last[a[i]] = i;
		}

		for (int i=0; i < k; ++i)
		{
			int aa, bb;
			cin >> aa >> bb;
			if (not first.contains(aa) or not first.contains(bb))
				cout << "NO" << endl;
			else if (first[aa] < last[bb])
				cout << "YES" << endl;
			else
				cout << "NO" << endl;
		}
	}
}
