#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           push_back(x)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
*/

/********************************************************************CODE*********************************************************************/
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k >>= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
int  A[100000+5];
// ll ans[200000+5];
void solve(){
    int n; cin >> n;
    map<int,int> count;
    fo(i,n) {cin >> A[i]; ++count[A[i]];}
    int q; cin >> q;

    fo(Q,q){
        ll s,p;
        cin >> s >> p;
        ll d = s*s-4*p;
        if (d < 0){
            cout << 0 << ' ';
            continue;
        }
        ll k = int_sqrt(d);
        if (k*k != d){
            cout << 0 << ' ';
            continue;
        }
        if (k != 0){
            ll a = (s+k)/2;
            ll b = (s-k)/2;
            cout << count[a]*count[b] << ' ';
            continue;
        }
        ll a = s/2;
        a = count[a];
        cout << (a*a - a)/2 << ' '; 
    }
    cout << '\n';
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