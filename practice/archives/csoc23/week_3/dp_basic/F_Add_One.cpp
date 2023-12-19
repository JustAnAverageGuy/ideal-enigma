#define MOD ((int)(1e9 + 7))
#define fo(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define print(k) cout << (k) << '\n';
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
#define pb(x) push_back(x)
#define nl '\n'
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

/* 
    !!!!!!!!!!!!!!!!!!!!!!!!!!!
        WHY TF IS IT WORKING IN CPP 
        WHILE IT TAKES A WHOLE 
        FUCKING SECOND FOR PRECOMPUTATION IN PYTHON
    !!!!!!!!!!!!!!!!!!!!!!!!!!!
*/
ll dp[200010][10];

int main()
{
    fast();

    memset(dp,0,sizeof(dp));

    fo(i, 10) dp[0][i] = 1;

    for (int i = 1; i < 200007; i++)
    {
        fo(x, 9)
        {
            dp[i][x] = dp[i - 1][x + 1];
        }
        dp[i][9] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
    }

    int t;
    cin >> t;
    while (t--)
    {
        int n,m;
        cin >> n >> m;
        ll ans = 0;
        while (n > 0){
            ans = (ans +dp[m][n%10]) % MOD;
            n /= 10;
        }
        print(ans);
    }
}