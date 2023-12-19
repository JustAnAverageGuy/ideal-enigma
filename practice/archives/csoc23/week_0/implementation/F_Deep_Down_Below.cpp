#define MOD 1e9 + 7
#define fo(i, n) for (int i = 0; i < n; ++i)
#define print(k) cout << k << '\n';
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
#define pb(x) push_back(x)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

void solve()
{
    int n;
    cin >> n;
    vector<vector<int>> caves;
    int k;
    fo(_, n)
    {
        vector<int> cave;
        cin >> k;
        cave.pb(k);
        fo(_, k)
        {
            int ai;
            cin >> ai;
            cave.pb(ai);
        }
        caves.pb(cave);
    }
    vector<pair<int,int>> min_pows;
    for (auto cave : caves)
    {
        int k = cave[0];
        int min_pow = cave[k - 1] + 1;
        for (int j = k - 1; j > 0; --j)
            min_pow = max(min_pow - 1, cave[j] + 1);
        min_pows.pb(make_pair(min_pow,k));
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    fast();
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}