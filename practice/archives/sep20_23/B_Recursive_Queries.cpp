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

int prod(int n){
    int t = n;
    while ( t > 9){
        int pro = 1;
        while (t){
            pro *= (t%10) + (t%10 == 0);
            t /= 10;
        }
        t = pro;
    }
    return t;
}

int main()
{
    fast();
    vector<int> A[10];
    for(int i = 1; i <= 1000000; i++){
        A[prod(i)].emplace_back(i);
    }
    // print("Done");
    fo(i,10){sort(A[i].begin(),A[i].end());}
    
    int t;
    cin >> t;
    while(t--){
        int l,r,k;
        cin >> l >> r >> k;
        int a = lower_bound(A[k].begin(),A[k].end(),l) - A[k].begin();
        int b = upper_bound(A[k].begin(),A[k].end(),r) - A[k].begin();
        print(b -a);

    }
    
}