
#include <iostream>
#include <vector>

using namespace::std;

int argmax(const vector<int> &a, int start, int end)
{
	int m = a[start];
	int mi = start;
	for (int i=start; i <= end; ++i)
	{
		if (a[i] > m)
		{
			m = a[i];
			mi = i;
		}
	}
	return mi;
}

int argmin(const vector<int> &a, int start, int end)
{
	int m = a[start];
	int mi = start;
	for (int i=start; i <= end; ++i)
	{
		if (a[i] < m)
		{
			m = a[i];
			mi = i;
		}
	}
	return mi;
}

int req(const vector<int> &a, int start, int end)
{
	int _ma = argmax(a, start, end);
	int _mi = argmin(a, start, end);
	int low, mid, hi;

	int mi = min(_mi, _ma);
	int ma = max(_mi, _ma);

	if (a[start] == a[mi] and a[end] == a[ma])
		return 1;
	if (a[end] == a[mi] and a[start] == a[ma])
		return 1;
	if (mi == start)
		low = 0;
	else
		low = req(a, start, mi);
	mid = req(a, mi, ma);
	if (ma == end)
		hi = 0;
	else
		hi = req(a, ma, end);
	return low + mid + hi;
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i=0; i < n; ++i)
			cin >> a[i];
		if (n == 1)
			cout << 0 << endl;
		else
			cout << req(a, 0, n - 1) << endl;
	}
}
