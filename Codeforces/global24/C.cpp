
#include <bits/stdc++.h>
#define int long long
using namespace::std;

signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        map<int, int> a;
        for (int i=0; i < n; ++i) {
            int _a;
            cin >> _a;
            a[_a] += 1;
        }
        if (a.size() == 1) {
            cout << a.begin()->second / 2 << endl;
            continue ;
        } else if (a.size() == 2) {
            cout << (a.begin()->second * (++a.begin())->second) << endl;
            continue ;
        }
        n = a.size();
        vector<int> sfr(n, 0);
        vector<int> sba(n, 0);

        sfr.at(0) = a.begin()->second;
        int i=1;
        for (auto it = ++a.begin(); it != a.end(); ++it) {
            sfr.at(i) = sfr.at(i - 1) + it->second;
            ++i;
        }

        sba.back() = a.rbegin()->second;
        i = n - 2;
        for (auto it = ++a.rbegin(); it != a.rend(); ++it) {
            sba.at(i) = sba.at(i + 1) + it->second;
            --i;
        }

        int ans = 0;
        for (int i=0; i < n - 1; ++i) {
            int aa = sfr.at(i) * sba.at(i + 1);
            ans = max(ans, aa);
        }
        cout << ans << endl;
    }
}
