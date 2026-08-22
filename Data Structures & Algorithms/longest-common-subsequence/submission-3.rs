impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let m = text1.len();
        let n = text2.len();
        let bytes1 = text1.as_bytes();
        let bytes2 = text2.as_bytes();

        let mut prev = vec![0i32; n + 1];
        let mut curr = vec![0i32; n + 1];

        for r in (0..m).rev() {
            for c in (0..n).rev() {
                if bytes1[r] == bytes2[c] {
                    curr[c] = 1 + prev[c + 1];
                } else {
                    curr[c] = max(curr[c + 1], prev[c])
                } 
            }
            std::mem::swap(&mut prev, &mut curr);
            curr.fill(0);
        }

        prev[0]
    }
}
