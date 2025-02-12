#include <cstring>
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




ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
const int inv = powmod(10000, MOD - 2, MOD);

int A[2'00'000+5];
ll  P[2'00'000+5];

ll currp[1024];
ll nexp[1024];

void solve() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++) {
        ll x;
        cin >> x;
        P[i] = (1LL * x * inv) % MOD;
    }

    memset(currp, 0, sizeof(ll)*1024);
    currp[0] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 1024; j++) {
            nexp[j] = (
                                (1LL * currp[j]        * (((1 - P[i]) + MOD)%MOD) )%MOD
                              + (1LL * currp[j ^ A[i]] * P[i]) % MOD
                        )%MOD;
        }
        swap(currp, nexp);
    }

    long long s = 0;
    for (int j = 0; j < 1024; j++) {
        s += ((1LL * j * j)%MOD * currp[j]) % MOD;
        s %= MOD;
    }

        print(s);
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
