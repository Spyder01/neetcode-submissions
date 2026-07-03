class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if len(grid) == 0:
            return 0
        
        minutes = 0
        nb_rows, nb_columns = len(grid), len(grid[0])
        visited = [[False for _ in range(nb_columns)] for _ in range(nb_rows)]
        DIRECTIONS = [(1,0), (0, 1), (-1, 0), (0, -1)]

        queue = []
        fresh = 0
        for row in range(nb_rows):
            for column in range(nb_columns):
                if grid[row][column] == 1:
                    fresh += 1

                if grid[row][column] in (0, 1):
                    continue                
                
                queue.append((row, column))
        
        if fresh == 0:
            return 0
        
        while len(queue) != 0:
            level_size = len(queue)
            infected = False

            for _ in range(level_size):
                row, column = queue[0]
                queue = queue[1:]
    
                if row < 0 or column < 0 or row >= nb_rows or column >= nb_columns or visited[row][column] or grid[row][column] == 0:
                    continue
    
                visited[row][column] = True
                for x, y in DIRECTIONS:
                    _row, _column = row + x, column + y
                    if _row < 0 or _column < 0 or _row >= nb_rows or _column >= nb_columns or visited[_row][_column] or grid[_row][_column] == 0:
                        continue
                    
                    if grid[_row][_column] == 1:
                        grid[_row][_column] = 2
                        fresh -= 1
                        queue.append((_row, _column))
                        infected = True

                
            if infected:    
                minutes += 1

        if fresh != 0:
            return -1

        return minutes
        