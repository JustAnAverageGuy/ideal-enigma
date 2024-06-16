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
int t = 0;

int dfs(int node, int arr[], int in[], vector<int> &value, int siz[], int n, int p, vector<vector<int>> &adj){
    t++;
    in[node] = t;
    value.pb(arr[node]);
    // cerr << node << sp;
    int s = 1;
    
    for(int nei : adj[node]) {
        if(nei!=p) {
            s += dfs(nei, arr, in,  value, siz, n, node, adj);
        }
    }
    
    siz[node] = s;
    return s;
};

void solve(){
    int n; cin >> n;
    int q; cin >> q;
    int arr[n+1];
    fo(i,n) cin >> arr[i+1];
    vector<vector<int>> adj(n+1);
    fo(i, n-1){
        int u,v; cin >> u >> v;
        adj[u].pb(v);
        adj[v].pb(u);
    }
     
    t = 0;
    int in[n+1];
    vector<int> value;
    int siz[n+1];
    value.pb(-1);

    dfs(1, arr, in,  value, siz, n, 0, adj);
    
    for(int i=1;i<=n;i++) {
        cout << in[i] << " ";
    }
    cout << endl;
    for(int i=1;i<=n;i++) {
        cout << value[i] << " ";
    }
    cout << endl;
    for(int i=1;i<=n;i++) {
        cout << siz[i] << " ";
    }
    cout << endl;
}

int main()
{
    fast();
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
}
