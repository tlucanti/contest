
#include <bits/stdc++.h>

template <class T>
T gcd(T a, T b)
{
	if (b > a) {
		return gcd(b, a);
	}
	while (true) {
		if (b == 0) {
			return a;
		}
		T c = a % b;
		a = b;
		b = c;
	}
}

int main()
{
	int a, b, c, d;

	std::cin >> a >> b >> c >> d;

	int m = a * d + c * b;
	int n = b * d;
	int g = gcd(n, m);

	std::cout << m / g << ' ' << n / g << '\n';
}

