
#include <iostream>
#include <string>
#include <vector>

using namespace::std;
#define int long long

signed main()
{
    int t;
    cin >> t;
    while (t--) {
        int _n;
        string s;
        cin >> _n >> s;
        int _0 = 0, _1 = 0;
        int n = 0, ans = 0;
        char cc = s.at(0);
        for (char c : s) {
            if (c == '1')
                ++_1;
            else
                ++_0;
            if (cc == c)
                ++n;
            else {
                ans = max(n * n, ans);
                cc = c;
                n = 1;
            }
        }
        ans = max(n * n, ans);
        ans = max(ans, _1 * _0);
        cout << ans << endl;
    }
}
