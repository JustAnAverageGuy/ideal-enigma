#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
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

int A[N_MAX][18];

bool check(int l,int r, int k){
    if (r < l) return false;
    int len = r - l + 1;
    int v = len;
    int lg = 0;
    while (v >>= 1) lg++;
    return (A[l][lg] & A[r - (1 << lg)+1][lg]) < k;

}

void solve(){
    int n; cin >> n;
    fo(i,n){
        cin >> A[i][0];
    }

    for(int j = 1; j < 18; ++j){
        for(int l = 0; l + (1<<j)-1 < n; ++l){
            A[l][j] = A[l][j-1] & A[l + (1<<(j-1))][j-1];
        }
    }
    
    /* PREPROCESS HERE */
    
    int q;
    cin >> q;
    fo(i,q){
        int l0,k;
        cin >> l0 >> k;
        --l0;
        if(A[l0][0] < k) {cout << -1 << sp; continue;}

        int l = l0, r = n;
        while(r - l > 1) {
            int m = (l + r) / 2;
            if(check(l0, m, k)) {
                r = m; // 0 = f(l) < f(m) = 1
            } else {
                l = m; // 0 = f(m) < f(r) = 1
            }
        }
        cout << l + 1 << sp;

    }
    cout << nl;
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