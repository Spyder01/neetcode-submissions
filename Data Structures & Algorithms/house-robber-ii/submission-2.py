class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0 
        if n == 1:
            return nums[0]
        
        # For circular houses, we can split into two cases:
        # 1. Rob houses from 0 to n-2 (excluding the last house)
        # 2. Rob houses from 1 to n-1 (excluding the first house)
        # Then take the maximum of these two cases
        
        # Helper function for regular house robber (no circularity)
        def rob_linear(houses):
            if not houses:
                return 0
                
            n = len(houses)
            # dp[i] represents maximum money if considering houses 0 to i
            dp = [0] * n
            
            for i in range(n):
                if i == 0:
                    dp[i] = houses[i]
                elif i == 1:
                    dp[i] = max(houses[0], houses[1])
                else:
                    # Either rob current house + money from i-2, or skip current house
                    dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            
            return dp[-1]
        
        # Handle the circular case by running the algorithm twice
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))