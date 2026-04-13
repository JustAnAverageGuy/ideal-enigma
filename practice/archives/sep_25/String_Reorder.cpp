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
    string s;

    // cin >> s;
    s = "HATTIVATTI";

    int n = s.length();

    int cnt[26] = {};
    
    string ans = "";

    char last = '\n';

    for(char const&c: s) cnt[c-'A'] += 1;

    for(auto const&  v: cnt){
        if (n < 2*v -1){
            cout << -1 << nl;
            return 0;
        }
    }
    
    for(int remaining = n; n >= 1; --remaining){

        bool unbroken = true;
        int otherwise = 25;
        for(int c = 0; c < 26; c++){
            // if(c + 'A' == last) continue;
            if(remaining == 2*cnt[c]-1){
                ans.push_back(c+'A');
                last = c+'A';
                // ans += (c+'A');
                cnt[c] -= 1;
                unbroken = false;
                break;
            }
            if(otherwise > c && last-'A' != c && cnt[c]) otherwise = c;
        }

        #define DEBUG 0
        #if DEBUG
        for(int i = 0; i < 26; i++)if(cnt[i]){ cout << static_cast<char>(i + 'A') << " " << cnt[i] << nl;}
        cout << "-----------" << ans ;
        if (unbroken) cout << static_cast<char>(otherwise + 'A');
        cout << nl;
        #endif // DEBUG

        if(!unbroken) continue;
        ans.push_back(otherwise + 'A');
        cnt[otherwise] -= 1;
        last = otherwise+'A';


    }

    cout << ans;


}

