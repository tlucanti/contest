#include <iostream>
#include <string>
using namespace::std;

int main() {
	string s;
	while (1)
	{
		cin >> s;
		if (s.empty())
			break;
		if (s == "Is it rated?")
			cout << "NO" << endl;
		flush();
	}
}
