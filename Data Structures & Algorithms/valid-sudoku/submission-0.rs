impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows = [[0_u8; 9]; 9];
        let mut cols = [[0_u8; 9]; 9];
        let mut grid = [[0_u8; 9]; 9];

        for i in 0..9 {
            for j in 0..9 {
                if board[i][j] == '.' {
                    continue;
                }
                
                let val = (board[i][j] as u8 - '0' as u8) as usize - 1;

                if rows[i][val] == 1 {
                    return false;
                }

                if cols[j][val] == 1 {
                    return false;
                }

                if grid[3*(i/3)+j/3][val] == 1 {
                    return false;
                }

                rows[i][val] = 1;
                cols[j][val] = 1;
                grid[3*(i/3)+j/3][val] = 1;

            }
        }

        true
    }
}