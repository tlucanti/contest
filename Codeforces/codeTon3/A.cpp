
#include <iostream>
using namespace::std;
int main()
{
    int t;
    cin >> t;
    while (t--) {
        int n, a, _;
        cin >> n >> a;
        while (--n)
            cin >> _;
        if (a == 1)
            cout << "Yes\n";
        else
            cout << "No\n";
    }
}
