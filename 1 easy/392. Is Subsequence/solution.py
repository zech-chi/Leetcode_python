class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        s_len = len(s)
        for t_index in range(len(t)):
            if s_index == s_len:
                return True
            if s[s_index] == t[t_index]:
                s_index += 1
        if s_index == s_len:
                return True
        return False
