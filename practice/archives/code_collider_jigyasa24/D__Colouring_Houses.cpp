#include <bits/stdc++.h>
//#include<ext/pb_ds/assoc_container.hpp>
//#include<ext/pb_ds/tree_policy.hpp>
#define vi vector<int>
#define vll vector<long long>
#define ll long long
#define int long long
#define pll pair<long long, long long>
#define all(x) (x).begin(),(x).end()
#define mll map<long long, long long>
#define pb push_back
#define F first
#define S second
using namespace std;
//using namespace __gnu_pbds;
//typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> pbds;
//typedef tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update> pbdsl;
// *a.find_by_order(x)-->gives xth element considering 0 indexing
// a.order_of_key(x)-->gives number of elements strictly smaller than x
const int N = 2e5 + 5;
const int INF = 1e9;
const int M = 998244353;
const int MOD = 1e9 + 7;


void give(vll &x){
    for(auto ele:x){
        cout<<ele<<' ';
    }
    cout<<'\n';
}

ll mul(int a, int b){
    return ((a%M)*(b%M))%M;
}

ll add(int a, int b){
    return ((a%M)+(b%M))%M;
}

ll sub(int a, int b){
    return ((a%M)-(b%M)+M)%M;
}

ll mypow(int a, int b){
    if(b==0) return 1;
    int ans = mypow(a,b/2);
    ans = ans;
    if(b&1){
        return (ans*ans*(a));
    }else{
        return (ans*ans);
    }
}

ll my_pow_iter(ll a, ll b){
    ll res = 1;
    while(b>0){
        if(b&1){
            res = ((res%M)*(a%M))%M;
        }
        a = ((a%M)*(a%M))%M;
        b >>= 1;
    }
    return res;
}


long long modInverse(long long n) {
    return my_pow_iter(n, M - 2);
}
 

long long nCr(long long n, long long r) {
    if(n<r)return 0;
    if (r == 0) {
        return 1;
    }
 
    long long num = 1;
    for (long long i = n; i >= n - r + 1; i--) {
        num = mul(num, i);
    }
 
    // Calculate denominator: r!
    long long den = 1;
    for (long long i = 1; i <= r; i++) {
        den = mul(den, i);
    }
 
    // Calculate modular inverse of denominator
    long long denInverse = modInverse(den);
 
    // Calculate final result: (n * (n-1) * ... * (n-r+1)) / r!
    return mul(num, denInverse);
}

ll divide(int a, int b){
    int x = modInverse(b);
    return mul(a,x);
}

/* array ke elements ka product nhi krna h
 * dp me first value se second value calculate krne se pehle first value poori calculate 
   krna i mean first value ab kabhi bhi update nhi honi chahiye
 * positions vale questions me modulo jitna ho ske avoid kro(icpc)
 * i and n/i ka dyaan rkhna root(n) tak chalate vakt
 * stuff you should look for
 * int overflow, array bounds n and m
 * special cases (n=1?)
 * do smth instead of nothing and stay organized
 * WRITE STUFF DOWN
 * DON'T GET STUCK ON ONE APPROACH
 */

const int bda = 1e15;

int arr[102][102];
int dp[102][102][102];
int k,m;

int solve2(int idx, int prev, int segs, vll &v){
    // cout<<idx<<" "<<prev<<" "<<segs<<endl;
    // cout<<dp[idx][prev][segs]<<endl;
    int n = v.size();
    if(idx==n && segs==k){
        return 0;
    }
    if(idx==n) return bda;
    if(dp[idx][prev][segs]!=-1){
        return dp[idx][prev][segs];
    }
    
    if(v[idx]!=0){
        // cout<<"here";
        if(v[idx]==prev){
            return dp[idx][prev][segs] = solve2(idx+1,v[idx],segs,v);
        }else{
            return dp[idx][prev][segs] = solve2(idx+1,v[idx],segs+1,v);
        }
    }else{
        int ans = bda;
        for(int i=1; i<=m; i++){
            if(i==prev) ans = min(ans,arr[idx+1][i]+solve2(idx+1,i,segs,v));
            else ans = min(ans,arr[idx+1][i]+solve2(idx+1,i,segs+1,v));
        }
        return dp[idx][prev][segs] = ans;
    }
}

void solve(){
    int n;
    cin>>n>>m>>k;
    // memset(dp,-1,sizeof(dp));
    vll v(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            cin>>arr[i][j];
        }
    }
    // cout<<dp[1][1][1]<<endl;
    for(int i=0; i<=100; i++){
        for(int j=0; j<=100; j++){
            for(int k=0; k<=100; k++){
                dp[i][j][k] = -1;
            }
        }
    }
    int ans = solve2(0,0,0,v);
    if(ans>=1e12){
        ans = -1;
    }
    cout<<ans<<'\n';
}
 
 
signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    
    int t=1;
    //  cin>>t;
    
    while(t--){
       solve();
    }
    return 0;
}
