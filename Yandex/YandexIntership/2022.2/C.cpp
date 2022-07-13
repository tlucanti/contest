
#include <iostream>
#include <cmath>

long long sq(long long n)
{
	return n * n;
}

long long closest_square_slow(long long n, long long hint)
{
	long long i = hint;
	while (n < sq(2*i - 1) and n >= sq(2*i + 1))
		++i;
	return i;
}

long long closest_square_fast(long long n)
{
	double i = std::floor(std::sqrt(static_cast<double>(n)));
	return closest_square_slow(n, std::max(static_cast<long long>(i) / 2 - 2, 0LL));
}

std::pair<long long, long long> solve(long long n)
{
	if (n == 0)
		return {0, 0};
	long long i = closest_square_fast(n);
	long long pos = n - sq(2*i - 1);
	long long sq = 2*i * 4;
	std::pair<long long, long long> c = {-i, i - 1};
	if (pos >= 0 and pos < sq / 4)
		c.second -= pos;
	else if (pos >= sq / 4 and pos < sq / 2)
	{
		c.second -= sq / 4 - 1;
		c.first += pos - (sq / 4 - 1);
	}
	else if (pos >= sq / 2 and pos < sq * 3 / 4)
	{
		c.second -= sq / 4 - 1;
		c.first += sq / 4;
		c.second += pos - (sq / 2 - 1);
	}
	else
	{
		++c.second;
		c.first += sq - pos - 1;
	}
	return c;
}

int main()
{
	for (int i=0; i < 100; ++i)
	{
		auto c = solve(i);
		std::cout << i << " [" << c.first << ", " << c.second << "]\n";
	}
}

