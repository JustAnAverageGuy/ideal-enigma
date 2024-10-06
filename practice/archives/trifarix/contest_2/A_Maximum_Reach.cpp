#define         MOD             ((int)(1e9 + 7))
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

int main()
{
    fast();
    int n; cin >> n;
    int A[1'000'05];
    fo(i,n) cin >> A[i];    

    set<int> hmm = {};

    int ans[1'000'05];

    for (int i = n-1; i >= 0; --i) {
        hmm.insert(A[i]);
        ans[i] = distance(hmm.upper_bound(A[i]), hmm.end());
    }
    fo(i,n) cout << ans[i] << sp;
}