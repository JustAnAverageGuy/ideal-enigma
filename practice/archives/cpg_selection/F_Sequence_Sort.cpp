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
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

ll A[1000000+3];
int positions[1000000+3];
int B[1000000+3];

ll ans[1000000+3];
void solve(){
    int n; cin >> n;
    for(int i = 1; i <= n; i++) cin >> A[i];
    int q; cin >> q;
    ll K[61] = {0};
    fo(i,q) {int x; cin >> x; ++K[x];}

    for(int i = 1; i <= n; i++){positions[i] = i; B[i] = i;ans[i] = 0;}
    
    for(int k = 1; k <= 60; ++k){
        int ones = 0;
        int zeroes = 0;
        for(int i = 1; i<= n ; i++){
            if ((A[B[i]] >> (k-1))&1) ones++;
            else positions[B[i]] -= ones;

            if ((A[B[n+1-i]] >> (k-1)) & 1) positions[B[n+1 - i]] += zeroes;
            else zeroes += 1;
        }

        for (int i=1; i<=n; i++){
            B[positions[i]] = i;
            if (K[k]) ans[i] += K[k] * positions[i];
        }

    }
    for (int i = 1; i<=n; i++) cout << ans[i] << " ";
    cout << "\n";
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