#include <iostream>
#include <cmath>
#include <vector>

using namespace std;
int isqrtt[1'00'000+1];

int isqrt(long long n){
    if (n > 100000) return  100005;
    return isqrtt[n];
}

int main() {
    const int MAX_DIS = 100001;
    vector<int> ans(MAX_DIS, 4);
    ans[0] = 1;

    for(int k = 0; k < 1000; k++){
        int a = k*k;
        if (a > 100000) break;
        int b = (k+1)*(k+1);
        b = ((b < 100000)?b:100000)+1;

        for(int x = a; x < b; x++) isqrtt[x] = k;
    }

    for (int x = 1; x < MAX_DIS; ++x) {
        for (int y = x + 1; y < MAX_DIS; ++y) {
            int d = isqrt(x * x + y * y);
            if (d > MAX_DIS) break;
            ans[d] += 8;
        }
    }

    for (int k = 0; k < MAX_DIS; ++k) {
        int d = isqrt(2 * k * k);
        if (d > MAX_DIS) break;
        ans[d] += 4;
    }

    for (int i = 0; i < MAX_DIS; ++i) {
        cout << ans[i] << " ";
    }

    return 0;
}

