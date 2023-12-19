a,v = map(int,input().strip().split())
l,d,w = map(int,input().strip().split())

def solve(a,v,l,d,w):
    if w >= v or (2*a*d) <= (w*w):
        # the limit doesn't matter here
        if 2*a*l <= (v*v): return ((2*l)/a)**0.5
        else: return (l/v + v/(2*a))
    else:
        
        if 2*a*d <= (2*v*v - w*w) :
            vmax = (a*d + (w*w)/2)**0.5
            tin = (2*vmax - w)/a
            
            if v*v - w*w >= 2*a*(l-d): return tin + ((w*w + 2*a*(l-d))**0.5  - w)/a    
            else: return tin + (v-w)/a  + (l-d)/v  + (w*w-v*v)/(2*a*v)
        else:
            tin = ((w*w -2*v*v + 2*a*d)  / (2*a*v)) + (2*v - w)/a
            
            if v*v - w*w >= 2*a*(l-d): return tin + ((w*w + 2*a*(l-d))**0.5  - w)/a    
            else: return tin + (v-w)/a  + (l-d)/v  + (w*w-v*v)/(2*a*v)           
            
            
    

print(solve(a,v,l,d,w))