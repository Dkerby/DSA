impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut obstacle_grid = obstacle_grid;
        if obstacle_grid[0][0] == 1 || obstacle_grid[m-1][n-1] == 1 {
           return 0; 
        }

        obstacle_grid[m-1][n-1] = 1;

        for r in (0..m).rev() {
            for c in (0..n).rev() {
                if r == m - 1 && c == n - 1 {
                    continue;
                }

                if obstacle_grid[r][c] == 1 {
                    obstacle_grid[r][c] = 0;
                } else {
                    if r + 1 < m {
                        obstacle_grid[r][c] += obstacle_grid[r + 1][c];
                    }
                    if c + 1 < n {
                        obstacle_grid[r][c] += obstacle_grid[r][c + 1];
                    } 
                }
            }
        }

        obstacle_grid[0][0]
    }
}
