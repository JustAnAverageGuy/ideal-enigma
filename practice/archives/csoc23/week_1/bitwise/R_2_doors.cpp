// #define MOD 1e9 + 7
// #define fo(i, n) for (int(i) = 0; (i) < (n); ++(i))
// #define print(k) cout << (k) << '\n';
// #define fast()                        \
//     ios_base::sync_with_stdio(false); \
//     cin.tie(NULL)
// #define pb(x) push_back(x)
// #define nl '\n'
// #include <bits/stdc++.h>
// typedef long long ll;
// using namespace std;
// /*
// ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if (isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)% mod;b >>= 1;}return res;}
// ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
// */

// /********************************************************************CODE*********************************************************************/
// #define N 100005
// #define Q 200005
// int main()
// {
//     // #ifndef ONLINE_JUDGE
//     //     freopen("input.txt", "r", stdin);
//     //     freopen("output.txt", "w", stdout);
//     // #endif
//     fast();
//     int n, q;
//     cin >> n >> q;
//     vector<int> ORS(n, 0);
//     vector<tuple<int, int, int>> inps;
//     for (int qu = 0; qu < q; ++qu)
//     {
//         int i, j, OR;
//         cin >> i >> j >> OR;
//         --i;
//         --j;
//         ORS[i] |= OR;
//         ORS[j] |= OR;
//         if (i > j)
//         {
//             int t = i;
//             i = j;
//             j = t;
//             // i ^= j ^= i ^= j;
//         }
//         inps.pb(make_tuple(i, j, OR));
//     }
//     sort(inps.begin(), inps.end());
//     // int A[N] = {0};
//     vector<int> A(n, 0);
//     for (int b = 0; b < 31; b++)
//     {
//         for (auto q : inps)
//         {

//             int i, j, o;
//             tie(i, j, o) = q;
//             // cout<<i<<" "<<j<<" "<<o<<endl;
//             if (((o >> b) & 1) == 0)
//                 continue;
//             else if (((ORS[j] >> b) & 1) == 0)
//                 A[i] |= (1 << b);
//             else
//                 A[j] |= (1 << b);
//         }
//     }
//     fo(i, n) cout << A[i] << " ";
// }
#include <iostream>
#include <vector>

using namespace std;

inline bool get_bit(uint32_t &x, uint32_t &bt) { return (x >> bt) & 1; }
inline void make_one(uint32_t &x, uint32_t &bt) { x |= (1 << bt); }
inline void make_null(uint32_t &x, uint32_t &bt) { x &= (~(1 << bt)); }

inline bool solve_bit(vector<uint32_t> &ans,
                      vector<vector<pair<uint32_t, uint32_t>>> &g,
                      uint32_t &bt) {
    for (uint32_t i = 0; i < (uint32_t)ans.size(); ++i)
        for (auto &it : g[i])
            if (!get_bit(it.second, bt))
                make_null(ans[i], bt);
            else if (!get_bit(ans[i], bt) && !get_bit(ans[it.first], bt))
                return false;
    for (uint32_t i = 0; i < (uint32_t)ans.size(); ++i)
        if (get_bit(ans[i], bt)) {
            make_null(ans[i], bt);
            for (auto &it : g[i])
                if (!get_bit(ans[it.first], bt) && get_bit(it.second, bt)) {
                    make_one(ans[i], bt);
                    break;
                }
        }

    return true;
}

inline void solve() {
    uint32_t n, m;
    cin >> n >> m;
    vector<vector<pair<uint32_t, uint32_t>>> g(n);
    while (m--) {
        uint32_t a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        g[a].emplace_back(b, c);
        g[b].emplace_back(a, c);
        // if (a > b)
        //     swap(a, b);
    }
    const int pt = 31;
    vector<uint32_t> ans(n, ~(1 << pt));
    for (uint32_t i = 0; i < pt; ++i)
        if (!solve_bit(ans, g, i)) {
            cout << "-1\n";
            return;
        }
    for (auto &it : ans)
        cout << it << " ";
    cout << "\n";
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}