
#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <string>

using namespace::std;
#define int long long

void rm_old(map<int, set<int>> &val, int old, int num)
{
    auto old_it = val.find(old);
    if (old_it != val.end()) {
        old_it->second.erase(num);
        if (old_it->second.empty()) {
            val.erase(old_it);
        }
    }
}

signed main()
{
    int n, m, q;

    cin >> n >> m >> q;

    vector<set<int>> data(n);
    vector<int> resets(n);
    map<int, set<int>> values;
    vector<int> scores(n, 0);
    for (int i=0; i < n; ++i) {
        values[0].insert(i);
    }

    for (int i=0; i < q; ++i) {
        string cmd;
        cin >> cmd;
        if (cmd == "GETMAX") {
                cout << *(values.rbegin()->second.begin()) + 1 << endl;
        } else if (cmd == "GETMIN") {
                cout << *(values.begin()->second.begin()) + 1 << endl;
        } else if (cmd == "RESET") {
            int num;
            cin >> num;
            --num;
            int old_score = scores.at(num);
            rm_old(values, old_score, num);
            resets.at(num) += 1;
            data.at(num).clear();
            int new_score = resets.at(num) * m;
            values[new_score].insert(num);
            scores.at(num) = new_score;
        } else {
            int num, serv;
            cin >> num >> serv;
            --num;
            --serv;
            int old_score = scores.at(num);
            rm_old(values, old_score, num);
            data.at(num).insert(serv);
            int new_score = resets.at(num) * (m - data.at(num).size());
            values[new_score].insert(num);
            scores.at(num) = new_score;
        }
    }
}
