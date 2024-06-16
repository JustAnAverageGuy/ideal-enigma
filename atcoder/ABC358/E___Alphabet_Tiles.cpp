// #define         MOD             ((int)(1e9 + 7))
#define         MOD             (998244353)
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

ll factorial[1005];
ll inverse_factorial[1005];
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}


int k;
int ci[26];
int dp(int count_remaining, int idx_completed, vector<int> freq_acquired){
    if(count_remaining == 0 || idx_completed == 25){

    }
}

int main()
{
    fast(); 

    cin >> k;
    for(int i = 0; i < 26; i++){ cin >> ci[i]; }

    factorial[0] = inverse_factorial[0] = 1;

    for(int i =1; i <= 1001; i++){
        factorial[i] = (factorial[i-1] * i)%MOD;
        inverse_factorial[i] =  powmod(factorial[i], MOD-2);
    }
        

}
