#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
#define         elif            else if
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           emplace_back(x)
#define         N_MAX           (500000+5)
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


vector<int> graph[N_MAX];
ll A[N_MAX];

ll dfs(int node,int parent=0){

    ll ans = A[node] + A[parent];

    for(auto children: graph[node]){
        dfs(children, node);
    }

    return ans;

}


void solve(){
    
    int n; cin >> n;
    
    memset(A,0,sizeof(ll)*(n+2));
    fo(i,n+2) graph[i+1] = vector<int>();

    cerr << "*************************\n";

    int sz = 1;
    fo(i,n){
        int t; cin >> t;
        if (t == 1) {
            // add child , so pre = -parent's values
            int v;
            cin >> v;

            cerr << "Append the child \"" << sz+1 << "\" to " << v << nl;

            graph[v].pb(sz+1);
            sz++;
            A[sz] = -A[v];

        } else {
            ll v,x; cin >> v >> x;

            cerr << "Add "<<x<< " to the subtree rooted at " << v << nl;

            A[v] += x;
        }
    }

    dfs(1);

    fo(i,n) { cout << A[i+1] << sp;}
    print("");
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