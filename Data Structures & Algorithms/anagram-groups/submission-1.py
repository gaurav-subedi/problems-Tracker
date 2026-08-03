class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c)-ord('a')] += 1
            count = tuple(count)
            if count not in hashSet:
                hashSet[count].append(string)
            else:
                hashSet[count].append(string)

        listt = []
        for value in hashSet.values():
            listt.append(value)
        return listt



