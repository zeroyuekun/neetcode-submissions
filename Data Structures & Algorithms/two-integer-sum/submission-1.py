class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        diffMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[n] = i
        return []
        