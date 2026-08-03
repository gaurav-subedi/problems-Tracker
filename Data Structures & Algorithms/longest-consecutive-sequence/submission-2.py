class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            total = 0
            nums = set(nums)
            i=0
            for n in nums:
                cons = 1
                if(n-1 not in nums):
                  while n + cons in nums:
                    cons += 1
                total = max(cons, total)
            return total




