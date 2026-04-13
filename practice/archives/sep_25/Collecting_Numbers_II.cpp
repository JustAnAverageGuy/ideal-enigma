#include <cstring>
#include <utility>
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
    int n,m;
    cin >> n >> m;
    int A[N_MAX], pos[N_MAX+2];
    memset(pos, -1, sizeof(int)*(N_MAX+2));
    pos[n+1] = n+1;
    fo(i, n) {cin >> A[i]; pos[A[i]] = i;}
    int ops = 0;
    fo(i, n+1) ops += (pos[i] > pos[i+1]);

    int i,j, a, b;
    fo(_, m){
        cin >> i >> j;
        a = A[--i];
        b = A[--j];

        set<pair<int, int>> pairs = {
            {a-1, a},
            {a, a+1},
            {b-1, b},
            {b, b+1},
        };

        for(auto x: pairs) ops -= (pos[x.first] > pos[x.second]);
        // swap(A[i], A[j]);
        int t;
        t = A[i];
        A[i] = A[j];
        A[j] = t;

        pos[a] = j;
        pos[b] = i;
        for(auto x: pairs) ops += (pos[x.first] > pos[x.second]);
        print(ops+1);

    }


}
