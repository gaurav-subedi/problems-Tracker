class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums)-1
        mini = nums[0]

        while l <= r:
            if nums[r] > nums[l]:
                mini = min(mini, nums[l])
                break
            m = (l+r) // 2
            mini = min(mini, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m -1
            
        return mini

