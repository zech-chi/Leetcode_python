class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        h1, m1 = loginTime.split(':')
        h1 = int(h1)
        m1 = int(m1)
        start = h1 * 60
        if m1 % 15 == 0:
            start += m1
        else:
            start += (m1 // 15) * 15 + 15
            
        h2, m2 = logoutTime.split(':')
        h2 = int(h2)
        m2 = int(m2)
        end = h2 * 60
        if m2 % 15 == 0:
            end += m2
        else:
            end += (m2 // 15) * 15

        if (h1 == h2) and (0 <= (m2 - m1) < 15):
            return 0
        if h2 > h1:
            diff = (h2 - h1) * 60 + (m2 - m1)
            if diff < 15:
                return 0

        if end < start:
            end += 60 * 24
        

        return (end - start) // 15
