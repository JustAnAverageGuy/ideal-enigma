#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           emplace_back(x)
#define         N_MAX           (200000+5)
#define         A_MAX           (1000000000+7)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

void solve(){
    int n; cin >> n;
    vector<pair<pair<ll,ll>,pair<ll,ll>>> lines;
    fo(i,n){
        ll xa,ya,xb,yb;
        cin>>xa>>ya>>xb>>yb;
        pair<ll,ll> slope,intercept;
        
        if (xa == xb) {
            ll g = gcd(ya-yb,xa-xb);
            slope = {(ya-yb)/g,(xa-xb)/g};
            g = gcd(yb*xa-ya*xb,xa-xb);
            intercept = {(yb*xa-ya*xb)/g, (xa-xb)/g};

        } else {
            slope = {0,0};
            intercept = {xb,0};
        }
        lines.pb(make_pair(slope,intercept));
    }
    
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