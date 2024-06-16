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

bitset<5000> s;
bitset<5000> x;
int n;


bool check(int k){
    // return true if it is possible to have the blocks of k

    if(k == 1) return  true;

    x[0] = s[0];
    
    if (k-1 <= n-k){


        for (int i = k-1; i > 0; i--){
            x[i] =  s[i] ^ s[i-1]; 
        }
        bool txor = s[k-1];

        for(int i = k; i <= n-k; i++){
            txor ^= x[i - k];
            x[i] = txor ^ s[i];
            txor = s[i];
        }

        // cerr <<"k: " << k << " x: ";
        // for (int i = 0; i <= n-k; i++) cerr << x[i];
        // cerr << nl;


        for(int i = n-k+1; i < n; i++){
            txor ^= x[i - k];
            if (txor != s[i]) return  false;
        }
    } else {
        for (int i = n-k; i > 0; i--){
            x[i] =  s[i] ^ s[i-1]; 
        }

        // cerr <<"k: " << k << " x: ";
        // for (int i = 0; i <= n-k; i++) cerr << x[i];
        // cerr << nl;

        bool txor = s[n-k];
        for (int i = n-k+1; i <= k-1; i ++) {if (s[i] != txor) return false; }
        for(int i = k; i < n; i++){
            txor ^= x[i - k];
            if (txor != s[i]) return  false;
        }

    }
    return true;
    
    


}

void solve(){
    cin >> n;
    cin >> s;

    s.flip();

    // reverse the bitset
    
    for (int i = 0 ; i < n/ 2; i++){
        bool t = s[n-1-i];
        s[n-1-i] = s[i];
        s[i] = t;

    }

    // cerr << "-----------" << nl;

    // fo(i, n){
        // cerr << s[i];
    // }
    cerr << nl;
    
    
    // int r = n+1;
    // int l = 0;
    // int m;
    //
    // while(r-l > 1){
    //     m = l + (r-l)/2;
    //     if (!check(m)) r = m;
    //     else l = m;
    // }
    //
    // cout << l << nl;

    for(int k = n; k > 0; k--){
        if(check(k)) {
            cout << k <<nl; return;
        }
    }
    return;
    
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
