
#include <iostream>
#include <vector>
using namespace::std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> a(k);
        for (int i=0; i < k; ++i)
            cin >> a.at(i);
        bool LAST = false;
        int last = 0;
        const char *ans = "YES";
        for (int i=k - 2; k >= 0; --k)
        {
            int e = a.at(i + 1) - a.at(i);
            if (LAST and e > last)
            {
                ans = "NO";
                break ;
            }
            last = e;
            LAST = true;
        }

        if (k > 1 and (n - k + 1) * last < a.at(0))
            ans = "NO";
        cout<<ans<<"\n";
    }
}
