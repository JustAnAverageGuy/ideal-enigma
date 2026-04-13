#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    map<pair<int,int>, int> reference;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        reference[{a, b}] = (b - a + 3) / 2;
    }

    int qcount;
    cin >> qcount;
    vector<int> queries(qcount);
    for (int i = 0; i < qcount; i++) {
        cin >> queries[i];
        queries[i]--;
    }

    int l = -1;
    int r = qcount + 1;

    while (r - l > 1) {
        int mid = l + (r-l)/2;
        map<pair<int,int>, int> segs = reference;
        bool check = false;

        for (auto &seg : segs) {
            auto range = seg.first;
            for (int i = 0; i < mid; i++) {
                int q = queries[i];
                if (q < range.first || q > range.second) continue;
                seg.second -= 1;
                if (seg.second == 0) {
                    check = true;
                    break;
                }
            }
            if (check) break;
        }

        if (check)
            r = mid;
        else
            l = mid;
    }

    if (r != qcount + 1)
        cout << r << "\n";
    else
        cout << -1 << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}


