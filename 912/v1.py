class Solution:
    def merge(self, numsA, numsB: List[int]) -> List[int]:
        i, j = 0, 0
        res = []
        while i < len(numsA) and j < len(numsB):
            if numsA[i] <= numsB[j]:
                res.append(numsA[i])
                i += 1
            else:
                res.append(numsB[j])
                j += 1
        
        while i < len(numsA):
            res.append(numsA[i])
            i += 1
        
        while j < len(numsB):
            res.append(numsB[j])
            j += 1

        return res
        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        n = len(nums)
        numsA = nums[:n // 2]
        numsB = nums[n // 2:]

        numsA = self.sortArray(numsA)
        numsB = self.sortArray(numsB)

        return self.merge(numsA, numsB)
        
