#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
using namespace::std;
#define ing long long int

void factor(int a, set<int> &s, map<int, int> &all, int m)
{
    int i = 1;
    while (i * i <= a) {
        if (i > m) {
            break ;
        }
        if (a % i == 0) {
            s.insert(i);
            all[i] += 1;
            int j = a / i;
            if (j <= m) {
                s.insert(j);
                all[j] += 1;
            }
        }
        ++i;
    }
}


int forward(map<int, set<int>> &n, map<int, int> &all) {
    for (auto it = n.begin(); it != n.end(); ++it) {
        for (int i : it->second) {
            if (all[i] <= 1) {
                return abs(all.rbegin()->first - it->first);
            }
            all[i] -= 1;
        }
    }
    std::abort();
}

int backward(map<int, set<int>> &n, map<int, int> &all) {
    for (auto it = n.rbegin(); it != n.rend(); ++it) {
        for (int i : it->second) {
            if (all[i] <= 1) {
                return abs(all.begin()->first - it->first);
            }
            all[i] -= 1;
        }
    }
    std::abort();
}

signed main()
{
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;

        map<int, set<int>> N;
        map<int, int> all;
        for (int i = 0; i < n; ++i) {
            int a;
            cin >> a;

            set<int> s;
            factor(a, s, all, m);
            N[a] = s;
        }
        if ((int)all.size() < m) {
            cout << "-1\n";
            continue ;
        }

        auto all2(all);
        int ans = forward(N, all);
        int ans2 = backward(N, all2);
        std::cout << min(ans, ans2) << "\n";
    }
}
