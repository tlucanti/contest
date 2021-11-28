/*
* @Author: kostya
* @Date:   2021-11-21 17:47:13
* @Last Modified by:   kostya
* @Last Modified time: 2021-11-21 18:12:47
*/

#include <vector>
#include <list>
#include <iostream>

using namespace::std;

int ranks[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000,
	1000000000};

int get_digit(int n, int i)
{
	return (n % ranks[i + 1]) / ranks[i];
}

void lsd_radix_sort(vector<int> &arr, int max=6)
{
	for (int i=0; i < max; ++i)
	{
		list<int> bins[10];
		for (int a : arr)
			bins[get_digit(a, i)].push_back(a);
		int it = 0;
		for (int j=0; j < 10; ++j)
		{
			for (int a : bins[j])
				arr[it++] = a;
		}
	}
}

int main()
{
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i=0; i < n;++i)
		cin >> a[i];
	lsd_radix_sort(a);
	cout << endl;
	int problems = 1;
	int ans = 0;
	for (int i=0; i < n; ++i)
	{
		if (a[i] >= problems)
		{
			++ans;
			++problems;
		}
	}
	cout << ans << endl;
}
