use std::collections::HashMap;

struct TimeMap {
    key_store: HashMap<String, Vec<(i32, String)>>
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {key_store: HashMap::new()}
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.key_store.entry(key).or_default().push((timestamp, value));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        // if it's empty, just return ""
        let values = match self.key_store.get(&key) {
            Some(v) => v,
            None => return String::new(),
        }; 

        // need to do a binary search for a timestamp that has the largest previous timestamp
        let mut res = String::new();
        let mut l = 0 as i32;
        let mut r = values.len() as i32 - 1;
        while l <= r {
            let m = l + (r - l) / 2;
            let (t, value) = &values[m as usize];
            if *t <= timestamp {
                res = value.clone();
                l = m+1;
            } else {
                r = m-1;
            }
        }

        res
    }
}
