#define MOD ((int)(1e9 + 7))
#define fo(i, n) for (int i = 0; i < n; ++i)
#define print(k) cout << k << '\n';
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
#define pb(x) emplace_back(x)
#define N_MAX (200000 + 5)
#define A_MAX (1000000000 + 7)
#define nl ('\n')
#define sp (' ')
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

int main()
{
    fast();
    int n;
    cin >> n;

    set<int> all_factors;
    
    int x = 0;
    int gcd = -1;
    
    fo(i, n)
    {
        int t;
        cin >> t;
        x = max(x, t);
        if(all_factors.count(t)) gcd = max(t,gcd);
        all_factors.insert(t);
    }
    int y = gcd;
    // print("gcd="<<gcd)
    for (auto f: all_factors){
        if (x % f) y = max(f,y);
    }
    // int y = *all_factors.rbegin();
    // int y = 0;
    
    print(x<<sp<<y);
}