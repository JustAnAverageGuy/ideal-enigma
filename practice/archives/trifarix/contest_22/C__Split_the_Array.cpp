#include <bits/stdc++.h>
using namespace std;
#define int long long int
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
void solve()
{
    long n,i,j;
    cin>>n;
    int A[n+1],DP[n+1];
    for(i=1;i<=n;i++)
        cin>>A[i];
    memset(DP,0,sizeof(DP));
    unordered_map<int,int> M;
    for(i=1;i<=n;i++)
    {
        vector<int> Fact;
        Fact.push_back(A[i]);
        for(j=2;j*j<=A[i];j++)
        {
            if(A[i]%j==0)
            {
                if(j*j==A[i])
                {
                    Fact.push_back(j);
                }
                else
                {
                    Fact.push_back(j);
                    Fact.push_back(A[i]/j);
                }
            }
        }
        int ans=DP[i-1]+1;
        for(j=0;j<Fact.size();j++)
        {
            if(M.find(Fact[j])==M.end())
            {
                M[Fact[j]]=DP[i-1];
            }
            else
            {
                ans=min(ans,M[Fact[j]]+1);
            }
        }
        DP[i]=ans;
    }
    cout<<DP[n]<<endl;
}
int32_t main()
{
    boost;
        solve();
}
