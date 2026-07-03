class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            num = nums[mid]

            if num == target:
                return mid
            
            if num > target:
                r -= 1
            else:
                l += 1
        
            
        return -1
        