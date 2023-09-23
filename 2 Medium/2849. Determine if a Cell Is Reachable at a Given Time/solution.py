class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy) and t == 1:
            return False
        dx = max(sx, fx) - min(sx, fx)
        dy = max(sy, fy) - min(sy, fy)
        if max(dx, dy) <= t:
            return True
        return False
