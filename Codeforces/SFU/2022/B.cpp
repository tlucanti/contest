
#include <bits/stdc++.h>
#define int long long
using namespace::std;

set<int> sqares;

signed main()
{
    {
        int i = 1;
        while (i * i <= (int)2e9) {
            sqares.insert(i * i);
            ++i;
        }
    }
    int t;
    cin >> t;
    while (t--) {
        int s;
        cin >> s;
        bool ok = false;

        int i = 0;
        while (i * i <= s) {
            ++i;
            if (s % i != 0) {
                continue ;
            }
            int a = i;
            int b = s / i;
            if (sqares.find(a * a + b * b) != sqares.end()) {
                ok = true;
                break ;
            }
        }
        if (ok) {
            cout << "Yes\n";
        } else {
            cout << "No\n";
        }
    }
}
