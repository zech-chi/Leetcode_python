class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_s = {}
        dict_t = {}

        for c in s:
            if not c in dict_s:
                dict_s[c] = 0
            dict_s[c] += 1
        
        for c in t:
            if not c in dict_t:
                dict_t[c] = 0
            dict_t[c] += 1
        
        for c in dict_t:
            if not c in dict_s or dict_s[c] != dict_t[c]:
                return c
