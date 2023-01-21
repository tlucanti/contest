
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#define int long long int
using namespace::std;
signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<pair<int, int>> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a.at(i).second;
            a.at(i).first = i;
        }
        sort(a.begin(), a.end(), [](const auto &a1, const auto &a2) { return a1.second < a2.second; });
        set<int> f1;
        for (int i = 1; i <= n; ++i) {
            f1.insert(i);
        }
        set<int> f2(f1);

        vector<int> ans1(n);
        vector<int> ans2(n);
        bool ans = true;

        //cout << "----\n";
        //for (int i =0 ; i<n; ++i) { cout << a.at(i).first << ' '; } cout << '\n';
        //for (int i =0 ; i<n; ++i) { cout << a.at(i).second << ' '; } cout << '\n';
        for (int i = 0; i < n; ++i) {
            int el = a.at(i).second;
            int id = a.at(i).first;

            auto ff = f1.find(el);
            if (ff != f1.end()) {
                ans1.at(id) = el;
                f1.erase(ff);
                if (*(f2.begin()) > el) {
                    ans = false;
                    break ;
                } else {
                    ans2.at(id) = *(f2.begin());
                    f2.erase(f2.begin());
                }
            } else {
                ff = f2.find(el);
                if (ff != f2.end()) {
                    ans2.at(id) = el;
                    f2.erase(ff);
                    if (*(f1.begin()) > el) {
                        ans = false;
                        break ;
                    } else {
                        ans1.at(id) = *(f1.begin());
                        f1.erase(f1.begin());
                    }
                } else {
                    ans = false;
                    break ;
                }
            }
        }

        if (ans) {
            cout << "YES\n";
            for (int i = 0; i < n; ++i) {
                cout << ans1.at(i) << ' ';
            }
            cout << '\n';
            for (int i = 0; i < n; ++i) {
                cout << ans2.at(i) << ' ';
            }
            cout << '\n';
        } else {
            cout << "NO\n";
        }
    }
}
