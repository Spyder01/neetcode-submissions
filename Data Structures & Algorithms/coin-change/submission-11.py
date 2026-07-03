from collections import deque
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)  # Prioritize larger coins first
        queue = deque([(0, 0)])  # (current_sum, coin_count)
        visited = set()  # Track visited sums to avoid redundant computations

        while queue:
            total, count = queue.popleft()

            for coin in coins:
                new_total = total + coin

                if new_total == amount:
                    return count + 1  # Found the optimal solution
                
                if new_total < amount and new_total not in visited:
                    visited.add(new_total)
                    queue.append((new_total, count + 1))

        return -1  # No solution found
