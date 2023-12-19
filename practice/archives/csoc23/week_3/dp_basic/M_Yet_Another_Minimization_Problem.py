"""

S = sum{i:1..n}sum{j: i<j<=n} (ai^2 + aj^2 + bi^2 + bj^2 + 2 (ai*aj + bi*bj)) 

 a1*a2+a1*a3+a1*a4+...+a1*an
      +a2*a3+a2*a4+...+a2*an           +    [similar stuff for B]
            +a3*a4+...+a3*an
                   ...      
                      +a{n-1}an            
                     
𝚫S(k) = sum after swapping ak, bk - Original

-(ak*a_{k+1} + bk*b_{k+1} + a1*ak+a2*ak+...+a{k-1}ak + b1*bk+b2*bk+...+b{k-1}bk)
+(bk*a_{k+1} + ak*b_{k+1} + a1*bk+a2*bk+...+a{k-1}bk + b1*ak+b2*ak+...+b{k-1}ak)
= - (ak-bk)*(a_{k+1}+a1+...+a{k-1} - b_{k+1}+b1+...+b{k-1})

𝚫 needs to be as negative as possible 

O(n**3)

"""