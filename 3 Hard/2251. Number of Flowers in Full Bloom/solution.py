class Solution:
    def BinarySearch(self, arr, t):
        l = 0
        r = len(arr)
        while l < r:
            m = (l + r) // 2
            if t < arr[m]:
                r = m
            else:
                l = m + 1
        return l

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(flowers)
        start_flowers = [flowers[i][0] for i in range(n)]
        end_flowers = [flowers[i][1] + 1 for i in range(n)]
        start_flowers.sort()
        end_flowers.sort()
        Dict = {}
        set_people = set(people)
        for person in set_people:
            start = self.BinarySearch(start_flowers, person)
            end = self.BinarySearch(end_flowers, person)
            Dict[person] = start - end

        ans = [0] * len(people)
        for i in range(len(people)):
            ans[i] = Dict[people[i]]
        return ans
