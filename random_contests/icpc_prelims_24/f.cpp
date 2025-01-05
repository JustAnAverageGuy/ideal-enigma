#include<bits/stdc++.h>
#include<stdbool.h>
//#include<ext/pb_ds/assoc_container.hpp>
//#include<ext/pb_ds/tree_policy.hpp>
//using namespace __gnu_pbds;
using namespace std;
#define db(x) cout << #x << " = " << x << endl;
#define ll long long
#define pll pair<ll,ll>
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define ull unsigned long long
#define big 1000005
#define ed '\n'
#define mod 1000000007

//typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds; // find_by_order, order_of_key (SET)
//typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> pbds; // find_by_order, order_of_key (MULTISET)

ll gcd(ll a, ll b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
} 
ll lcm(ll a, ll b){
  return ((a*b)/gcd(a,b));
}

ll abso(ll x){
  if(x > 0){
    return x;
  }else{
    return (-1)*x;
  }
}

ll minm(ll a, ll b, ll c, ll d){
  return min(min(a,b),min(c,d));
}

ll maxm(ll a, ll b){
  if(a > b){
    return a;
  }else{
    return b;
  }
}

ll ceil2(ll a, ll b) {
    return (a + b - 1) / b;
}

// must check if both pairs are disjoint before using this template 
pair<ll,ll> inter(pair<ll,ll> a, pair<ll,ll> b){
  if(b.second >= a.first && a.first >= b.first && b.second <= a.second){
    return {a.first,b.second};
  }else if(b.first >= a.first && b.second <= a.second){
    return {b.first,b.second};
  }else if(a.first >= b.first && a.second <= b.second){
    return {a.first,a.second};
  }else{
    return {b.first,a.second};
  }
}

/*
 vector<long long>* div = new vector<long long>[big];
   //precomputation
   for(int i = 1 ; i < big ; i++){
    for(int j = i ; j < big ; j = j + i){
         div[j].push_back(i);
    }
   } */


vector<pair<ll,ll>> merge(vector<pair<ll,ll>>& v){ 
   sort(v.begin(),v.end());
   vector<pair<ll,ll>> ans;
   ans.push_back({v[0].first,v[0].second});
   for(ll i = 1; i < v.size() ; i++){
       if(v[i].second > (ans.back()).second && v[i].first <= (ans.back()).second){
        ll st = (ans.back()).first;
        ans.pop_back();
        ans.push_back({st,v[i].second});
       }else if(v[i].first > (ans.back()).second){
        ans.push_back({v[i].first,v[i].second});
       }
   }
   return ans;  
}

vector<ll> adj[200005];
bool is_visited[200005];
ll vis[200005];
// initialize it with inf in case of disjoint components or better in general
ll level[200005];

void dfs(ll current){
   is_visited[current] = true;
   for(auto child:adj[current]){
    if(is_visited[child]) continue;
        dfs(child);
   }
}

void bfs(ll source){
  queue<ll> q;
  q.push(source);
  vis[source] = 1;
  level[source] = 0;
  while(!q.empty()){
     ll curr = q.front();
     q.pop();
     for(auto child:adj[curr]){
        if(!vis[child]){
           q.push(child);
           vis[child] = 1;
           level[child] = level[curr] + 1;
        }
     }
  }
}

vector<pair<ll,ll>> g[200005];
vector<ll> dist(200005,1e18);
vector<ll> prevs(200005,0);
vector<ll> vs(200005,0);

void dijkstra(ll source){
  set<pair<ll,ll>> s;
  dist[source] = 0;
  s.insert({0,source});
  while(s.size()){
    pair<ll,ll> p = *(s.begin());
    s.erase(s.begin());
    if(vs[p.second]) continue;
    vs[p.second] = 1;
    for(auto child:g[p.second]){      
        ll new_dist = p.first+child.second;
        if(dist[child.first] > new_dist){
        prevs[child.first] = p.second;
        s.insert({new_dist,child.first});
        dist[child.first] = new_dist;
        }
    }
  }   
}

ll cnt_in_interval(vector<ll>& v,ll lower, ll upper){ // O(log(n))
  // number of numbers in range [lower,upper] in v(sorted already);
   ll s = v.size();
   ll e = -1;
   auto it1 = upper_bound(v.begin(),v.end(),upper);
   if(it1 != v.begin()) e = (it1-v.begin())-1;
   auto it2 = lower_bound(v.begin(),v.end(),lower);
   if(it2 != v.end()) s = (it2-v.begin());
   if(e>=s) return (e-s+1);
   else return 0;
}

vector<ll> seg_tree;

void build(vector<ll>& v, ll& n){
  while(__builtin_popcountll(v.size()) != 1) v.push_back(0);
  n = v.size();
  seg_tree.resize(2*n);
  for(ll i = 0; i < n ; i++) seg_tree[i+n]=v[i];
  for(ll i = n-1; i > 0; i--) seg_tree[i] = seg_tree[2*i]+seg_tree[(2*i)+1];
}

ll query(ll node, ll node_low, ll node_high, ll l, ll r){
     if(l > node_high || node_low > r) return 0;
     if(node_low >= l && node_high <= r) return seg_tree[node];
     ll middle = (node_low+node_high)/2;
     return query(2*node,node_low,middle,l,r)+query(2*node+1,middle+1,node_high,l,r);  
}

void update(ll ind, ll v, ll n){
   seg_tree[ind+n] = v;
   for(ll j = (ind+n)/2; j >= 1; j /= 2){
      seg_tree[j] = seg_tree[2*j]+seg_tree[(2*j)+1]; 
   }
}

ll ct(vector<ll>& v1 , vector<ll>& v2){
   ll n1 = v1.size();
   ll n2 = v2.size();
   set<ll> st;
   for(auto x:v1) st.insert(x);
   ll cnt = 0;
   for(auto y:v2){
     if(st.count(y)) cnt++;
   }
   return cnt;
}


void solve(){
  ll n;
  cin >> n;
  ll a[n];
  for(ll i = 0; i < n ; i++)
  cin >> a[i];

  vector<vector<ll>> v;
  for(ll i = 0 ; i < n ; i++){
    vector<ll> temp;
    for(ll j = 0 ; j < a[i]; j++){
       ll x;
        cin >> x;
        temp.push_back(x); 
    }
    v.push_back(temp);
  }
  if(n==2){
     cout << ct(v[0],v[1]) << ed;
     return;
  }
  ll dp[n][2][2];
  for(ll i = 0 ; i < n ; i++){
    for(ll j = 0 ; j < 2 ; j++){
      for(ll k = 0 ; k < 2 ; k++) dp[i][j][k]=1e18;
    }
  }
  ll inf = 1e18;
  dp[1][0][0]=inf; dp[1][0][1]=inf; dp[1][1][0]=ct(v[0],v[1]); dp[1][1][1]=0;
  dp[2][0][0]=ct(v[0],v[1])+ct(v[0],v[2]); dp[2][0][1]=ct(v[0],v[1]); dp[2][1][0]=ct(v[0],v[2])+ct(v[1],v[2]); dp[2][1][1]=0;
  for(ll i = 3 ; i < n ; i++){
     dp[i][0][0]=minm(dp[i-2][0][0],dp[i-2][0][1]+ct(v[i-1],v[i-2])+ct(v[i],v[i-2]),dp[i-2][1][0]+ct(v[i-2],v[i-3])+ct(v[i-3],v[i-1]),dp[i-2][1][1]+ct(v[i-1],v[i-2])+ct(v[i-3],v[i-1])+ct(v[i-2],v[i]));
     dp[i][0][1]=minm(dp[i-2][0][0], dp[i-2][0][1]+ct(v[i-1],v[i-2]) , dp[i-2][1][0]+ct(v[i-2],v[i-3]) , dp[i-2][1][1]+ct(v[i-1],v[i-2])+ct(v[i-1],v[i-3]));
     dp[i][1][0]=minm(dp[i-2][0][0]+ct(v[i],v[i-1]),dp[i-2][0][1]+ct(v[i],v[i-1])+ct(v[i],v[i-2]),dp[i-2][1][1]+ct(v[i],v[i-1])+ct(v[i],v[i-2]),dp[i-2][1][0]+ct(v[i-1],v[i])+ct(v[i-2],v[i-3]));
     dp[i][1][1]=minm(dp[i-2][0][0],dp[i-2][0][1],dp[i-2][1][0]+ct(v[i-2],v[i-3]),dp[i-2][1][1]);
  }
  cout << min(dp[n-1][1][0],dp[n-1][0][0]) << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
   //cin.tie(NULL); --> on it for interactive problems
   /* #ifndef ONLINE_JUDGE
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   #endif*/
   //int t;
   //cin >> t;
   //while(t--){
    solve();
   //
  }
