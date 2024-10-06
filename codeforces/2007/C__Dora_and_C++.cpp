#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

void solve() {
    int n, a, b;
    cin >> n >> a >> b;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    int g = gcd(a, b);

    // cerr << "----" << g << "----" << endl;
    // for (int x : A) {
    //     cerr << x % g << " ";
    // }
    // cerr << endl;

    if (g == 1 || n == 1) {
        cout << 0 << endl;
        return;
    }

    // cerr << g << " ~| ";
    // for (int x : sorted(set(A.begin(), A.end(), [](int a, int b) { return a % g < b % g; }))) {
    //     cerr << x << " ";
    // }
    // cerr << endl;

    vector<int> s;
    for (int x : A) {
        s.push_back(x % g);
    }
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()), s.end());
    if (s.size() == 1) {
        cout << 0 << endl;
        return;
    }
    int ans = s.back() - s[0];
    int mn = s.back() - g;
    s.pop_back();
    while (!s.empty()) {
        ans = min(ans, s.back() - mn);
        mn = s.back() - g;
        s.pop_back();
    }
    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}

