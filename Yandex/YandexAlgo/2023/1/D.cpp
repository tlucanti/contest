
#include <bits/stdc++.h>

int main()
{
	std::string a, b;
	std::cin >> a >> b;
	std::multiset<char> sa(a.begin(), a.end());
	std::multiset<char> sb(b.begin(), b.end());
	if (sa == sb) {
		std::cout << "YES\n";
	} else {
		std::cout << "NO\n";
	}
}
