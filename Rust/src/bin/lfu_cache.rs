use std::collections::{BTreeSet, HashMap};

struct LFUCache {
    cap: usize,
    key_val: HashMap<i32, i32>,
    key_freq: HashMap<i32, i32>,
    key_order: HashMap<i32, u64>,
    // freq -> ordered set of (insertion_order, key); front = least recently used
    buckets: HashMap<i32, BTreeSet<(u64, i32)>>,
    min_freq: i32,
    counter: u64,
}

impl LFUCache {
    fn new(capacity: i32) -> Self {
        Self {
            cap: capacity.max(0) as usize,
            key_val: HashMap::new(),
            key_freq: HashMap::new(),
            key_order: HashMap::new(),
            buckets: HashMap::new(),
            min_freq: 0,
            counter: 0,
        }
    }

    fn touch(&mut self, key: i32) {
        let f = self.key_freq[&key];
        let ord = self.key_order[&key];
        let b = self.buckets.get_mut(&f).unwrap();
        b.remove(&(ord, key));
        if b.is_empty() {
            self.buckets.remove(&f);
            if self.min_freq == f {
                self.min_freq += 1;
            }
        }
        self.counter += 1;
        let nord = self.counter;
        self.key_freq.insert(key, f + 1);
        self.key_order.insert(key, nord);
        self.buckets.entry(f + 1).or_default().insert((nord, key));
    }

    fn get(&mut self, key: i32) -> i32 {
        if let Some(&v) = self.key_val.get(&key) {
            self.touch(key);
            v
        } else {
            -1
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        if self.cap == 0 {
            return;
        }
        if self.key_val.contains_key(&key) {
            self.key_val.insert(key, value);
            self.touch(key);
            return;
        }
        if self.key_val.len() >= self.cap {
            let b = self.buckets.get_mut(&self.min_freq).unwrap();
            let &(ord, ek) = b.iter().next().unwrap();
            b.remove(&(ord, ek));
            if b.is_empty() {
                self.buckets.remove(&self.min_freq);
            }
            self.key_val.remove(&ek);
            self.key_freq.remove(&ek);
            self.key_order.remove(&ek);
        }
        self.counter += 1;
        let ord = self.counter;
        self.key_val.insert(key, value);
        self.key_freq.insert(key, 1);
        self.key_order.insert(key, ord);
        self.buckets.entry(1).or_default().insert((ord, key));
        self.min_freq = 1;
    }
}

fn main() {
    let ops = [
        "LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get",
    ];
    let args: [(i32, i32); 11] = [
        (2, 0),
        (1, 1),
        (2, 2),
        (1, 0),
        (3, 3),
        (2, 0),
        (3, 0),
        (4, 4),
        (1, 0),
        (3, 0),
        (4, 0),
    ];
    let mut c = LFUCache::new(0);
    let mut out: Vec<String> = Vec::new();
    for (op, &(a, b)) in ops.iter().zip(args.iter()) {
        match *op {
            "LFUCache" => {
                c = LFUCache::new(a);
                out.push("null".into());
            }
            "get" => out.push(c.get(a).to_string()),
            "put" => {
                c.put(a, b);
                out.push("null".into());
            }
            _ => {}
        }
    }
    println!("[{}]", out.join(", "));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        let mut c = LFUCache::new(2);
        c.put(1, 1);
        c.put(2, 2);
        assert_eq!(c.get(1), 1);
        c.put(3, 3);
        assert_eq!(c.get(2), -1);
        assert_eq!(c.get(3), 3);
        c.put(4, 4);
        assert_eq!(c.get(1), -1);
        assert_eq!(c.get(3), 3);
        assert_eq!(c.get(4), 4);
    }
}
