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

/********************************************************************CODE*********************************************************************/

bool visited[1'000'000];
int A[1000][1000];
int n,m;

int dfs(int r, int c){
    if (visited[r*m+c]) return 0;;
    visited[r*m+c] = true;
    int s = 1;
    int walls = A[r][c];
    bool cangoup         = 1 - ((walls >> 3) & 1);
    bool cangoright      = 1 - ((walls >> 2) & 1);
    bool cangodown       = 1 - ((walls >> 1) & 1);
    bool cangoleft       = 1 - ((walls ) & 1);
    if (cangoup && r > 0) s += dfs(r-1, c);
    if (cangodown  && r < n-1) s += dfs(r+1, c);
    if (cangoleft && c > 0) s += dfs(r, c-1);
    if (cangoright && c < m-1) s += dfs(r, c+1);
    return s;
}

void solve(){
     cin >> n;
     cin >> m;

    fo(r,n){
        fo(c, m){
            cin >> A[r][c];
        }
    }
    vector<int> hmm;

    fo(cell, n*m){
        int r = cell / m;
        int c = cell % m;

        int x = dfs(r,c);
        if (x > 0) hmm.pb(x);
    }
    sort(hmm.begin(), hmm.end(), greater<int>());

    for( int k: hmm){
        cout << k << sp;
    }


    

    
}

int main()
{
    fast();
    int t;
    t = 1;
    while(t--){
        solve();
    }
}
