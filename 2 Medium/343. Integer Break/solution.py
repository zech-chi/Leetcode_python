class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        div = n // 3
        mod = n % 3

        if mod == 0:
            return 3 ** div
        elif mod == 1:
            return 4 * (3 ** (div - 1))
        else:
            return 2 * (3 ** div)
