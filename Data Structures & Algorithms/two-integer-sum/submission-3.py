class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in hashSet:
                return [hashSet[diff], i]
            hashSet[j] = i
