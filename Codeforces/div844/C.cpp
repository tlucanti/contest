
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>

using namespace::std;
#define int long long int

signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        n = s.size();

        map<char, int> mp;
        vector<pair<char, int>> d;
        for (char c : s) {
            mp[c] += 1;
        }
        for (const auto &i : mp) {
            d.push_back(i);
        }
        sort(d.begin(), d.end(), [](const pair<char, int> &a, const pair<char, int> &b) {
            return a.second < b.second;
        });
        int ans = n;
        int aw, ah;
        for (int w = 1; w <= 26; ++w) {
            if (n % w != 0) {
                continue ;
            }
            int h = n / w;
            int cur1 = 0;
            //int cur2 = 0;
            int i = 0;
            for (auto it = d.rbegin(); it != d.rend(); ++it) {
                cout << it->first << ':' << it->second << ' ';
                if (i < w) {
                    cur1 += abs(h - it->second);
                } else {
                    cur1 += it->second;
                }
                ++i;
            }
            while (i < w) {
                cur1 += h;
                ++i;
            }
            /*
            i = 0;
            for (auto it = d.begin(); it != d.end(); ++it) {
                if (i < w) {
                    cur2 += abs(h - it->second);
                } else {
                    cur2 += it->second;
                }
                ++i;
            }
            while (i < w) {
                cur2 += h;
                ++i;
            }
            */
            int cur = cur1; // min(cur1, cur2);
            cout << '\n' << w << 'x' << h << " - " << cur << "\n";
            if (cur < ans) {
                ans = cur;
                aw = w;
                ah = h;
            }
        }
        cout << ans / 2 << "\n";
        map<char, int> m;
        int i = 0;
        int w = aw;
        int h = ah;
            for (auto it = d.rbegin(); it != d.rend(); ++it) {
                if (i < w) {
                    m[it->first] = h;
                }
                ++i;
            }
        for (char c = 'a'; c <= 'z'; ++c) {
            if (i >= w) {
                break ;
            }
            if (m.find(c) == m.end()) {
                m[c] = h;
                ++i;
            }
        }

        // ================================
        for (auto ii : m) {
            cout << ii.first << ':' << ii.second << ' ';
        }
        cout << '\n';
        // ==============================

        for (char &c : s) {
            if (m[c] > 0) {
                m[c] -= 1;
            } else {
                c = '0';
            }
        }


        for (char &c : s) {
            if (c == '0') {
                while (m.begin()->second == 0) {
                    m.erase(m.begin());
                }
                c = m.begin()->first;
                m.begin()->second -= 1;
            }
        }

        cout << s << '\n';
    }

}
