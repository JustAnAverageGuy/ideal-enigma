#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << k << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           emplace_back(x)
#define         N_MAX           (100000+5)
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

vector<int> G[N_MAX];

double dfs(int node, int par=-1){


    double ans = 0;

    int children_count = G[node].size() - 1 + (par == -1);
    if (children_count == 0)  return 0;

    for(auto child: G[node]) {
        if (child == par) continue;
        ans += dfs(child, node) / children_count; 
    }
    // print("Expected value of Node " << node << " = " << 1 + ans)
    return 1 + ans;

}

int main()
{
    fast();
    int n;
    cin >> n;

    fo(i,n-1){
        int u,v; cin >> u >> v;
        G[u].pb(v);
        G[v].pb(u);
    }
    cout.precision(15);
    print(dfs(1));


}