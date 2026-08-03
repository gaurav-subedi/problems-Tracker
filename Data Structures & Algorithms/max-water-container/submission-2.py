class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            a , b = heights[l], heights[r]
            mini = min(a, b)
            area = max(area, mini * (r-l))

            if(a < b):
                l += 1
            else:
                r -= 1

        return area

            

