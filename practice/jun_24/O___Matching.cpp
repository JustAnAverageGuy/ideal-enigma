#include <cstring>
#include <vector>
#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << k << '\n';
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

int cache[(1<<21)];
vector<vector<bool>> A;
int n;

int cnt_perm(int taken = 0){
    int currman = __builtin_popcount(taken);
    if (currman >= n) return  1;
    if (cache[taken] != -1) return cache[taken];
    ll s = 0;
    for(int i = 0; i < n; i++){
        if ((! ((taken >> i)&1)) &&  A[currman][i]){
            s += cnt_perm(taken | (1 << i));
            s %= MOD;
        }
    }
    return cache[taken] = s;
}

int main()
{
    fast();
        
     cin >> n;
    for(int i = 0; i < n; i++){
        vector<bool> v;
        bool k;
        for (int j = 0; j < n; j++){
            cin >> k;
            v.pb(k);
        }
        A.pb(v);
    }

    memset(cache, -1, (1<<21)*sizeof(int));
    print(cnt_perm());
    

}
