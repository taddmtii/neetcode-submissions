class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for num, count in count.items():
            buckets[count].append(num)
        
        res = []
        # Go through in descending order since most frequent are at the end.
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
            if len(res) == k:
                return res
