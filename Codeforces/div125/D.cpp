/*
* @Author: tlucanti
* @Date:   2022-03-22 19:31:15
* @Last Modified by:   tlucanti
* @Last Modified time: 2022-03-22 19:43:21
*/

#include <iostream>
#include <vector>

using namespace::std;

typedef unsigned long long ull;

struct war
{
	ull c;
	ull d;
	ull h;
};


int main()
{
	ull n, C;
	cin >> n >> C;
	vector<struct war> W(n);
	ull c, d, h;
	for (int i=0; i < n; ++i)
	{
		cin >> c >> d >> h;
		W[i] = {c, d, h};
	}
	ull m;
	cin >> m;
	for (int i=0; i < m; ++i)
	{
		cin >> d >> h;
		ull c = W[0].c * h;
		for (const auto &w : W)
		{
			ull ni = h * d / (w.d * w.h);
			if (ni * w.d * w.h <= h * d)
				++ni;
			ull ci = w.c * ni;
			if (ci < c)
				c = ci;
		}
		if (c <= C)
			cout << c << endl;
		else
			cout << "-1\n";
	}
}
