class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Handle duplicates
        # sum up 3 distinct numbers to 0
        nums.sort()
        res = []
        s = set()
        # [-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    threeSum = nums[i] + nums[j] + nums[k]
                    if threeSum == 0:
                        s.add(tuple([nums[i], nums[j], nums[k]]))
        return [list(items) for items in s]
                        