class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = ''.join(char.lower() for char in s if char.isalnum())
        l,r = 0, len(cleanedStr) - 1
        print(cleanedStr)

        while l < len(cleanedStr) and r >= 0:
            if cleanedStr[l] != cleanedStr[r]:
                return False
            l +=1
            r-=1
        return True