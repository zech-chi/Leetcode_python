class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0
        l = 1
        r = 2 ** (n - 1)

        for _ in range(n - 1):
            m = (l + r) // 2
            if k <= m:
                r = m
            else:
                l = m + 1
                ans = 0 if ans == 1 else 1
        
        return ans
