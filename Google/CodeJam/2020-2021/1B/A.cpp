#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;
int main() {
	int T;
	cin >> T;
	bool f;
	const long long p = 1000000000;
	const long long pp = 43200000000000;
	for (int i = 0; i < T; ++i) {
		long long a, b, c;
		cin >> a >> b >> c;
		for (int kk = 0; kk < 60 * 60 * 12) {
			if (f)
				break;
			vector<long long> vct = { a,b,c };
			vector<int> vct_perm = { 1,2,3 };
			const long long cs = 1000000000;
			for (int i=0; i < )
			for (int j = 0; j < 6; ++j) {
				auto n1 = vct[vct_perm[0] - 1] % cs;
				auto s1 = vct[vct_perm[0] - 1] / cs % 60;
				auto m1 = vct[vct_perm[0] - 1] / cs / 60 % 60;
				auto h1 = vct[vct_perm[0] - 1] / cs / 60 / 60 % 12;

				auto n2 = vct[vct_perm[1] - 1] / 12 % cs;
				auto s2 = vct[vct_perm[1] - 1] / 12 / cs % 60;
				auto m2 = vct[vct_perm[1] - 1] / 12 / cs / 60 % 60;

				auto n3 = vct[vct_perm[2] - 1] / 720 % cs;
				auto s3 = vct[vct_perm[2] - 1] / 720 / cs % 60;

				if (n1 == n2 && n2 == n3 && s1 == s2 && s1 == s3 && m1 == m2) {
					cout << "Case #" << i + 1 << ": " << h1 << " " << m1 << " " << s1 << " " << n1 << endl;
					f = 1;
					break;
				}
				next_permutation(vct_perm.begin(), vct_perm.end());
			}

			a += p;
			b += p;
			c += p;
			a %= pp;
			b %= pp;
			c %= pp;

		}
	}
}
