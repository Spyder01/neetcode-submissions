use std::collections::VecDeque;

impl Solution {
    pub fn islands_and_treasure(grid: &mut Vec<Vec<i32>>) {
        let (m, n) = (grid.len(), grid[0].len());
        let (mi, ni) = (m as isize, n as isize);
        let mut q = VecDeque::<(usize, usize)>::with_capacity(m*n);

        const DIR: [(isize, isize); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != 0 {
                    continue;
                }

                q.push_back((i, j));
            }
        }

        while let Some((x, y)) = q.pop_front() {
            let dist = grid[x][y] + 1;
            for &(dx, dy) in &DIR {
                let (nxi, nyi) = (x as isize + dx, y as isize + dy);
                if nxi < 0 || nyi < 0 || nxi >= mi || nyi >= ni {
                    continue;
                }

                let (nx, ny) = (nxi as usize, nyi as usize);
                if grid[nx][ny] != i32::MAX {
                    continue;
                }

                grid[nx][ny] = dist;
                q.push_back((nx, ny));
            }
        }
    }
}
