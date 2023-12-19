#define MOD 1e9 + 7
#define fo(i, n) for (int(i) = 0; (i) < (n); ++(i))
#define print(k) cout << (k) << '\n';
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
#define pb(x) push_back(x)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/
#define MAX 200010
void solve()
{
    int n, m;
    cin >> n >> m;
    // vector<int> A;
    int M[MAX + 1] = {0};
    fo(i, n)
    {
        int k;
        cin >> k;
        // A.pb(k);
        M[k] += 1;
    }
    int l, r;
    l = 1;
    r = 3*MAX;
    while (l <= r)
    {
        int mid = l + (r - l) / 2;
                int t = mid;
                ll extra_work{0}, backlog{0};
                bool res = 0;
                for (int i = 1; i <= n; ++i)
                {
                    if (t >= M[i])
                    {
                        extra_work += (t - M[i]) / 2;
                    }
                    else
                    {
                        backlog += (M[i] - t);
                    }
                }
                if (backlog > extra_work)
                {
                    res = false;
                }
                else
                {
                    res = true;
                }
        if (res)
        {
            l = l;
            r = mid - 1;
        }
        else
        {
            l = mid + 1;
            r = r;
        }
    }
    print(r + 1);
}

int main()
{
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif
    fast();
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}