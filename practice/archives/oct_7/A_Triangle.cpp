#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <ctime>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> pt;
#define ft first
#define sc second

int a[6];

bool read() {
	forn(i, 6)
		if (!(cin >> a[i]))
			return false;
	return true;
}

#define sqr(x) ((x)*(x))
int dist2(int x1, int y1, int x2, int y2) {
	return sqr(x1 - x2) + sqr(y1 - y2);
}

bool check() {
	int c[3], csz = 0;

	forn(i, 3)
		forn(j, i)
			c[csz++] = dist2(a[i * 2], a[i * 2 + 1], a[j * 2], a[j * 2 + 1]);

	sort(c, c + 3);
	if (c[0] == 0)
		return false;
	return c[0] + c[1] == c[2];
}

void solve() {
	int res = 0;

	if (check()) {
		puts("RIGHT");
		return;
	}

	for (int d = -1; d <= +1; ++d) {
		forn(i, 6) {
			a[i] -= d;
			if (check()) {
				puts("ALMOST");
                for(int i = 0; i < 6 ; i++) cout << a[i] << ' ';
                cout << '\n'; 
				return;
			}
			a[i] += d;
		}
	}

	puts("NEITHER");
}

int main() {


	while (read())
		solve();
	
	return 0;
}
