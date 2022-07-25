
#include <iostream>
#include <vector>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int m, n, k;
		cin >> m >> n >> k;
		vector<int> a(k);
		for (int i=0; i < k; ++i)
			cin >> a.at(i);
		vector<int> a2(a);
		long long sm = 0;
		for (int i : a)
			sm += i;
		if (sm < m * n)
		{
			cout << "NO\n";
			continue;
		}
		bool ok = false;
		int ki = 0;
		int ni = 0;
		bool pos1 = false;
		bool pos2 = false;
		if (n % 2)
		{
			for (int i=0; i < k; ++i)
			{
				int add = a.at(i) / m;
				if (add >= 3)
				{
					ni += 3;
					pos1 = true;
					a.at(i) -= m * 3;
					break ;
				}
			}
		}
		else
		{
			pos1 = true;
		}
		if (pos1)
		{
			while (true)
			{
				if (ki >= k)
					break;
				int add = a.at(ki) / m;
				a.at(ki) -= add * m;
				if (add > 1)
					ni += add;
				else
					++ki;
				if (ni >= n)
				{
					ok = true;
					break ;
				}
			}
		}
		if (ok)
		{
			cout << "YES\n";
			continue ;
		}
		a.swap(a2);
		ki = 0;
		int mi = 0;
		if (m % 2)
		{
			for (int i=0; i < k; ++i)
			{
				int add = a.at(i) / n;
				if (add >= 3)
				{
					mi += 3;
					pos2 = true;
					a.at(i) -= n * 3;
					break ;
				}
			}
		}
		else
			pos2 = true;
		if (pos2)
		{
			while (true)
			{
				if (ki >= k)
					break ;
				int add = a.at(ki) / n;
				a.at(ki) -= add * n;
				if (add > 1)
					mi += add;
				else
					++ki;
				if (mi >= m)
				{
					ok = true;
					break ;
				}
			}
		}
		if (ok)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}

