/**
 *	Author:		antikostya
 *	Created:	2021-10-02 14:52:59
 *	Modified:	2021-10-02 15:37:15
 **/

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace::std;

class box
{
public:
	uint			del_id;
	vector<uint>	next;

	box(void)
	{
		del_id = 0;
	}

	box(uint _del_id)
	{
		del_id = _del_id;
	}
};

vector<box>	boxes;
set<uint>	st;

void	dfs(uint mybox)
{
	for (uint bx : boxes[mybox].next)
	{
		st.insert(boxes[bx].del_id);
		dfs(bx);
	}
}

#define vec_input(__vec, __size) \
	do { \
		__vec.resize(__size); \
		for (uint __i=0; __i < __size; ++__i) \
			std::cin >> __vec[__i]; \
	} while (0)

#define vec_print(__vec) \
	do { \
		for (const auto &__it : __vec) \
			std::cout << __it << ' '; \
		std::cout << endl; \
	} while (0)

int	main(void)
{
	uint	n, k;

	vector<uint>	delivery;
	vector<uint>	parent;
	vector<uint>	out;
	vector<uint>	roots;
	vector<uint>	ans;

	cin >> n;
	vec_input(delivery, n);
	vec_input(parent, n);
	cin >> k;
	vec_input(out, k);

	boxes.resize(n);
	for (uint i=0; i < n; ++i)
	{
		boxes[i] = box(delivery[i]);
	}
	for (uint i=0; i < n; ++i)
	{
		if (parent[i] == 0)
			roots.push_back(i);
		else
			boxes[parent[i] - 1].next.push_back(i);
	}

	set<uint>	inter;
	for (uint rt : roots)
	{
		st.clear();
		st = {boxes[rt].del_id};
		dfs(rt);
		inter.clear();
		set_intersection(
			st.begin(), st.end(),
			out.begin(), out.end(),
			inserter(inter, inter.begin())
		);
		if (inter.size() == 0)
			ans.push_back(rt + 1);
	}
	cout << ans.size() << endl;
	vec_print(ans);
}
