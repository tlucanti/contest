
#include <iostream>
#include <string>

using namespace::std;

void str_upper(string &str)
{
	for (int i=0; i < str.size(); ++i)
	{
		str[i] = std::toupper(str[i]);
	}
}

int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		string str;
		cin >> str;
		str_upper(str);
		if (str == "YES")
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}

