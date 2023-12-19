#define MOD ((ll)(1e9 + 7))
#define fo(i, n) for (ll i = 0; i < n; ++i)
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

ll corals[200000 + 3];

// ll prefix[200000 + 3];

bool check(ll h, ll n,ll x)
{
    // ll colms = upper_bound(corals, corals + n, h) - corals;
    // print(colms);
    ll s = 0;
    for (int i = 0; i < n; i++){
        auto k = corals[i];
        s += max(h - k,0LL);
    }
    // cout << "water_required= " << s << "\n";
    // return !(colms * h - prefix[colms] <= x); 
    return !(s <= x);
}

void solve()
{   
    memset(corals,0,sizeof(ll) * (200000+3));
    // memset(prefix,0,sizeof(ll) * (200000+3));
    ll n;
    cin >> n;
    ll x;
    cin >> x;
    fo(i, n)
    {
        cin >> corals[i];
    }
    // sort(corals, corals + n);
    // prefix[0] = 0;
    // fo(i, n) { prefix[i + 1] += (prefix[i] + corals[i]); }

    // print(check(4,n,x))
    // check(4,n,10);
    ll l = 1, r = INT_MAX;
    while (r - l > 1)
    {
        ll m = (l + r) / 2;
        if (check(m, n, x))
        {
            r = m; // 0 = f(l) < f(m) = 1
        }
        else
        {
            l = m; // 0 = f(m) < f(r) = 1
        }
    }
    print(l);
}

int main()
{
    fast();
    ll t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}