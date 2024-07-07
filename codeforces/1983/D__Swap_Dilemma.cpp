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
ll ll_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k != 0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/


ll merge(vector<ll>& arr, ll low, ll mid, ll high) {
    vector<ll> t;
    ll cnt = 0;
    ll l = low;
    ll r = mid + 1;
    while (l <= mid && r <= high) {
        if (arr[l] <= arr[r]) {
            t.push_back(arr[l]);
            l++;
        } else {
            t.push_back(arr[r]);
            r++;
            cnt += mid - l + 1;
        }
    }
    for (ll i = l; i <= mid; i++) {
        t.push_back(arr[i]);
    }
    for (ll j = r; j <= high; j++) {
        t.push_back(arr[j]);
    }
    for (ll i = low; i <= high; i++) {
        arr[i] = t[i - low];
    }
    return cnt;
}

ll mergeSort(vector<ll>& arr, ll low, ll high) {
    if (low >= high) return 0;

    ll cnt = 0;
    ll mid = low + (high - low) / 2;
    cnt += mergeSort(arr, low, mid);
    cnt += mergeSort(arr, mid + 1, high);
    cnt += merge(arr, low, mid, high);
    return cnt;
}

ll getInversions(vector<ll>& arr, ll n) {
    return mergeSort(arr, 0, n - 1);
}

bool solve() {
    ll n;
    cin >> n;
    vector<ll> A(n);
    vector<ll> B(n);
    for (ll i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (ll i = 0; i < n; i++) {
        cin >> B[i];
    }

    ll inva = mergeSort(A, 0, n - 1);
    ll invb = mergeSort(B, 0, n - 1);

    if (A != B || (inva - invb) % 2) return false;
    return true;
}

int main() {
    ll t;
    fast();
    cin >> t;
    for (ll i = 0; i < t; i++) {
        cout << (solve() ? "YES" : "NO") << endl;
    }
    return 0;
}

