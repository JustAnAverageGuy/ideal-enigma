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

int A[10][100000+5];

int main()
{
    fast();
    int n,m,k;
    cin >> n >> m >> k;
    fo(i,n){
        fo(j,m){
            cin >> A[i][j];
        }
    }
    ll wallet = 0;
    
    for (int p = 0; p < m - k + 1 ; p++ ){
        ll max_money = 0;
        int loc_row = -1;
        int loc_col = -1;
        for (int kol = p; kol < p + k ; kol++ ){
            for(int row = 0; row < n; row++){
                if (max_money < A[row][kol]) {
                    max_money = A[row][kol];
                    loc_row = row;
                    loc_col = kol;
                }

            }
        }
        wallet += max_money;
        A[loc_row][loc_col] = 0;
        // print(loc_row << ' ' << loc_col)
    }
    print(wallet);

}