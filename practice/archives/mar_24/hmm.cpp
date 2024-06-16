#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
#define int long long int
#define deb(x) cout << #x << "=" << x << endl
#define read(a, n)              \
	for (int i = 0; i < n; ++i) \
		cin >> a[i];
#define print(a, n)               \
	for (int i = 0; i < n; ++i)   \
		if (i == n - 1)           \
		{                         \
			cout << a[i] << "\n"; \
		}                         \
		else                      \
		{                         \
			cout << a[i] << ' ';  \
		}
#define trav(it, x) for (auto it = x.begin(); it != x.end(); it++)
#define f(a, start, end) for (int a = start; a < end; a++)
#define ft(a, end) for (int a = 0; a < end; a++)
#define fi(a, start, end, inc) for (int a = start; a < end; a += inc)
#define si(x) scanf("%lld", &x)
#define sll(x) scanf("%lld", &x)
#define ss(s) scanf("%s", s)
#define pi(x) printf("%d\n", x)
#define pll(x) printf("%lld\n", x)
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
// #define PI 3.14159265

typedef vector<int> vi;
typedef map<int, int> mii;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int MOD = (int)(1e9 + 7);

void solve()
{
	int n, k, z;
	cin >> n >> k >> z;
	vi v(n);
	read(v, n);
	vi pre(1, 0);
	for (int i = 0; i < n; i++)
		pre.pb(pre.back() + v[i]);
	vi max2sum(1, 0);
	for (int i = 0; i < n - 1; i++)
	{
		max2sum.pb(max(max2sum.back(), v[i] + v[i + 1]));
	}
	max2sum.pb(max2sum.back());
	int ans = v[1];
	for (int i = 0; i <= z; i++)
	{
		if (k >=2*i)
			ans = max(ans, pre[k + 1 - 2 * i] + i * max2sum[k + 1 - 2 * i]);
		else
			break;
	}
	cout << (ans) << endl;
}

int32_t main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t = 1;
	cin >> t;
	while (t--)
	{
		solve();
	}
	return 0;
}
