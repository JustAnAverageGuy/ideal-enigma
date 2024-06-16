// #define         MOD             ((int)(1e9 + 7))
#define         MOD             ((int)(998244353))
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

int A[5000];
bool dp[5001][5001];
// dp[i][j] = 1 if some subset of A[:i] has sum j else 0

int main()
{
    fast();
    int n; cin >> n;
    fo(i,n) cin >> A[i];

    fo(i, 5001) dp[i][0] = true;
    for(int i = 1; i <= 5000; i++) dp[0][i] = false;

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= 5000; j++){
            dp[i][j] = dp[i-1][j];
            if(A[i-1] <= j) dp[i][j] |= dp[i-1][j - A[i-1]];
        }
    } 







}
