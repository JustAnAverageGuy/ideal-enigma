#define MOD 1e9 + 7
#define fo(i, n) for (int i = 0; i < (n); ++i)
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
void solve()
{
    int n, m;
    cin >> n >> m;
    if (m < n)
    {
        print("No");
        return;
    }
    if (m % n == 0)
    {
        print("Yes");
        int t = m / n;
        fo(i, n) { cout << t << " "; };
        cout << "\n";
        return;
    }
    if (n % 2)
    {
        print("Yes");
        fo(i, n - 1) { cout << "1 "; }
        print(m - n + 1);
        return;
    }
    if (n % 2 == 0)
    {
        if (m % 2)
        {
            print("No");
            return;
        }
        print("Yes");
        fo(i, n - 2) { cout << "1 "; }
        cout << (m - n + 2) / 2 << " " << (m - n + 2) / 2 << "\n";
        return;
    }
};
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    fast();
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}