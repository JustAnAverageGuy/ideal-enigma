#define MOD ((int)(1e9 + 7))
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
    ll n;
    cin >> n;
    vector<ll> v(n);
    ll o = 0;
    fo(i, n)
    {
        cin >> v[i];
        if (v[i] == 1)
            o++;
    }
    sort(v.begin(), v.end());
    ll left = o % 3;
    ll ans = 1;
    if (left == 1)
    {
        fo(i, o / 3 - 1)
        {
            ans *= 3;
            ans %= MOD;
        }
    }
    else
    {
        fo(i, o / 3)
        {
            ans *= 3;
            ans %= MOD;
        }
    }
    if (left == 2)
    {
        ans *= 2;
        ans %= MOD;
    }
    else if (left == 1)
    {
        if (o >= 2)
            ans *= 4;
        else if (o < 2)
            v[1]++;
        ans %= MOD;
    }
    fo(i, n)
    {
        if (v[i] != 1)
        {
            ans *= v[i];
            ans %= MOD;
        }
    }
    print(ans);
}

int main()
{
    fast();

    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}