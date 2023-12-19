#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int (i)=0; (i) < (n); ++(i))
#define         print(k)        cout << (k) << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           push_back(x)
#define         nl              '\n'
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

void solve(){
    int n;
    cin >> n;
    map<ll,ll> A[4];
    int x,y;
    fo(i,n){
        cin >> x >> y;
        A[0][y]   += 1;
        A[1][x]   += 1;
        A[2][x-y] += 1;
        A[3][x+y] += 1;
    };
    ll ans = 0;
    fo(i,4){
        for(auto x: A[i]){
            ans += (x.second * x.second - x.second);
        }
    }
    print(ans);
    
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