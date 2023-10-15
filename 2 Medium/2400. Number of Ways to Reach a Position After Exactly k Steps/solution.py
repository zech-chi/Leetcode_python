class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memoize = {}
        mod = 10 ** 9 + 7

        def dfs(curPos, stepsleft):
            if stepsleft == 0:
                return curPos == endPos
            if (curPos, stepsleft) in memoize:
                return memoize[(curPos, stepsleft)]
            

            res = dfs(curPos - 1, stepsleft - 1) % mod
            res = (res + dfs(curPos + 1, stepsleft - 1)) % mod
            
            memoize[(curPos, stepsleft)] = res
            return res
        
        return dfs(startPos, k)
