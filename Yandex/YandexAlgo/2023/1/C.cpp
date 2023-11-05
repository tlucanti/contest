
#include <bits/stdc++.h>
#include <stdio.h>

double hypot(double xa, double ya, double xb, double yb)
{
	double dx = xa - xb;
	double dy = ya - yb;
	return std::sqrt(dx * dx + dy * dy);
}

int main()
{
	double xa, ya, xb, yb;

	std::cin >> xa >> ya >> xb >> yb;

	double aa = std::atan2(ya, xa);
	double ab = std::atan2(yb, xb);
	double ang = std::abs(aa - ab);

	double r = hypot(xa, ya, 0, 0);
	double R = hypot(xb, yb, 0, 0);

	if (r > R) {
		std::swap(r, R);
	}

	double ans = std::min(r * ang, r * 2) + R - r;
	printf("%.18f\n", ans);
}

