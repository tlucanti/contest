/*
* @Author: kostya
* @Date:   2021-11-13 15:35:40
* @Last Modified by:   kostya
* @Last Modified time: 2021-11-13 15:38:17
*/

#include <iostream>

using namespace::std;

int main()
{
	int n;
	for (int i=0; i < 25; ++i)
	{
		cin >> n;
		if (n == 1)
			cout << abs(i / 5 - 2) + abs(i % 5 - 2) << endl;
	}
}
