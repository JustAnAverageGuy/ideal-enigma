#include <algorithm>
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

int nimbers[5'000'001];
// nimbers[i] = nim[2*i+1]

const int N = 10'000'001;
vector<int> lp(N+1);
vector<int> pr;

// https://oeis.org/A038802
// oeis[i] = nim[2*i+1] - 1

void gennimbers(){
for (int i=2; i <= N; ++i) {
    if (lp[i] == 0) {
        lp[i] = i;
        pr.push_back(i);
    }
    for (int j = 0; i * pr[j] <= N; ++j) {
        lp[i * pr[j]] = pr[j];
        if (pr[j] == lp[i]) {
            break;
        }
    }
}
    nimbers[1/2] = 1;
    for(int i = 3; i <= N; i += 2 ){
        int leastprim = lp[i];
        // find index of leastprim
        auto l = lower_bound(pr.begin(), pr.end(), leastprim);
        int c = (l - pr.begin());
        nimbers[i/2] = c+1;
    }

}
void solve(){
    int n; cin >> n;
    int xr = 0;
    fo(i,n){
        int a;
        cin >> a;
        if ((a&1)==0) continue;
        xr ^= nimbers[a/2];
    }
    cout << (xr?"Alice":"Bob") << nl;
    
}

int main()
{
    gennimbers();
    fast();
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
