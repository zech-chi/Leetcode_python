class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            #odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (right - left + 1) < (r - l + 1):
                    left, right = l, r
                l -= 1
                r += 1
            
            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (right - left + 1) < (r - l + 1):
                    left, right = l, r
                l -= 1
                r += 1
            
        return s[left: right + 1]
