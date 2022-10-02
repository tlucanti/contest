
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace::std;
int check_loop(int f, const vector<int> &d)
{
    int q = 1;
    int ff = f;
    f = d.at(f);
    while (true)
    {
        if (f == ff)
            return q;
        if (f == -1)
            return 26;
        f = d.at(f);
        q += 1;
    }
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        vector<int> d(26, -1);
        for (char i : s)
        {
            int o = i - 'a';
            if (d.at(o) == -1)
            {
                int nx = 0;
                while (true)
                {
                    if (find(d.begin(), d.end(), nx) != d.end())
                    {
                        nx = (nx + 1) % 26;
                        continue ;
                    }
                    d.at(o) = nx;
                    if (o == nx or check_loop(nx, d) < 26)
                    {
                        nx = (nx + 1) % 26;
                        continue ;
                    }
                    break ;
                }
            }
        }

        for (char i : s)
        {
            int o = i - 'a';
            int c = d.at(o);
            cout << (char)(c + 'a');
        }
        cout << endl;
    }
}
