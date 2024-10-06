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
    
    if(k % 2 == 0){
        cout << "Yes" << '\n';
        return;
    }

    int x = n / k, y = n / k + 1;
    int cx = k - n % k, cy = n % k;

    auto ok = [&](int z){
        return z >= 0 && z <= cy;
    };
    for (int i = 0; i <= cx; ++i){
        if(i % 2 != cx % 2) continue;
        int j1 = ((i * x) - (n % 2)) / y;
        int j2 = ((i * x) + (n % 2)) / y;
        if(j1 % 2 == cy % 2 && ok(j1) && i * x - j1 * y == n % 2){
            cout << "Yes" << '\n';
            return;
        }
        if(j2 % 2 == cy % 2 && ok(j2) && j2 * y - i * x == n % 2){
            cout << "Yes" << '\n';
            return;
        }
        if(!ok(j1) && !ok(j2)) break;
    }
    cout << "No" << '\n';
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

    return 0;}
