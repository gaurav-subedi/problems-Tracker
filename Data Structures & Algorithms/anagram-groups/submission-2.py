class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for i in s:
               count[ord("a")-ord(i)] += 1
            count = tuple(count)
            hashMap[count].append(s)

        listt = []
        for anagram in hashMap.values():
            listt.append(anagram)

        return listt



