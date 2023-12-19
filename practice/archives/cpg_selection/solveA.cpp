#define MOD ((int)(1e9 + 7))
#define fo(i, n) for (int i = 0; i < n; ++i)
#define print(k) cout << k << '\n';
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
#define pb(x) push_back(x)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/


#define repi(i,s,e) for(ll i=s;i<e;i++)
#define repd(i,e,s) for(ll i=e;i>=s;i--)
#define INF numeric_limits<float>::infinity();

bool vpsort(const pair<ll, ll>& a, const pair<ll, ll>& b) {
    if (a.first == b.first) {
        return a.second < b.second;
    }
    return a.first < b.first;
}

ll mul(ll a, ll b)
{ 
    return 1LL * a * b % MOD;
}
ll modPow(ll b, ll p)
{
    if (p == 0)
        return 1;

    ll x = modPow(b, p / 2);

    return p % 2 == 0 ? mul(x, x) : mul(b, mul(x, x));
}


void solve()
{
    ll n;cin>>n;
    vector<ll> v(n);
    ll o=0;
    fo(i,n)
    {
        cin>>v[i];
        if(v[i]==1)
            o++;
    }
    sort(v.begin(),v.end());
    ll no=o;
    ll prod=1;
    for(int i = o+1; i < n; i++)
    {
        prod*=v[i];
        prod%=MOD;
    }
    ll ans=-INF;
    // cout<<o<<nl;
    if(o==1)
    {
        ans=prod*(v[o]+1);
        print(ans);
    }
    else
    {
        for(int i = 1; i < o+1; i++)
        {
            ll total=o/i;
            ll sum=i;
            if(o<n)
            {
                ll tmp=1;
                ll left=o%i;
                if(sum<v[o])
                {
                    if(total>0)
                        tmp=modPow(sum,total-1);
                    else
                        tmp=1;
                    tmp%=MOD;
                    tmp*=sum+left;
                    tmp%=MOD;
                    tmp*=v[o];
                    tmp%=MOD;
                }
                else
                {
                    tmp=modPow(sum,total);
                    tmp%=MOD;
                    tmp*=v[o]+left;
                    tmp%=MOD;
                }
                tmp*=prod;
                tmp%=MOD;
                ans=max(ans,tmp);
            }
            else
            {
                ll tmp=1;
                ll left=o%i;
                if(total>0)
                    tmp=modPow(sum,total-1);
                tmp%=MOD;
                tmp*=sum+left;
                tmp%=MOD;
                ans=max(ans,tmp);
            }
        }
        if(o==0)
        {
            ans=prod*v[0];
            ans%=MOD;
        }
        print(ans);
    }
}

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    ll t;
    cin>>t;
    while(t--)
        solve();

    return 0;
}   