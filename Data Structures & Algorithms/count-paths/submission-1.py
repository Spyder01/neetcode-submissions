class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if 0 in (m,n):
            return 0
        
        DIRECTIONS=[(1,0), (0,1)]

        graph = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        def explore(row=0, column = 0):
            nonlocal count
            if row == m - 1 and column == n - 1:
                count += 1
                return 1
            
            if row < 0 or column < 0 or column >= n or row >= m or graph[row][column]:
                return 0

            graph[row][column] = True 

            res = 0
            for x, y in DIRECTIONS:
                res += explore(row + x, column + y)
            
            graph[row][column] = False

            return res
        
        return explore()

        