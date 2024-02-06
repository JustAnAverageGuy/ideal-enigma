class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        A = [[0]*52 for i in range(52)]
        for px, py in points: A[py][px+1] = 1
        
        for y in range(51,0,-1):
            for x in range(1, 52):
                A[y][x] += A[y+1][x] + A[y][x-1] - A[y+1][x-1]


        ans = 0
        for cx, cy in points:
            for tx, ty in points:
                if cx == tx and cy == ty: continue
                if cx > tx or cy > ty: continue
                cnt = A[ty][tx+1] - A[cy-1][tx+1] - A[ty+1][cx] + A[cy][cx]
                ans += (cnt == 2)
        return ans
                
