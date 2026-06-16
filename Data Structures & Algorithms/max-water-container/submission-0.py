class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        res = 0

        while l<r:
            area = (r-l) * min(heights[l],heights[r])
            if heights[r] > heights [l]:
                l+=1
            else:
                r-=1
            
            res = max(res,area)
        
        return res

        