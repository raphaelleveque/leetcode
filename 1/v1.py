class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap: [number, index]
        hashmap = {}
        for i, num in enumerate(nums):
            # y = target - x
            toFind = target - num
            if toFind in hashmap:
                return [i, hashmap[toFind]]
            hashmap[num] = i
        return []
        
