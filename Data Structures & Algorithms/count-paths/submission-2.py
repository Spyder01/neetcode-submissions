class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if 0 in (m,n):
            return 0
        
        DIRECTIONS=[(1,0), (0,1)]

        graph = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        cache = {}

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
                n_row, n_column = row + x, column + y

                if n_row not in cache:
                    cache[n_row] = {}
                
                if n_column not in cache[n_row]:
                    cache[n_row][n_column] = None
                
                if cache[n_row][n_column] is None:
                    cache[n_row][n_column] = explore(n_row, n_column)
                
                res += cache[n_row][n_column]
            
            graph[row][column] = False

            return res
        
        return explore()

        