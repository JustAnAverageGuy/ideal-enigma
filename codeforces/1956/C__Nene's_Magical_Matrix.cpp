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

int A[500][500];
int n;

void debug(){

    for(int i = 0; i < n; i++){ for(int j = 0; j < n; j++){ cerr << A[i][j] << sp;} cerr << nl; }
    cerr << "=====" << nl;
}

void fill(int n){

    for(int i = n-1; i >= 0; i--){
        for(int j = 0; j < n; j++){
            A[i][j] = j+1;
            A[j][i] = j+1;
        }
        debug();
    }


}

void solve(){
    // cerr << "------\n";
    // int n; cin >> n;
    cin >> n;
    cout << (((n*n+n)*(4*n-1))/6) << sp << 2*n << nl; 

    for(int i = n; i > 0; i--){
        cout << 1 << sp <<  i << sp;
        for(int i = 1; i <= n; i++) cout <<i << sp;
        cout << nl;
        cout << 2 << sp <<  i << sp;
        for(int i = 1; i <= n; i++) cout <<i << sp;
        cout << nl;
    }

    // fill(n);

    // ll s = 0;
    // fo(i,n){
    //     fo(j,n){
    //         s += A[i][j];
    //     }
    // }
    //
    // debug();

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
