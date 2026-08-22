impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let m = text1.len();
        let n = text2.len();
        let mut cache = vec![vec![0;n+1]; m+1];
        let bytes1 = text1.as_bytes();
        let bytes2 = text2.as_bytes();

        for r in (0..m).rev() {
            for c in (0..n).rev() {
                if bytes1[r] == bytes2[c] {
                    cache[r][c] = 1 + cache[r+1][c+1];
                } else {
                    cache[r][c] = max(cache[r+1][c], cache[r][c+1]);
                } 
            }
        }

        return cache[0][0];
    }
}
