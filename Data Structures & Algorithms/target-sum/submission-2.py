class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}
        
        def decide(index, positive, total = 0):
            if index >= len(nums):
                return 0
            
            num = nums[index] * (-1 if not positive else 1)
            total = total + num
            if index == len(nums) - 1:
                if total == target:
                    return 1
                return 0
            
            if (index, positive, total) not in cache:
                cache[(index, positive, total)] = decide(index + 1, True, total) + decide(index + 1, False, total)

            return cache[(index, positive, total)]
        
        return decide(0, True) + decide(0, False)