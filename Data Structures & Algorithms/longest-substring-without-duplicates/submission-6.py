class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        charSet = set(s[0])
        longest = 1
        l,r = 0, 1
        cur = 1
        while r < len(s):

            if s[r] in charSet:
                charSet.remove(s[l])
                l+=1
                cur-=1
            else:
                charSet.add(s[r])
                r+=1
                cur+=1
            longest = max(cur, longest)
        return longest


