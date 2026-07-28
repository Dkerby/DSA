impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut start = 0;
        let mut end = nums.len()-1; 

        while start < end {
            println!("start: {}, end: {}", start, end);
            let mut mid = start + (end - start) / 2;
            if nums[mid] > nums[end] {
                start = mid + 1;
            } else {
                end = mid;
            }
        }

        nums[start] as i32
    }
}