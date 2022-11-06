
#include <iostream>
#include <vector>
#include <string>

using namespace::std;
#define int long long

void add(vector<int> &arr, const vector<int> &a) {
    for (int i=0; i < a.size(); ++i) {
        arr.at(arr.size() - i - 1) += a.at(a.size() - i - 1);
    }
}

void sub(vector<int> &arr, const vector<int> &a) {
    for (int i=0; i < a.size(); ++i) {
        arr.at(arr.size() - i - 1) -= a.at(a.size() - i - 1);
    }
}

bool poly(const vector<int> &arr, int sus) {
    int left = 0;
    for (int i=arr.size() - 1; i >= 0; --i) {
        int cur = arr.at(i) + left;
        if (cur % sus != 0)
            return false;
        left = cur / sus;
    }
    return true;
}

signed main()
{
    string s;
    getline(cin, s);

    vector<int> arr((size_t)1e6);
//    vector<int> arr(20);
    vector<int> last;
    bool inv = false;
    char op = '+';
    int min_sus = 2;

    for (char c : s) {
        if (c == ' ') {
            continue ;
        } else if (isalnum(c)) {
            int cc;
            if (isdigit(c))
                cc = c - '0';
            else
                cc = c - 'A' + 10;
            min_sus = max(min_sus, cc + 1);
            last.push_back(cc);
            continue ;
        }

        if (op == '+') {
            if (inv)
                sub(arr, last);
            else
                add(arr, last);
        } else {
            if (inv)
                add(arr, last);
            else
                sub(arr, last);
        }
        last.clear();

        if (c == '+' or c == '-')
            op = c;
        else {
            op = '+';
            inv = true;
        }
    }
    if (op == '+') {
        if (inv)
            sub(arr, last);
        else
            add(arr, last);
    } else {
        if (inv)
            add(arr, last);
        else
            sub(arr, last);
    }


    int size = arr.size();
    for (int i=0; i < arr.size(); ++i) {
        if (arr.at(i) != 0) {
            size = arr.size() - i;
            break ;
        }
    }
    if (size == 0) {
        cout << min_sus << endl;
        return 0;
    }
    arr.erase(arr.begin(), arr.end() - size);

    bool ok = false;
    for (int sus = min_sus; sus <= 1000002; ++sus) {
        if (poly(arr, sus)) {
            ok = true;
            cout << sus << endl;
            break ;
        }
    }
    if (not ok) {
        cout << "-1\n";
    }
}

