impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
            // combine the position/speed vectors into pairs
            let mut pairs: Vec<(i32, i32)> = position.into_iter().zip(speed.into_iter()).collect();

            // sort the pairs in descending order by position
            pairs.sort_by(|position, speed| speed.0.cmp(&position.0));

            // instantiate a stack as a Vec of floats
            let mut stack: Vec<f64> = Vec::new();

            // loop through the pairs that are in descending order by position
            for (position, speed) in pairs {
                // calculate the time to reach the target for the car
                let mut timeToReachTarget = (target - position) as f64 / speed as f64;

                // push it on to the stack so we can use it later
                stack.push(timeToReachTarget);

                // save the stack length since we'll use it multiple times 
                let stackLength = stack.len();

                // if the stack isn't just one element, and the fleets can't be collapsed together, pop
                if stackLength >= 2 && stack[stackLength - 1] <= stack[stackLength - 2] {
                    stack.pop();
                }
            }

            stack.len() as i32
    }
}
