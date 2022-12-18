#include <iostream>
#include <vector>
#define int long long
using namespace::std;
struct interval {
    int start;
    int end;
    bool moved;
};
signed main()
{
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a.at(i);
        }
        vector<interval> v;
        int start = a.at(0);
        int prev = start;
        bool moving = false;
        for (int i = 1; i < n; ++i) {
            if (a.at(i) - prev == 0) {
                moving = true;
                prev = a.at(i);
            } else if (a.at(i) - prev == 1) {
                prev = a.at(i);
            } else if (a.at(i) - prev > 1) {
                interval in;
                in.start = start;
                if (moving) {
                    in.end = prev + 1;
                    in.moved = true;
                } else {
                    in.end = prev;
                    in.moved = false;
                }
                start = a.at(i);
                moving = false;
                prev = start;
                v.push_back(in);
            }
        }
        int back = a.back();
        interval in;
        in.start = start;
        if (moving) {
            in.end = back + 1;
            in.moved = true;
        } else {
            in.end = back;
            in.moved = false;
        }
        v.push_back(in);

        /* done */

        int end;
        bool merging = false;
        vector<interval> vv;
        for (int i = v.size() - 1; i >= 0; --i) {
            if (merging) {
                if (start - v.at(i).end == 1) {
                    start = v.at(i).start;
                } else {
                    interval in = {
                        .start = start,
                        .end = end,
                        .moved = true
                    };
                    vv.push_back(in);
                    merging = false;
                }
            }
            if (not merging) {
                if (v.at(i).moved == false) {
                    vv.push_back(v.at(i));
                    continue ;
                }
                end = v.at(i).end;
                start = v.at(i).start;
                merging = true;
            }
        }
        if (merging) {
            in.end = end;
            in.start = start;
            in.moved = true;
            vv.push_back(in);
        }
        v.swap(vv);

        /* merged */

        end = v.front().end;
        start = v.front().start;
        int ans = end - start + 1;
        for (int i = 1; i < (int)v.size(); ++i) {
            if (start - v.at(i).end == 1) {
                start = v.at(i).start;
                ans = max(ans, end - start + 1);
            } else if (start - v.at(i).end == 2 and v.at(i).moved == false) {
                ans = max(ans, end - v.at(i).start);
                end = v.at(i).end;
                start = v.at(i).start;
                ans = max(ans, end - start + 1);
            } else {
                end = v.at(i).end;
                start = v.at(i).start;
                ans = max(ans, end - start + 1);
            }
        }
        cout << ans << "\n";

        /*
        for (int i = v.size() - 1; i >= 0; --i) {
            in = v.at(i);
            cout << (in.moved ? '[' : '(');
            cout << in.start << ", " << in.end;
            cout << (in.moved ? "] " : ") ");
        }
        cout << '\n';
        */
    }
}
