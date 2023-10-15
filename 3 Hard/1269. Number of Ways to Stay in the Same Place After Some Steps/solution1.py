class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memoize = {}
        mod = 10 ** 9 + 7

        def dfs(curPos, stepsleft):
            if stepsleft == 0:
                return curPos == 0
            if (curPos, stepsleft) in memoize:
                return memoize[(curPos, stepsleft)]
            
            res = (dfs(curPos, stepsleft - 1)) % mod
            if curPos > 0:
                res = (res + dfs(curPos - 1, stepsleft - 1)) % mod
            if curPos < arrLen - 1:
                res = (res + dfs(curPos + 1, stepsleft - 1)) % mod
            
            memoize[(curPos, stepsleft)] = res
            return res
        
        return dfs(0, steps)
