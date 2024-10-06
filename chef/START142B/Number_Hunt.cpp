#define MOD ((int)(1e9 + 7))
#define fo(i, n) for (int i = 0; i < n; ++i)
#define print(k) cout << k << '\n';
#define elif else if
#define fast()                                                                 \
  ios_base::sync_with_stdio(false);                                            \
  cin.tie(NULL)
#define pb(x) emplace_back(x)
#define N_MAX (200000 + 5)
#define A_MAX (1000000000 + 7)
#define nl ('\n')
#define sp (' ')
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/*
ll powmod(ll a, ll b, ll mod = MOD, bool isprime = true){a %= mod;ll res=1;if
(isprime)b %= mod-1;while (b > 0){if (b & 1)res = (res * a) % mod;a=(a * a)%
mod;b >>= 1;}return res;} ll int_sqrt(ll x){ll ans{0};for(ll k = 1LL << 30; k !=
0; k /= 2){if ((ans + k) * (ans + k) <= x) {ans += k;}}return ans;}
*/

/********************************************************************CODE*********************************************************************/

/* This function calculates (ab)%c */
int modulo(int a, int b, int c) {
  long long
      x = 1,
      y = a; // long long is taken to avoid overflow of intermediate results
  while (b > 0) {
    if (b % 2 == 1) {
      x = (x * y) % c;
    }
    y = (y * y) % c; // squaring the base
    b /= 2;
  }
  return x % c;
}
/* this function calculates (a*b)%c taking into account that a*b might overflow
 */
long long mulmod(long long a, long long b, long long c) {
  long long x = 0, y = a % c;
  while (b > 0) {
    if (b % 2 == 1) {
      x = (x + y) % c;
    }
    y = (y * 2) % c;
    b /= 2;
  }
  return x % c;
}

/* Miller-Rabin primality test, iteration signifies the accuracy of the test */
bool Miller(long long p, int iteration) {
  if (p < 2) {
    return false;
  }
  if (p != 2 && p % 2 == 0) {
    return false;
  }
  long long s = p - 1;
  while (s % 2 == 0) {
    s /= 2;
  }
  for (int i = 0; i < iteration; i++) {
    long long a = rand() % (p - 1) + 1, temp = s;
    long long mod = modulo(a, temp, p);
    while (temp != p - 1 && mod != 1 && mod != p - 1) {
      mod = mulmod(mod, mod, p);
      temp *= 2;
    }
    if (mod != p - 1 && temp % 2 == 0) {
      return false;
    }
  }
  return true;
}

int main(int argc, char *argv[]) {
  fast();
  int t;
  cin >> t;
  ll p1;
  ll p2;
  while (t--) {

    ll input;
    cin >> input;
        if(input < 3) {cout << 6 << nl; continue;}
    ll i = 0;

    if (input % 2 == 0)
      i = input + 1;
    else
      i = input;

    for (; i < 2 * input; i += 2)
      if (Miller( i, 20)) break;
    p1 = i;
    i += 2;
    for (; i < 2 * p1; i += 2)
      if (Miller( i, 20)) break;
    p2 = i;
    cout << p1 * p2 << nl;
  }
  return 0;
}
