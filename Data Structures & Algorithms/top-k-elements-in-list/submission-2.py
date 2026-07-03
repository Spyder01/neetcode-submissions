class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = defaultdict(int)

        for x in nums:
            countMap[x] += 1


        bucket = {}
        max_ = -1
        for x, count in countMap.items():
            if count > max_:
                max_ = count

            if count not in bucket:
                bucket[count] = []

            bucket[count].append(x)
        
        res = []
        for i in range(max_+1, 0, -1):
            if i in bucket:
                res.extend(bucket[i])

            if len(res) == k:
                return res
        
        return res
        