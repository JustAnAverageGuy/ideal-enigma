#define MOD 1e9 + 7
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

void solve()
{
    int n, m;
    cin >> n >> m;
    vector<int> deg(n, 0);
    fo(i, m)
    {
        int u, v;
        cin >> u >> v;
        deg[u-1]++;
        deg[v-1]++;
    }
    int x,y;
    bool is_init_x{false},is_init_y{false};
    for (auto i: deg){
        if (i == 1) continue;
        if( !is_init_x){
            is_init_x = true;
            x = i;
            continue;
        }
        if (x != i) {cout << x << " " << (((n-1)/x) - 1) << "\n"; return;}; // we have found correct x
        // now the x actually contains y + 1
        y = x - 1; 
        cout << (n-1)/(1+y) << " " << y << "\n";
        return;
    }
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
