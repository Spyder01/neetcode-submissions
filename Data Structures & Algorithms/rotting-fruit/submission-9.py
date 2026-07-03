from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        minutes = 0
        nb_rows, nb_columns = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = []
        fresh = 0

        # Add all rotten oranges to the queue and count fresh oranges
        for row in range(nb_rows):
            for column in range(nb_columns):
                if grid[row][column] == 1:
                    fresh += 1
                elif grid[row][column] == 2:
                    queue.append((row, column))
        
        # Edge case: No fresh oranges to begin with
        if fresh == 0:
            return 0
        
        # Process the queue
        while len(queue) != 0:
            level_size = len(queue)
            infected = False

            for _ in range(level_size):
                row, column = queue.pop(0)

                for x, y in DIRECTIONS:
                    _row, _column = row + x, column + y

                    # Check boundaries and if the cell is a fresh orange
                    if 0 <= _row < nb_rows and 0 <= _column < nb_columns and grid[_row][_column] == 1:
                        # Infect the fresh orange
                        grid[_row][_column] = 2
                        fresh -= 1
                        queue.append((_row, _column))
                        infected = True

            # Increment minutes after processing a full level
            if infected:
                minutes += 1

        # If there are fresh oranges left, return -1
        return -1 if fresh != 0 else minutes
