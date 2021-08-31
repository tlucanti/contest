
#include <iostream>

using namespace::std;

bool inside(int __x1, int __x2, int a) {
	int x1 = min(__x1, __x2);
	int x2 = max(__x1, __x2);

	if (x1 < a and a < x2) {
		return (true);
	}
	return (false);
}

int solve(int ax, int ay, int bx, int by, int fx, int fy) {
	 if ((ax == bx and bx == fx and inside(ay, by, fy)) or (ay == by and by == fy and inside(ax, bx, fx))) {
	 	return (abs(ax - bx) + abs(ay - by) + 2);
	 }
	 else {
	 	return (abs(ax - bx) + abs(ay - by));
	 }
}

int main() {
	int t;
	char nl;
	int ax, ay, bx, by, fx, fy;

	cin >> t;
	while (t--) {
		cin >> ax >> ay >> bx >> by >> fx >> fy;
		cout << solve(ax, ay, bx, by, fx, fy) << endl;
	}
}
