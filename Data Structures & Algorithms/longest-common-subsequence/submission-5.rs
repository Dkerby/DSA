impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        
                let (t1, t2) = if text1.len() >= text2.len() {
            (text1.as_bytes(), text2.as_bytes())
        } else {
            (text2.as_bytes(), text1.as_bytes())
        };

        let mut curr = vec![0i32; t2.len() + 1];

        for r in (0..t1.len()).rev() {
            let mut prev = 0;
            for c in (0..t2.len()).rev() {
                let temp = curr[c];
                if t1[r] == t2[c] {
                    curr[c] = 1 + prev;
                } else {
                    curr[c] = max(curr[c], curr[c+1]);
                } 
               prev = temp; 
            }
        }

        curr[0]
    }
}
