#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << k << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           push_back(x)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

vector<int> G[1000000 + 2];
bool visited[1000000 + 2];

bool splittable[1000000 + 2];
bool children_paired_up[1000000 + 2];

bool can_split(int v){
    visited[v] = true;
    // do stuff to v

    if (G[v].size() == 0) { splittable[v] = false;return false;}
    
    int cnt = 0;
    int unpaired_child = -1;

    for(auto i: G[v]){
        if (! visited[i]) {
            bool r = (!can_split(i));
            if (r) {cnt++;}
            unpaired_child = i;
        };
    }
    if (cnt > 1) {splittable[v] = false; children_paired_up[v] = false; return false;}
    if (cnt == 1) {
        if (children_paired_up[unpaired_child])
        {splittable[v] = true; return true;}
        else {
            return false;
        }
    }
    // now all children are paired up
    if (cnt == 0) {splittable[v] = false; children_paired_up[v] = true; return false;}
    // so we need to tell the parent that we can pair up
    return false;
}

void solve(){
    int n;
    cin >> n;
    // vector<vector<int>> G(n); // list of children
    // vector<bool> visited(n,false); 
    for(int i = 1; i < n+1; i++) {G[i].clear();visited[i] = false;splittable[i] = false;children_paired_up[i] = false;}
    fo(i,n-1){
        int p;
        cin >> p;
        G[p].pb(i+2);
    }
    can_split(1);
    for (int i = 1; i < n +1 ; i++) {print((splittable[i]?"YES":"NO"));}

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