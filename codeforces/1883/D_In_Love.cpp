#define         MOD             ((int)(1e9 + 7))
#define         fo(i, n)        for(int i=0; i < n; ++i)
#define         print(k)        cout << k << '\n';
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

int main()
{
    fast();
    int q; cin >> q;

    set<int> ls;
    set<int> rs;
    map<int,int> cntl;
    map<int,int> cntr;
    while (q--){
        char s;
        int l,r;
        cin >> s >> l >> r;
        if (s == '+'){
            ls.insert(l);
            rs.insert(r);
            cntl[l]++;
            cntr[r]++;

        } else {
            cntl[l]--;
            cntr[r]--;

            if (cntl[l] == 0) ls.erase(l);
            if (cntr[r] == 0) rs.erase(r);
        }

        if (ls.size() == 0) {print("NO");continue;}
        auto it1 = rs.begin();
        auto it2 = ls.rbegin();
        
        // cout << "LS: ";
        // for(auto i: ls) cout << i << sp;
        // cout << nl;
        // cout << "RS: ";
        // for(auto i: rs) cout << i << sp;
        // cout << nl ;
        // // --it2;
        // cout << "min_r: " << *it1 << nl;
        // cout << "max_l? " << *it2 << nl<<nl ;
        
        cout << (((*it1 <  *it2 ))?"YES":"NO") << nl;
    }

}