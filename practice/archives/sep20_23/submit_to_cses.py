#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << k << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           emplace_back(x)
#define         N_MAX           (200000+5)
#define         A_MAX           (1000000000+7)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

int main()
{
    fast();
    int n;
    cin >> n;

    int isDivisor[(int) 1e6+1] = {0};
    fo(i,n){
        int x;
        cin >> x;
        for(int j = 1; j*j <= x; j++){
            if (x % j == 0){ isDivisor[j]++;
            if (j*j != x) isDivisor[x/j]++;}
        }
    }
    // fo(i,30){cout << i << ':' <<  isDivisor[i] << '\n';}
    for(int i = 1e6; i > 0; i-- ){
        if(isDivisor[i] > 1){
            print(i);
            return 0;
        }
    }
}