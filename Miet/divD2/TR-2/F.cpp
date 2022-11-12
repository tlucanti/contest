#include <iostream>
#include <set>
#include <vector>

using namespace::std;
#define int long long

signed main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> tr;
    set<int> m;
    for (int i=0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        tr.push_back({a, b});
        m.insert(a);
    }
    auto p = tr.at(0);
    m.insert(p.first - p.second);
    int ans = 1;
    for (int i=1; i < n; ++i) {
        p = tr.at(i);
        auto start = m.lower_bound(p.first - p.second);
        if (*start == p.first) {
            ans += 1;
        } else {
            auto end = m.upper_bound(p.first);
            if (end == m.end() or *end > p.first + p.second) {
                m.insert(p.first + p.second);
                ans += 1;
            }
        }
    }
    cout << ans << endl;

}

