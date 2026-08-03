class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] = count.get(n,0) + 1
        #We need to store the elements which are repeated for the same number of times
        buckets = [[] for _ in range(len(nums)+1)]

        for c,v in count.items():
            buckets[v].append(c)

        result = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                result.append(j)
            if len(result) == k:
                return result
        return []