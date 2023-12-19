#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << (k) << '\n';
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

const int MAX_N = (1<<19); 
// const int MAX_A = ((1 << 31) - 1);
const int MAX_A = 2147483647;
int tree[MAX_N];

int range(int node, int low, int high, int left, int right){

    if( low <= left && right <= high ) return tree[node];

    if( right < low || left > high) return MAX_A;

    return range(2*node,low,high,left, (left+right)/2) & range(2*node+1,low,high,(left+right+1)/2, high);
}


void solve(){
    int n; cin >> n;
    int v = n;
    n--;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    n++;
    

    fo(i,v) cin >> tree[n+i];
    for(int i = v; i < n; ++i) tree[n+i] = MAX_A;

    for(int i = n-1; i >= 1; --i) tree[i] = tree[2*i] & tree[2*i+1];

    int q;
    cin >> q;
    while(q--){
        int k,l;
        cin >> k >> l;
        l--;
        if (tree[n+l] < k) {cout << -1 << sp; continue;}

        int lef,rig;
        lef = l; rig = v;
        while(rig - lef > 1){
            int mid = (lef+rig)/2;
            if (range(1, l, mid, 0, n-1) < k) {
                rig = mid;
            } else {
                lef = mid;
            }
        }
        cout << lef << sp;
        
    }
    cout << nl;
    

    
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