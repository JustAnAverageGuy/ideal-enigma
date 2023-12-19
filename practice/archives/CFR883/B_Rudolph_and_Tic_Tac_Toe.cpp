#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int (i)=0; (i) < (n); ++(i))
#define         print(k)        cout << (k) << '\n';
#define         fast()          ios_base::sync_with_stdio(false); cin.tie(NULL)
#define         pb(x)           push_back(x)
#define         nl              '\n'
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

void solve(){
    string A[3];
    fo(i,3) cin >> A[i];
    // fo(i,9) cout << A[i/3][i%3];
    fo(i,3){
        if(A[i][0]!= '.' && A[i][0] == A[i][1] && A[i][1] == A[i][2]){ print(A[i][0]); return;}
        if(A[0][i]!= '.' && A[0][i] == A[1][i] && A[1][i] == A[2][i]){ print(A[0][i]); return;}


    };
        if(A[1][1]!= '.' && A[0][0] == A[1][1] && A[1][1] == A[2][2]){ print(A[1][1]); return;}
        if(A[1][1]!= '.' && A[0][2] == A[1][1] && A[1][1] == A[2][0]){ print(A[1][1]); return;}
    print("DRAW");

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