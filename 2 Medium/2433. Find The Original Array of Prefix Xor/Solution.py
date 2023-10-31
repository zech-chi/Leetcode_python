class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        Xor = pref[0]
        for i in range(1, len(pref)):
            n = Xor ^ pref[i]
            pref[i] = n
            Xor ^= n
        
        return pref
