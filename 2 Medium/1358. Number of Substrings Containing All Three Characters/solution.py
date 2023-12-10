class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        A = []
        B = []
        C = []
        for i in range(len(s)):
            if s[i] == 'a':
                A.append(i)
            elif s[i] == 'b':
                B.append(i)
            elif s[i] == 'c':
                C.append(i)

        if A == [] or B == [] or C == []:
            return 0 
        
        a, b, c = 0, 0, 0
        count = 0
        for i in range(len(s) - 2):
            if i > A[a]:
                if a >= len(A) - 1:
                    break
                a += 1
            if i > B[b]:
                if b >= len(B) - 1:
                    break
                b += 1
            if i > C[c]:
                if c >= len(C) - 1:
                    break
                c += 1

            count += len(s) - max(A[a], B[b], C[c])
        
        return count
