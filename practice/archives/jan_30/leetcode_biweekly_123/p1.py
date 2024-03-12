class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]: return "none"
        s = set(nums)

        if len(s) == 1: return "equilateral"
        if len(s) == 2: return "isosceles"
        return "scalene"
        
