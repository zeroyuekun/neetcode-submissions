class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Find the largest height x length combination
        # make sure it's not slanted (must be same height)
        l,r = 0, len(height) - 1
        maxArea = 0
        while r > l:
            curHeight = min(height[l], height[r])
            curLength = r - l # 1
            curMax = curHeight * curLength
            maxArea = max(curMax, maxArea)
            if height[l] > height[r]:
                r-=1
            elif height[r] >= height[l]:
                l+=1

        return maxArea
        