class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        Max = nums[k]
        Min = nums[k]
        l = k
        r = k

        while l > 0 or r < len(nums) - 1:
            Left = nums[l - 1] if l > 0 else 0
            Right = nums[r + 1] if r < len(nums) - 1 else 0
            if Left > Right:
                Min = min(Min, Left)
                l -= 1
            else:
                Min = min(Min, Right)
                r += 1
            Max = max(Max, Min * (r - l + 1))

        return Max
