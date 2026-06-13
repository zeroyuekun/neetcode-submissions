class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # obvious solution is to sort
        # O(nlogn)
        occurrenceSet = set()
        maxLengthOfSeq = 0
        for num in nums:
            occurrenceSet.add(num)

        for num in nums:
            if self.isStartOfASequence(num, occurrenceSet):
                maxLengthOfSeq = max(self.countLengthOfSeq(num, occurrenceSet), maxLengthOfSeq)

        return maxLengthOfSeq

    def isStartOfASequence(self, num: int, occurrenceSet: set) -> bool:
        prevNum = num - 1
        if prevNum not in occurrenceSet:
            return True
        return False
    
    # Used after we find the start of the sequence
    def countLengthOfSeq(self, num: int, occurrenceSet: set) -> int:
        endOfSeq = False
        lengthOfSeq = 1
        cur = num
        while not endOfSeq:
            if cur+1 in occurrenceSet:
                lengthOfSeq +=1
                cur+=1
            else:
                endOfSeq = True
        return lengthOfSeq
