
#include <bits/stdc++.h>

enum SegTreeType {
	SEGTREE_MIN,
	SEGTREE_MAX,
	SEGTREE_SUM
};

template <class T, enum SegTreeType type>
class SegTree {
private:
	std::vector<T> tree;
	const std::vector<T> &in;
	size_t n;

public:
	SegTree(const std::vector<T> &in)
		: in(in), n(in.size())
	{
		tree.resize(n * 4);

		dfs_build(1, 0, n - 1);
	}

	T query(size_t left, size_t right)
	{
		bool dummy;

		if (left > right || right > n) {
			std::abort();
		}
		return dfs_query(1, 0, n - 1, left, right, dummy);
	}

private:
	T conv(const T &a, const T &b)
	{
		switch (type) {
		case SEGTREE_MIN: return std::min(a, b);
		case SEGTREE_MAX: return std::max(a, b);
		case SEGTREE_SUM: return a + b;
		default: std::abort();
		}
	}

	T dfs_query(size_t idx, size_t tl, size_t tr, size_t left, size_t right, bool &ok)
	{
		size_t c = (tl + tr) / 2;
		T r1, r2;
		bool ok1, ok2;

		ok = true;
		if (left > right) {
			ok = false;
			return T();
		}

		if (tl == left and tr == right) {
			return tree.at(idx);
		}

		r1 = dfs_query(idx * 2, tl, c, left, std::min(right, c), ok1);
		r2 = dfs_query(idx * 2 + 1, c + 1, tr, std::max(left, c + 1), right, ok2);

		if (ok1 and ok2) {
			return conv(r1, r2);
		} else if (ok1) {
			return r1;
		} else if (ok2) {
			return r2;
		} else {
			std::abort();
		}
	}

	void dfs_build(size_t idx, size_t start, size_t end)
	{
		size_t c = (start + end) / 2;

		if (start == end) {
			tree.at(idx) = in.at(start);
			return;
		}

		dfs_build(idx * 2, start, c);
		dfs_build(idx * 2 + 1, c + 1, end);

		tree.at(idx) = conv(tree.at(idx * 2), tree.at(idx * 2 + 1));
	}
};

int main()
{
	int n, q;

	std::cin >> n >> q;
	std::vector<int> v(n);

	for (int i = 0; i < n; ++i) {
		std::cin >> v.at(i);
	}

	SegTree<int, SEGTREE_MAX> tree_max(v);
	SegTree<int, SEGTREE_MIN> tree_min(v);

	for (int i = 0; i < q; ++i) {
		int a, b;
		int mi, ma;

		std::cin >> a >> b;
		mi = tree_min.query(a, b);
		ma = tree_max.query(a, b);
		if (mi != ma) {
			std::cout << ma << '\n';
		} else {
			std::cout << "NOT FOUND\n";
		}
	}

}
