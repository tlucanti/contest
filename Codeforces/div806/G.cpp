
#include <iostream>
#include <vector>

using namespace::std;

struct State
{
	long long penalty;
	long long div;

	State() : penalty(0), div(0) {}
	State(long long p, long long d) : penalty(p), div(d) {}
};

vector<long long> array_div(const vector<long long> &a)
{
	vector<long long> ret(a.size());
	for (long long i : a)
		ret[i] = i / 2;
	return ret;
}

vector<long long> array_sub(const vector<long long> &a,
		const vector<long long> &b)
{
	vector<long long> ret(a.size());
	for (long long i : a)
		ret[i] = a[i] - b[i];
	return ret;
}

vector<long long> cumsum(const vector<long long> &a)
{
	int n = a.size();
	vector<long long> ret(n);
	ret[n - 1] = a[n - 1];
	for (int i=n-2; i >= 0; --i)
		ret[i] = a[i] + ret[i + 1];
	return ret;
}

long long powll(long long a, long long n)
{
	long long ret = 1;
	while (n-- > 0)
		ret *= a;
	return ret;
}


int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		long long n, k;
		cin >> n >> k;
		vector<long long> a(n);
		for (int i=0; i < n; ++i)
			cin >> a[i];
		vector<vector<long long>> divs;
		vector<vector<long long>> cms;
		vector<vector<long long>> penalties;
		divs.push_back(a);
		for (int i=0; i < 31; ++i)
		{
			divs.push_back(array_div(divs.back()));
		}
		for (int i=0; i < 31; ++i)
		{
			cms.push_back(cumsum(divs[i]));
		}
		for (int i=0; i < 30; ++i)
		{
			penalties.push_back(array_sub(cms[i], cms[i + 1]));
		}

		vector<State> pay(n);
		vector<State> free(n);
		pay[0] = State(k, 0);
		free[0] = State(penalties[0][0], 1);
		vector<long long> full_buy;
		long long sm = 0;
		for (int i=0; i < n; ++i)
		{
			long long _s = 0;
			for (int j=0; j < 31; ++i)
			{
				if (i + j >= n)
					break ;
				_s += a[i + j] / powll(2, j + 1);
				full_buy.push_back(sm + _s);
				sm += a[i] - k;
			}
		}
		for (int i=1; i < n; ++i)
		{
			State state;
			if (pay[i - 1].penalty < free[i - 1].penalty)
				state = pay[i - 1];
			else
				state = free[i - 1];
			pay[i] = State(state.penalty + k, state.div);
			long long pen_i;
			if (state.div > 30)
				pen_i = 0;
			else
				pen_i = penalties[state.div][i];
			free[i] = State(state.penalty + pen_i, state.div + 1);
		}
		long long fb = 0;
		for (long long i : full_buy)
			fb = std::max(fb, i);
		long long suma = 0;
		for (long long i : a)
			suma += i;
		cout << std::max(suma - std::min(pay.back().penalty, free.back().penalty), fb) << endl;
	}
}
