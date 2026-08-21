impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut cache = vec![0; n+1];
        cache[n-1] = 1;

        for r in (0..m).rev() {
            for c in (0..n).rev() {
                // if it's blocked, we don't have a count here 
                if obstacle_grid[r][c] == 1 {
                    cache[c] = 0;
                }

                else {
                    cache[c] += cache[c + 1];
                }
            }
        }

        cache[0]
    }
}
