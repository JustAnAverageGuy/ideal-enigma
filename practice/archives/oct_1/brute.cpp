// # from math import gcd
// # def brute(n,A):
// #     max_ans = 0
// #     maxes = []
// #     for i in range(1,(1<<(n))):
// #         s = 0
// #         g = None
// #         for k in range(n):
// #             if (i >> k)&1:
// #                 s += A[k]
// #                 if g is not None:
// #                     g = gcd(g, A[k])
// #                 else:
// #                     g = A[k]
// #         ans = g*s
// #         if ans > max_ans:
// #             max_ans = ans
// #             maxes = [f'{i:0b}'.zfill(n)[::-1]]
// #         elif ans == max_ans: maxes.append(f'{i:0b}'.zfill(n)[::-1])
// #     return max_ans, maxes
// # n = int(input())
// # A = list(map(int,input().strip().split()))
// # print(brute(n,A)[0])

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int n;
    cin>>n;
    int ar[n];
    for(int i=0;i<n;i++)    cin>>ar[i];
    
    long cnt[10005] = {0};
    for(int i=0;i<n;i++){
        
        for(int j=1;j<=sqrt(ar[i]);j++){
            
            if(ar[i]%j==0){
                
                if(j*j==ar[i])  cnt[j]+=ar[i];
                else{
                    cnt[j]+=ar[i];
                    cnt[(ar[i]/j)]+=ar[i];
                }
            }
        }
    }
    
    long ans = 0;
    for(int i=1;i<=10000;i++)   ans = max(ans, i*cnt[i]);
    cout<<ans;
    
    return 0;
}
