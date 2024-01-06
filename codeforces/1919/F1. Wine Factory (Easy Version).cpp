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

const int N = 1 << 19;
int n,k;
struct P {ll l, r, ts, bs;}; // left, right, totalsum, bestsum
P p[2*N];

ll maxf(ll a,ll b,ll c) {return max(a,max(b,c));}

P combine(P &cl,P &cr) {
  P node;
  node.ts = cl.ts + cr.ts;
  node.l = maxf(cl.l, cl.ts, cl.ts + cr.l);
  node.r = maxf(cr.r, cr.ts, cr.ts + cl.r);
  node.bs = maxf(cl.bs, cr.bs, cl.r + cr.l);
  return node;
}

void change(int k, ll x) {
  k += N;
  p[k].l = p[k].r = p[k].ts = p[k].bs = x;
  for (k /= 2; k >= 1; k /= 2) {
    p[k] = combine(p[2*k], p[2*k+1]);
  }
}


int main()
{
    fast();
    // cerr << "Well hello there \n" <<endl;
    int n,q;
    cin >> n >> q;
    vector<ll> A(n);
    P nul = {0,0,0,0};
    fo(i,2*N){p[i] = nul;}   
    ll totsum = 0;
    fo(i,n){ll a; cin >> a; A[i] = a; totsum += a;}
    fo(i,n){ll a; cin >> a; A[i] -= a; change(i+1, A[i]);}
    fo(i,n-1) {ll t; cin >> t;}
    fo(i,q){
        ll pindex,a,b,c;
        cin >> pindex >> a >> b >> c;
        // cout << "GOT " << pindex << sp << a <<sp << b << sp << c << endl;
        change(pindex, a-b);
    // cerr << "Ahoy mates\n" << endl;
        totsum -= A[pindex - 1];
        totsum += a;
        cout << totsum - p[1].ts << nl;
    }
}
