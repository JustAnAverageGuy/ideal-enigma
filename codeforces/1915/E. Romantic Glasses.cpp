#include <set>
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

bool solve(){
    int n; cin >> n;
    set<ll> seen;
    ll sm = 0;
    ll tmp;
    bool ok = false;
    fo(i,n){
        cin >> tmp;
        
        // cerr << "Got " << tmp << nl;

        if (i%2) sm -= tmp;
        else sm += tmp;
        if (sm == 0|| seen.count(sm)) ok = true;
        seen.insert(sm);
    }
   
    // cerr << "n= " << n<<nl;
    // for(auto u: seen) cerr << u << sp;
    // cerr<<nl;
    //
    return ok;
}

int main()
{
    fast();
    int t;
    cin >> t;
    while(t--){
        
        // cerr << "Case "<<t<<nl;

        cout << (solve()?"YES":"NO")<<nl;
    }
}
