use std::collections::HashMap;

struct TimeMap {
    key_store: HashMap<String, Vec<(String, i32)>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            key_store: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.key_store.entry(key).or_default().push((value, timestamp));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        let Some(values) = self.key_store.get(&key) else {
            return String::new();
        };
        let mut res = String::new();
        let (mut l, mut r) = (0i32, values.len() as i32 - 1);
        while l <= r {
            let m = (l + r) / 2;
            if values[m as usize].1 <= timestamp {
                res = values[m as usize].0.clone();
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        res
    }
}