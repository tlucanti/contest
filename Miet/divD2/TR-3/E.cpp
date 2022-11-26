
#include <bits/stdc++.h>
#define int long long
using namespace::std;

signed main()
{
    int n, x;
    cin >> n >> x;
    map<int, int> m;
    for (int i=0; i < n; ++i) {
        int a;
        cin >> a;
        m[a] += 1;
    }
    while (true) {
        auto p = m.begin();
        int key = p.first;
        int valuie = p.second;
        if (value == 1) {
            if (m.size() > 1) {
                cout << "No\n";
                break ;
            } else {
                cout << "Yes\n";
                break ;
            }
        }
        if (value % key != 0) {
            cout << "No\n";
            break ;
        }
        m.erase(p);
        m[key + 1]
    }
}
