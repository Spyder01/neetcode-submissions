class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        bag = set(nums)
        maxCount = 0

        for x in bag:

            if x - 1 not in bag:
                count = 1
            else:
                continue
            
            while x + count in bag:
                count += 1
            
            if count > maxCount:
                maxCount = count
        
        return maxCount

