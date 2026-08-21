impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut cache = vec![vec![0; n+1]; m+1]; 
        cache[m-1][n-1] = 1;

        for r in (0..m).rev() {
            for c in (0..n).rev() {
                // if it's blocked, it's nothing
                if obstacle_grid[r][c] == 1 {
                    cache[r][c] = 0;
                }

                else {
                    cache[r][c] += cache[r + 1][c];
                    cache[r][c] += cache[r][c + 1];
                }
            }
        }

        cache[0][0]
    }
}
