#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
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

int A[N_MAX];
int G[N_MAX];
bool visited[N_MAX];
int dfs(int node,vector<int> *cycle){
    // cout << "trying to dfs " << node << '\n';
    if (visited[node]) return 0;
    visited[node] = 1;
    cycle->emplace_back(node);
    dfs(G[node], cycle);
    return 1;
}
const ll inv_2 = 500000004;

void solve(){
    int n; cin >> n;
    fo(i,n){cin >> A[i];}
    fo(i,n){
        int b;
        cin >> b;
        G[A[i]] = b;
    }
    
    ll ans = 1;
    
    set<int> known;
    fo(i,n){int x; cin >> x; known.insert(x);}
    memset(visited,0,sizeof(bool)*N_MAX);
    for(int i = 1; i <= n; ++i){
        vector<int>* cycle = new vector<int>();
        int new_dfs = dfs(i, cycle); 
        if (new_dfs && cycle->size() > 1) {
            bool know_n = false;
            for(auto j: *cycle){
                if(known.count(j)){
                    know_n = true;
                    known.erase(j);
                }
            }
            if (! know_n) { ans <<=1; ans %= MOD;}
        }
    }
    print(ans);



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