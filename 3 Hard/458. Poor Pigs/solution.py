class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie
        pigs = 0
        while True:
            if ((tests + 1) ** pigs >= buckets):
                return pigs
            pigs += 1
