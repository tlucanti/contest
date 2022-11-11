
#include <iostream>
#include <string>
#include <vector>

using namespace::std;

int main()
{
    int t;
    cin >> t;
    while (t--) {
        int n;
        string a, b;
        cin >> n >> a >> b;
        for (int i=0; i < n; ++i) {
            a[i] = a[i] - '0';
            b[i] = b[i] - '0';
        }
        bool ok = true;
        vector<int> ans;
        ans.reserve(n + 10);
        int invs = 0;
        if (a != b) {
            for (int i=0; i < n; ++i) {
                if (a[i] != 1 - b[i]) {
                    ok = false;
                    break ;
                }
            }
        } else {
            ans.push_back(1);
            ans.push_back(n);
            for (int i=0; i < n; ++i) {
                a[i] = 1 - a[i];
            }
        }
        if (not ok) {
            cout << "NO\n";
            continue ;
        }
        cout << "YES\n";
        for (int i=0; i < n; ++i) {
            if (a[i] == 1) {
                ans.push_back(i + 1);
                ans.push_back(i + 1);
                ++invs;
            }
        }
        if (invs % 2 == 0) {
            ans.push_back(1);
            ans.push_back(n);
            ans.push_back(1);
            ans.push_back(1);
            ans.push_back(2);
            ans.push_back(n);
        }
        cout << ans.size() / 2 << endl;
        for (int i=0; i < ans.size(); i += 2) {
            cout << ans[i] << ' ' << ans[i + 1] << endl;
        }
    }
}
