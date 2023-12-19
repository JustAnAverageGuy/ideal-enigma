#define         MOD             1e9 + 7
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           push_back(x)
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
    int x;
    cin >> n;
    vector<int> B;
    cin >> x;
    B.pb(x);
    int last = x;
    for(int i=1;i < n; i++) {
        cin >> x;
        if (x >= last) {B.pb(x); last = x;}
        else {B.pb(1); B.pb(x); last = x; }
    }
    print(B.size());
    for(auto i: B) {cout<<i <<' ';}
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