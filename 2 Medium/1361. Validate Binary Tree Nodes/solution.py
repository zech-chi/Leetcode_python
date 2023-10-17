class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        hasParent = set(leftChild + rightChild)
        if -1 in hasParent:
            hasParent.remove(-1)
        if len(hasParent) == n:
            return False
        
        root = -1
        count_roots = 0
        for i in range(n):
            if i not in hasParent:
                root = i
                count_roots += 1
            if count_roots > 1:
                return False
        

        visited = set()
        def dfs(i):
            if i == -1:
                return True
            if i in visited:
                return False
            visited.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        
        return dfs(root) and len(visited) == n
