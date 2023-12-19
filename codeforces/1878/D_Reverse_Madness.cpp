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

int l[N_MAX];
int r[N_MAX];
char s[N_MAX];

void solve(){
    int n,k; cin >> n >> k;
    fo(i,n) cin >> s[i+1];

    fo(i,k) {cin >> l[i];}
    fo(i,k) cin >> r[i];
    vector<set<int>> Xs(k);

    int q; cin >> q;
    fo(m,q){
        int x;
        cin >> x;
        // int l_i = l[upper_bound(l,l+k,x) - l];
        int i = lower_bound(r,r+k,x) - r;
        int l_i,r_i;
        l_i = l[i]; r_i = r[i];
        x = min(x,l_i + r_i - x);
        if (l_i + r_i == 2*x) continue;
        if (Xs[i].count(x)) {Xs[i].erase(x); } 
        else {Xs[i].insert(x);}
    }

    for (int g = 0; g < k; g++){
        bool mov_forward = true;

        int i = l[g];
        while (i <= r[g]){
            if (Xs[g].count(i) || Xs[g].count(l[g] + r[g] - i + 1)) { mov_forward = !mov_forward; }
            if (mov_forward){
                cout << s[i];
            } else {
                cout << s[l[g] + r[g] - i];
            }
            i++;
        }
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