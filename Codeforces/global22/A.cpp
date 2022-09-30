
#include <iostream>
#include <vector>
#include <algorithm>

using namespace::std;
typedef unsigned long long ull;

ull solve(const vector<ull> &A, const vector<ull> &B)
{
	int aa = 0;
	int bb = 0;

	ull ans = 0;
	if (A.size() > 0)
	{
		ans = A.back();
		aa = 1;
	}
	for (ull i=0; i < max(A.size(), B.size()) + 1; ++i)
	{
		if (i < B.size())
		{
			if (aa)
				ans += B.at(i) * 2;
			else
				ans += B.at(i);
			bb = 1;
		} else
			bb = 0;


		if (A.size() > 0 and i < A.size() - 1)
		{
			if (bb)
				ans += A.at(i) * 2;
			else
				ans += A.at(i);
			aa = 1;
		} else
			aa = 0;
	}
	return ans;
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		ull n;
		cin >> n;
		vector<ull> a(n);
		vector<ull> b(n);

		for (ull i=0; i < n; ++i)
			cin >> a.at(i);
		for (ull i=0; i < n; ++i)
			cin >> b.at(i);

		vector<ull> A;
		vector<ull> B;
		A.reserve(n);
		B.reserve(n);

		for (ull i=0; i < n; ++i)
		{
			if (a.at(i) == 0)
				A.push_back(b.at(i));
		}
		for (ull i=0; i < n; ++i)
		{
			if (a.at(i) == 1)
				B.push_back(b.at(i));
		}


		std::sort(A.begin(), A.end(), [](ull aa, ull bb){ return aa > bb; });
		std::sort(B.begin(), B.end(), [](ull aa, ull bb){ return aa > bb; });
		cout << max(solve(A, B), solve(B, A)) << endl;
	}
}

