#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           push_back(x)
#define         N_MAX           (200000+5)
#define         A_MAX           (1000000000+5)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

ll heights[N_MAX];
ll fruits[N_MAX];
ll prefix_fruits[N_MAX];

void solve(){
    memset(heights,0,sizeof(ll)*N_MAX);
    memset(fruits,0,sizeof(ll)*N_MAX);
    memset(prefix_fruits,0,sizeof(ll)*N_MAX);
    int n; cin >> n;
    int k;
    cin >> k;
    fo(i,n){cin >> fruits[i];prefix_fruits[i+1] = prefix_fruits[i] + fruits[i];}
    fo(i,n){cin >> heights[i];}
    vector<pair<ll,ll>> div_pairs;
    
}

int main()
{
    fast();
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}