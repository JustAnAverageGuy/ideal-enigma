#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << k << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           push_back(x)
#define         N_MAX           (200000+5)
#define         A_MAX           (1000000000+9)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}

void dfs(int node){
    // just reached the node

    for (int child : graph[node]){
        // trying to reach child

        dfs(child);
        // exited the child
    }
    // exiting the node
}
*/
/********************************************************************CODE*********************************************************************/


bool A[1001][1001];
bool visited[1001][1001];

bool dfs(int i, int j, int n, int m){
    // just reached the node 
    if (i < 0 || i >= n || j < 0 || j >= m || !A[i][j] || visited[i][j]){ return 0;}

    visited[i][j] = 1;

    dfs(i-1,j,n,m);
    dfs(i,j-1,n,m);
    dfs(i+1,j,n,m);
    dfs(i,j+1,n,m);
    // exiting the node
    return 1;
}


int main()
{
    fast();
    int n;
    cin >> n;
    int m;
    cin >> m;
    fo(i,n){
        string s;
        cin >> s;
        fo(j,m){
            A[i][j] = (s[j]=='.');
            visited[i][j] = 0;
        }
    }

    int ct = 0;
    fo(i,n){
        fo(j,m){
            ct += dfs(i,j,n,m);
        }
    }
    print(ct);
}