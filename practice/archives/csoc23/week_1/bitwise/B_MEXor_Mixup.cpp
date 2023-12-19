#define MOD 1e9 + 7
#define fo(i, n) for (int i = 0; i < n; ++i)
#define print(k) cout << (k) << '\n';
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

vector<int> xors;

void solve()
{
    int a, b;
    cin >> a >> b;
    int s = xors[a - 1] ^ b;
    if (s == a)
    {
        print(a + 2);
        return;
    }
    print(a + 1 - (s == 0));
    return;
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
    int curr = 0;

    fo(i, 300010)
    {
        xors.pb(curr ^= i);
    }
    // fo(i, 15) print(xors[i]);
    while (t--)
    {
        solve();
    }
}