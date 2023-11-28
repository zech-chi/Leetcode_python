class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        keep_going = True
        while keep_going:
            keep_going = False
            for i in range(len(expected) - 1):
                if expected[i] > expected[i + 1]:
                    expected[i], expected[i + 1] = expected[i + 1], expected[i]
                    keep_going = True
        
        
        diff = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                diff += 1
        
        return diff
