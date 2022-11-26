
#include <bits/stdc++.h>
#define int long long
using namespace::std;

signed main()
{
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i=0; i < n; ++i) {
            cin >> a.at(i);
        }
        sort(a.begin(), a.end());
        int m = a.front();
        int ans = 0;
        for (int i=1; i < n; ++i) {
            if (m == 1)
                ans += a[i] / m - 1;
            else
                ans += a[i] / (2 * m);
        }
        cout << ans << endl;
    }
}
