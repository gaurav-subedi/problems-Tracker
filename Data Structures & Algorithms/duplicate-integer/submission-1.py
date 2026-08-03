class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         listt = set()
         for i in nums:
            if i in listt:
                return True
            listt.add(i)
         return False