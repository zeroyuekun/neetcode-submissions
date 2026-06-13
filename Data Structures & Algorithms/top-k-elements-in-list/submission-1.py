class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create hashmap
        countMap = {}
        # Create frequency array
        freq = [[] for i in range(len(nums) + 1)]

        # Create hashmap that tracks num of occurences for each number in the list of nums
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        # iterate thru the map, append to the freq array
        for num, count in countMap.items():
            freq[count].append(num)

        # return top k elements in terms of occurrences in a list
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res