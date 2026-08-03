class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))

        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1

        return len(hashMap) != len(nums)