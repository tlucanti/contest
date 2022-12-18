#include <vector>
#include <iostream>
#define int long long int
#define LD long double
using namespace::std;
struct par {
    int a;
    int b;
};
int _find(int i, int sum)
{
    int l = 0;
    int r = sum;
    while (r - l > 1) {
        int c = (l + r) / 2;
        if (c * 100 / sum >= i)
            r = c;
        else
            l = c;
    }
    return r;
}
par find(int i, int sum)
{
    int start = _find(i, sum);
    int end = _find(i + 1, sum) - 1;
    if (start * 100 / sum != i or end * 100 / sum != i)
        return {-1, -1};
    return {start, end};
}
bool intersect(const par &first, const par &second)
{
    return (first.a <= second.a and second.a <= first.b) or
        (first.a <= second.b and second.b <= first.b);
}
signed main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    int sum = 0;
    vector<int> ans(100, 0);
    ans.at(0) = 1;
    for (int i = 0; i < n; ++i) {
        cin >> a.at(i);
        sum += a.at(i);
    }
    for (int i = 1; i < 100; ++i) {
        par f = find(i, sum);
        int cur = 0;
        if (f.a == -1)
            continue ;
        for (int k = 0; k < n; ++k) {
            par c = find(i, a.at(k));
            if (c.a == -1) {
                cur += a.at(k);
                continue ;
            }
            c.a += cur;
            c.b += cur;
            if (intersect(f, c))
                ans.at(i) = 1;
            cur += a.at(k);
        }
    }
    cout << "0\n";
    for (int i = 1; i < 100; ++i) {
        if (ans.at(i) != 0)
            cout << i << endl;
    }
    cout << "100\n";
}
