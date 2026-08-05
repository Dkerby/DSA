impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut start = 0;
        let mut end = nums.len() - 1;

        while start <= end {
            let mid = start + (end - start) / 2;
            if nums[mid] == target {
                return mid as i32;
            }
            // the left side is sorted 
            if nums[start] <= nums[mid] {
                if(target >= nums[start] && target < nums[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } 
            // the right side is sorted
            else {
                if(target > nums[mid] && target <= nums[end]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }

        }

        return -1 as i32;
    }
}
