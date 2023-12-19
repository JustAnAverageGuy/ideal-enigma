# #define rep(i, a, b) for(int i=(a); i<(b); i++)
# #define repi(i, a, b) for(int i=(a); i>(b); i--)
# #define iceil(n, x) (((n) + (x) - 1) / (x))

# #define N 20
 

# const int inf = 1e7;

# int dp[N][N][N];
# # dp[i][j][k]: Min. no. of shots to kill the archers starting from the ith archer
# # when the previous soldier still has j health points left
# # and the no. of direct shots at the previous soldiers were k

# int num[N][N][N];
# # num[i][j][k]: No. of direct attacks on ith soldier
# # that leads to the min. total no. of arrows 
# # needed to kill soldiers starting from the ith soldier
# # in the state dp[i][j][k]

# int hlth[N][N][N];
# # hlth[i][j][k]: The remaining health of the ith soldier after
# # considering direct attacks on it
# # and the direct attacks on the archer to its left
# # that leads to the optimal answer(min. no. of total arrows)
# # from the state dp[i][j][k]

# int h[N], n, a, b;
# vector<int> result; //The result

# # Assume that the archer no. 0 and n-1 have already been killed,
# # so we are only left with the archers from 1 .. n-2

# int rec(int i, int j, int k) {
#     if(i == n-1) {
#         //Reached the last soldier
#         //If prev. archer is still healthy, it's no longer
#         //possible to kill him
#         if(j > 0) {
#             return inf;
#         }
#         else {
#             return 0;
#         }
#     }

#     int &ans = dp[i][j][k];
#     if(ans != -1) return ans;

#     ans = inf;

#     int hh = h[i] - k*b; //New Health of the current archer after considering the damage incurred
#                          //from the direct attacks on the previous soldier
#     for(int x = 0; x <= 16; x++) {

#         if(x * b < j) {
#             //If x direct bullets on the current archer
#             //are not enough to kill the previous archer
#             continue;
#         }

#         int nh = max(0, hh - x*a); //New health of current archer after considering direct attacks
#         int kk = rec(i+1, nh, x) + x;
#         if(kk < ans) {
#             ans = kk;
#             num[i][j][k] = x;
#             hlth[i][j][k] = nh;
#         }
#     } 
#     return ans;
# }

# void compute_result(int i, int j, int k) {
#     if(i == n-1) {
#         return;
#     }

#     int m = num[i][j][k]; #No. of arrows shot directly at the ith soldier
#     while(m--) {
#         result.pb(i);
#     }
#     compute_result(i+1, hlth[i][j][k], num[i][j][k]);
# }

# main()
# {   
    
#     cin >> n >> a >> b;
#     rep(i, 0, n) {
#         cin >> h[i]; h[i]++;
#     }

#     memset(dp, -1, sizeof dp);
#     while(h[0] > 0) {
#         //Make direct shots at soldier 1
#         h[0] -= b;
#         h[1] -= a;
#         h[2] -= b;
#         result.pb(1);
#         //db(1);
#     }

#     h[0] = max(0, h[0]);
#     h[1] = max(0, h[1]);
#     h[2] = max(0, h[2]);

#     while(h[n-1] > 0) {
#         //Make direct shots at soldier (n-2)
#         h[n-1] -= b;
#         h[n-2] -= a;
#         h[n-3] -= b;
#         result.pb(n-2);
#         //db(2);
#     }

#     h[n-1] = max(0, h[n-1]);
#     h[n-2] = max(0, h[n-2]);
#     h[n-3] = max(0, h[n-3]);

#     rec(1, h[0], 0);

#     compute_result(1, h[0], 0);

#     cout << result.size() << '\n';
#     for(int i : result) cout << i+1 << ' '; cout << '\n';
    

# }


# n,a,b = map(int,input().strip().split())
