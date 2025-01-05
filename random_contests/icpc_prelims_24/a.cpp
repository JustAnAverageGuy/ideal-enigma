#include <bits/stdc++.h>
using namespace std;

#define int long long
#define ld long double

constexpr int INF = 2e18;
constexpr int MOD = 1e9 + 7;

#define all(x) begin(x), end(x)
#define Sort(x) sort(all(x))
#define rev_sort(x) sort(all(x), greater<int>())

void solve()
{
    int n, k;
    cin >> n >> k;
    
    vector<int> c(n);
    for(auto& i : c) cin >> i;

    rev_sort(c);
    
    vector<int> add(n,0), rem(n,0);
    for (int i = n - 1; i >= 0; --i){
        add[i] += c[i];
        if(i + 1 < n) add[i] += add[i + 1];
        int j = i + k + 1;
        rem[i] += c[i];
        if(j < n) rem[i] += rem[j];
    }

    for (int i = n - 1; i >= 0; --i){
        int cur = add[i];
        int j = i + k;
        if(j < n) cur -= rem[j];
        cout << cur << ' ';
    }
    cout << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(0), cin.tie(0);
    cout << setprecision(12) << fixed;
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    int tests = 1;
    cin >> tests;
    for (int tt = 1; tt <= tests; ++tt){
        // cout << "Test " << tt << " :\n";
        solve();
    }

    return 0;
}
