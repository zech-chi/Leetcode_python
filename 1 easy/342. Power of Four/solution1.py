import math

class Solution:
    def log4(self, n):
        return math.log(n) / math.log(4)

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        r = self.log4(n)
        return 4 ** r == 4 ** int(r)
