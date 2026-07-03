class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0

        nb_rows, nb_columns = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(nb_columns)] for _ in range(nb_rows)]
        nb_islands = 0

        def explore(row = 0, column = 0):
            if row < 0 or column < 0 or row >= nb_rows or column >= nb_columns or visited[row][column] or grid[row][column] == "0":
                return
            
            visited[row][column] = True
    
            for x, y in directions:
                explore(row+x, column+y)

        
        for row in range(nb_rows):
            for col in range(nb_columns):
                if visited[row][col] or grid[row][col] == "0":
                    continue

                print(row, col)
                explore(row, col)
                nb_islands += 1

        return nb_islands

            

        