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

int solve(){
    int n; cin >> n;
    // cout << "Got n= " << n << nl;
    if (n == 1) return 1;
    if (n == 2) return 0;
    if (n%2 == 1) return 0;
    if ( (n & (n-1)) == 0) return 1;
    if ( n%4==0) return 0;
    
    // now n is of the form 2 * (2k+1), so 
    // player_1 will remove all but one odd prime factor if possible
    // forcing player_2 to remove that odd factor (since subtracting
    // 1 sends it into odd state, and player_1 wins) 
    // and now player 1 gets 2 and wins

    // so if the number has exactly 1 odd factor, player_1 loses, otherwise wins
    // hence the number should be prime
    // so the number should be 2*p for some p for player_2 to win

    int f = n/2;
    int p = 3;
    if (f==p) return 1;
    while(p*p <= f){
        if (f%p == 0) return 0;
        p += 2;
    }
    return 1;
    
}

int main()
{
    fast();
    int t;
    cin >> t;
    while(t--){
        print(solve()?"FastestFinger":"Ashishgup");
        // print(solve());
    }
}