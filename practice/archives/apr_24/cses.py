#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
#define         elif            else if
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           emplace_back(x)
#define         N_MAX           (200000+5)
#define         A_MAX           (1000000000+7)
#define         nl              ('\n')
#define         sp              (' ')
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

void solve(){
    int n,x;
    cin >> x >> n;
    multiset<int> lns;
    set<int> endpoints;
    endpoints.insert(0);
    endpoints.insert(x);
    lns.insert(x);

    for(int i = 0; i < n; i++){
        int p; cin >> p;

        int ls = *(--endpoints.lower_bound(p));
        int rs = *endpoints.upper_bound(p);


        // cout << i << sp << ls << sp << p << sp << rs << nl;
        int ln = rs - ls;
        lns.erase(lns.find(ln));
        lns.insert(rs - p);
        lns.insert(p - ls);

        // for (auto i: lns) {
        //     cerr << i << sp;
        // }
        // cerr << nl;

        cout << *lns.rbegin() << sp;

        endpoints.insert(p);



    }

        
        
}

int main()
{
    fast();
    int t;
    // cin >> t;
    t = 1;
    while(t--){
        solve();
    }
}
