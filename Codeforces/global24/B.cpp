
#include <bits/stdc++.h>
#define int long long
using namespace::std;

void factor(int n, vector<int> &ans) {
    int i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            ans.push_back(i);
            n /= i;
        } else {
            ++i;
        }
    }
    if (n != 0) {
        ans.push_back(n);
    }
}


int prod(const vector<int> &a) {
    int ans = 1;
    for (const auto i : a) {
        ans *= i;
    }
    return ans;
}

signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        int mx = 0;
        for (int i=0;i < n; ++i) {
            cin >> a.at(i);
            mx = max(mx, a.at(i));
        }
        vector<int> divs;
        factor(a.at(0), divs);
        for (int i=0; i < n; ++i) {
            if (divs.empty()) {
                break ;
            }
            vector<int> dd;
            int aa = a.at(i);
            for (const auto d : divs) {
                if (aa % d == 0) {
                    dd.push_back(d);
                    aa /= d;
                }
            }
            divs = dd;
        }
        if (divs.empty()) {
            cout << mx << endl;
        } else {
            int p = prod(divs);
            cout << mx / p << endl;
        }
    }
}
