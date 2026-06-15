/**
 * Definition of Interval:
 * #[derive(Debug, Clone)]
 * pub struct Interval {
 *     pub start: i32,
 *     pub end: i32,
 * }
 *
 * impl Interval {
 *     pub fn new(start: i32, end: i32) -> Self {
 *         Interval { start, end }
 *     }
 * }
 */

impl Solution {
    pub fn can_attend_meetings(intervals: Vec<Interval>) -> bool {
        if intervals.len() == 0 {
            return true
        }
        let mut intervals = intervals;
        intervals.sort_by_key(|i| i.start);
        for i in 0..intervals.len() - 1 {
            println!("({}, {})", intervals[i].start, intervals[i].end);
            println!("({}, {})", intervals[i+1].start, intervals[i+1].end);
            if intervals[i+1].start < intervals[i].end {
                return false
            }
        }

        return true 
    }
}
