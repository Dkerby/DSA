impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut cache = vec![vec![-1; n]; m]; 

        Self::dfs(0,0,&obstacle_grid, &mut cache, m, n)
    }

    pub fn dfs(r:usize, c:usize, grid: &Vec<Vec<i32>>, cache: &mut Vec<Vec<i32>>, m: usize, n: usize) -> i32{
        // We are outside of the bounds of the grid, or the spot is blocked,
        // so return a 0 for the count
        if r >= m || c >= n || grid[r][c] == 1{
            return 0;
        }

        // we reached a goal position, so increment the counter
        if r == m - 1 && c == n - 1 {
            return 1
        }

        if cache[r][c] > -1 {
            return cache[r][c];
        }

        // add the result to the cache, then return the cached value
        cache[r][c] = Self::dfs(r + 1, c, grid, cache, m, n) + Self::dfs(r, c + 1, grid, cache, m, n);
        
        cache[r][c]
    }
}
