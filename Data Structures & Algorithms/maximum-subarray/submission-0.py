class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cur_sum = nums[0], 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += num
            res = max(res, cur_sum)
        
        return res
        