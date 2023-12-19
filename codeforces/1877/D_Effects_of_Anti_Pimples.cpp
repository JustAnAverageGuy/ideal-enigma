#define         MOD             (998244353)
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << k << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           emplace_back(x)
#define         N_MAX           (100000+5)
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

int A[N_MAX];
int main()
{
    fast();
    int n; cin >> n;

    fo(i,n) cin >> A[i+1];

    for (int j = 1; 2*j <= n; j++ ){
        int m = A[j];
        for (int k = 2*j; k <= n; k+=j) m = max(m, A[k]);
        A[j] = m;
    }

    sort(A+1,A+n+1);
    ll ans = 0;
    ll po = 1;
    for (int i = 1; i <= n; i++){
        ans += (A[i]*po)%MOD;
        ans %= MOD;
        po <<= 1;
        po %= MOD;
    }
    print(ans);


}