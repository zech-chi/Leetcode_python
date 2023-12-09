class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        counter = 0
        l = 0
        for r in range(len(s)):
            if s[r] == '(':
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                res += s[l + 1:r]
                l = r + 1
        
        return res
