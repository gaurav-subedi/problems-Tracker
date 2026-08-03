class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strs = set()
        lenn = 0
        l = 0
        for i in range(len(s)):
            while s[i] in strs:
                strs.remove(s[l])
                l += 1
            strs.add(s[i])
            lenn = max(lenn, i - l + 1)
        return lenn