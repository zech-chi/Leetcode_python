class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        size = len(piles) // 3
        i = len(piles) - 2
        Sum = 0
        while size:
            Sum += piles[i]
            i -= 2
            size -= 1
        
        return Sum
