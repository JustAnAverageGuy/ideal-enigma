#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
// #include <bits/stdc++.h>

using namespace std;
int A[1000000];
int B[1000000];
int C[1000000];

int main() {
    // Fast input
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Reading input
    int n, m;
    cin >> n >> m;
    
    
    for(int i = 0; i < n; ++i) {
        cin >> A[i];
    }
    for(int i = 0; i < n; ++i) {
        cin >> B[i];
    }
    for(int i = 0; i < m; ++i) {
        cin >> C[i];
    }

    vector<pair<int, int>> s(n);
    for(int i = 0; i < n; ++i) {
        s[i] = {A[i], B[i]};
    }

    sort(s.begin(), s.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if ((a.first - a.second) != (b.first - b.second)) {
            return (a.first - a.second) < (b.first - b.second);
        }
        return a.first < b.first;
    });

    priority_queue<int> pq(C, C+m);

    long long xp = 0;

    for(const auto& i : s) {
        int gatekeep = i.first, los = i.first - i.second;
        while (!pq.empty()) {
            int topmost = pq.top();
            if (topmost >= gatekeep) {
                long long lamda = ((topmost - gatekeep) / los) + 1;
                xp += 2 * lamda;
                topmost -= lamda * los;
                pq.pop();
                pq.push(topmost);
            } else {
                break;
            }
        }
    }

    cout << xp << endl;

    return 0;
}

