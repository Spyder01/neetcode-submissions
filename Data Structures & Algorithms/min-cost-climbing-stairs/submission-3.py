cache = {}

class Solution:
    def minCostClimbingStairs(self, cost: List[int], index = 0) -> int:
        if len(cost) <= 1:
            return 0
        
        def backtrack(index):
            if index >= len(cost) or len(cost) <= 1:
                return 0
            
            return cost[index] + min(backtrack(index+1), backtrack(index + 2))
        
        return min(backtrack(0), backtrack(1))
            

        