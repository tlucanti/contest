
#include <iostream>
#include <vector>

using namespace::std;
#define int unsigned long long

int convert(const vector<int> &nn, int aa)
{
    int ans = 0;
    for (int i : nn) {
        ans = ans * aa + i;
    }
    return ans;
}

int count(const vector<int> &nn, const vector<int> &a)
{
    int ans = 0;
    for (int i : nn) {
        ans = ans * 10 + a.at(i);
    }
    return ans;
}

signed main()
{
    int t;
    cin >> t;
    while (t--) {
        int n, b;
        cin >> n >> b;
        vector<int> a;
        a.reserve(10);
        for (int i=0; i < 10; ++i) {
            if (i % b == 0)
                a.push_back(i);
        }
        vector<int> num(18, 0);
        int pos = 0;
        while (true) {
            if (pos >= 18) {
                break ;
            }
            num.at(pos) += 1;
            if (num[pos] == a.size()) {
                num[pos] -= 1;
                pos += 1;
                continue ;
            }
            int cc = count(num, a);
            if (cc == n)
                break ;
            else if (cc > n) {
                num[pos] -= 1;
                pos += 1;
            }
        }
        cout << convert(num, a.size()) << endl;
    }
}
