#pragma GCC optimize("O3","unroll-loops")
#pragma GCC target("avx2")
#define         MOD             1e9 + 7
#define         fo(i, n)        for(int (i)=0; (i) < (n); ++(i))
#define         print(k)        cout << (k) << '\n';
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/
#define N 20010


vector<tuple<int, int, int>> children[N + 15];
vector<int> R(N);
void ans(int n, int c, ll a, vector<ll> &B)
{
    for (auto i : children[c])
    {
        a += get<1>(i);
        if (B.size() == 0)
            B.push_back(get<2>(i));
        else
            B.push_back(B[B.size() - 1] + get<2>(i));
        R[get<0>(i)] = (upper_bound(B.begin(), B.end(), a) - B.begin() );
        ans(n, get<0>(i), a, B);
        B.pop_back();
        a -= get<1>(i);
    }
    if (c == 1)
    {
        for (int i = 2; i <= n; ++i)
        {
            cout << R[i] << " ";
        }
        cout << "\n";
    }
}

int main()
{
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif
    fast();
    int _;
    cin >> _;
    while (_--)
    {
        int n;
        cin >> n;
        for (int i = 0; i < n+1; i++)
        {
            children[i].clear();
        }
        for (int i = 2; i < n + 1; i++)
        {
            int p, a, b;
            cin >> p >> a >> b;
            children[p].push_back(make_tuple(i, a, b));
        }
        vector<ll> B = {};
        ans(n, 1, 0, B);
    }
}
