#define         MOD             1e9 + 7
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

bool solve(){
    int n;
    cin >> n;
    vector<int> A(n,0);
    fo(i,n) {cin >> A[i];}
    if (A[0] != n) return false;
    for(int i = 1; i <= n; i++){
        int expected = A[i-1] - 1;
        if( !( ( !(expected + 1 < n) || A[expected+1] < i) && A[expected] >= i)) return false;

    }
    return true;
}

int main()
{

    fast();
    int t;
    cin >> t;
    while(t--){
        print((solve()?"YES":"NO"));
    }
        

}