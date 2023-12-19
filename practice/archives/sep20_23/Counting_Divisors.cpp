#define MOD ((int)(1e9 + 7))
#define fo(i, n) for (int i = 0; i < n; ++i)
#define print(k) cout << k << '\n';
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
#define pb(x) emplace_back(x)
#define N_MAX (200000 + 5)
#define A_MAX (1000000000 + 7)
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

    const int N = 1000000;
    vector<int> lp(N + 1);
    vector<int> pr;

    for (int i = 2; i <= N; ++i)
    {
        if (lp[i] == 0)
        {
            lp[i] = i;
            pr.emplace_back(i);
        }
        for (int j = 0; i * pr[j] <= N; ++j)
        {
            lp[i * pr[j]] = pr[j];
            if (pr[j] == lp[i])
            {
                break;
            }
        }
    }
    int n;
    cin >> n;

    fo(i, n)
    {
        int x;
        cin >> x;
        map<int, int> factorization;
        while (x != 1)
        {
            factorization[lp[x]]++;
            x /= lp[x];
        }
        ll ans = 1;
        for (auto k : factorization)
        {
            ans *= k.second + 1;
        }
        print(ans);
    }
}