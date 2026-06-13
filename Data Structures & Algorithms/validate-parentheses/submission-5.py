class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackMap = {"}" : "{", ")" : "(", "]" : "["}
        if len(s) <= 1:
            return False
        for c in s:
            if c in brackMap:
                if stack and stack[-1] == brackMap[c]:
                    openBracket = stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) > 0:
            return False
        return True

            
