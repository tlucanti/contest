
#include <bits/stdc++.h>
using namespace::std;
#define int long long
signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n, q;
        cin >> n >> q;

        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a.at(i);
        }
        vector<int> pref(n);
        vector<int> suff(n);

        pref.at(0) = a.at(0);
        for (int i = 1; i < n; ++i) {
            pref.at(i) = pref.at(i - 1) + a.at(i);
        }

        suff.at(n - 1) = a.at(n - 1);
        for (int i = n - 2; i >= 0; --i) {
            suff.at(i) = suff.at(i + 1) + a.at(i);
        }

        for (int i = 0; i < q; ++i) {
            int l, r, k;
            cin >> l >> r >> k;
            --l;
            --r;
            int L, R;
            if (l == 0) {
                L = 0;
            } else {
                L = pref.at(l - 1);
            }
            if (r == n - 1) {
                R = 0;
            } else {
                R = suff.at(r + 1);
            }
            int ans = L + R + k * (r - l + 1);
            if (ans % 2 == 0) {
                cout << "NO\n";
            } else {
                cout << "YES\n";
            }
        }
    }
}
