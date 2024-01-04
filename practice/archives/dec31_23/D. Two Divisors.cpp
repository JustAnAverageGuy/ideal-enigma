#include <cmath>
#include <vector>
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
vector<int> d1;
vector<int> d2;

void prime_factors(int n, int *res1, int *res2){

    int t = n;
    int cnt = 0;
    map<int,int> f;
    
    
    if (!(t & 1)){
        cnt++;
        while (!(t&1)){
            f[2]++;
            t>>=1;
        }
    }
    if (cnt == 1){
        *res1 = (1<<f[2]);
        if (t == 1){
            return;
        }
        *res2 = t;
        return;
    }

    int i = 3;
    while (i*i <= t && cnt < 1){
        if (t%i == 0){
            cnt++;
            while (t%i == 0){
                f[i]++;
                t /= i;
            }
        }
        i += 2;
    }
    if (t > 1) f[t]++;
    if (f.size() == 1) return;
    auto it = f.begin();
    *res1 = pow(it->first, it->second);
    *res2 = t;
}

void solve(){
    int n; cin >> n;
    int res1,res2;
    res1 = -1;
    res2 = -1;
    prime_factors(n, &res1, &res2);
    if (res1 == -1 || res2 == -1){
        d1.pb(-1); d2.pb(-1);
    } else {
        d1.pb(res1); d2.pb(res2);
    }

}

int main()
{
    fast();
    int t;
    cin >> t;
    while(t--){
        solve();
    };
    for(auto x: d1) cout << x << sp;
    cout << nl;
    for(auto x: d2) cout << x << sp;
    cout << nl;
}
