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

int times[200010];

void solve()
{

    int n, m, h;
    cin >> n >> m >> h;

    int score = 0;
    ll penalty = 0;
    ll t = 0;
    for (int j = 0; j < m; j++)
    {
        cin >> times[j];
    }
    sort(times, times + m);

    while (score < m)
    {
        if (times[score] + t > h)
            break;
        t += times[score];
        score += 1;
        penalty += t;
    }
    int sc_rudolf = score;
    ll pen_rudolf = penalty;
    int rank = 1;

    for (int i = 1; i < n; i++)
    {
        int score = 0;
        ll penalty = 0;
        ll t = 0;
        for (int j = 0; j < m; j++)
        {
            cin >> times[j];
        }
        sort(times, times + m);

        while (score < m)
        {
            if (times[score] + t > h)
                break;
            t += times[score];
            score += 1;
            penalty += t;
        }

        if (score > sc_rudolf || (score == sc_rudolf && penalty < pen_rudolf))
            ++rank;
    }
    print(rank);
}

int main()
{
    fast();
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}