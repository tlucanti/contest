
#include <bits/stdc++.h>
using namespace::std;
#define int long long

signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x;
        cin >> n >> x;
        vector<int> a(n, 1);
        a.at(0) = 0;
        a.at(x - 1) = 0;
        vector<int> ans(n, -1);
        ans.front() = x;
        ans.back() = 1;
        for (int i=1; i < n - 1; ++i) {
            bool kk = false;
            for (int j=i + 1; j <= n; j += i + 1) {
                if (a[j - 1] == 1 and j % (i + 1) == 0) {
                    ans.at(i) = j;
                    a.at(j - 1) = 0;
                    kk = true;
                    break ;
                }
            }
        }
        /*if (not ok) {
            cout << "-1\n";
            continue ;
        }*/

        bool ok = true;
        for (int i=0; i < n; ++i) {
            if (ans[i] == -1) {
                ok = false;
                break ;
            }
        }
        if (ok) {
            for (int i=0; i < n; ++i) {
                cout << ans.at(i) << ' ';
            }
        } else {
            cout << "-1";
        }
        cout << endl;
    }
}
