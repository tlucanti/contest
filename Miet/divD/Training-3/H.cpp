/**
 *    author:  kostya
 *    created: 2021-07-31 16:49:28
 *    modified 2021-07-31 16:54:48
 **/

#include <bits/stdc++.h>
using namespace::std;
#define ll long long

int main() {
	ll k;
	cin >> k;
	if (k < 3)
		cout << -1 << endl;
	else if (k % 2)
		cout << (k*k / 2) << ' ' << (k*k / 2 + 1) << endl;
	else if (k % 4)
		cout << (k*k / 8 * 2) << ' ' << ((k*k / 8 + 1) * 2) << endl;
	else
		cout << (k / 4 * 3) << ' ' << (k / 4 * 5) << endl; 
}
