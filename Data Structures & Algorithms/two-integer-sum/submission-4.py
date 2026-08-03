class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashSet:
                return [hashSet[diff], i]
            
            hashSet[v] = i
