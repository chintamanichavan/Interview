use std::collections::{BinaryHeap, HashSet};

fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
    let n = nums.len();
    let mut logt = vec![0usize; n + 1];
    for i in 2..=n {
        logt[i] = logt[i / 2] + 1;
    }
    let mut up_max: Vec<Vec<i32>> = vec![nums.clone()];
    let mut up_min: Vec<Vec<i32>> = vec![nums.clone()];
    let mut j = 1;
    while (1usize << j) <= n {
        let half = 1usize << (j - 1);
        let length = 1usize << j;
        let pmx = &up_max[j - 1];
        let pmn = &up_min[j - 1];
        let mut cmx = vec![0i32; n - length + 1];
        let mut cmn = vec![0i32; n - length + 1];
        for i in 0..=(n - length) {
            cmx[i] = pmx[i].max(pmx[i + half]);
            cmn[i] = pmn[i].min(pmn[i + half]);
        }
        up_max.push(cmx);
        up_min.push(cmn);
        j += 1;
    }
    let value = |l: usize, r: usize| -> i64 {
        let j = logt[r - l + 1];
        let shift = 1usize << j;
        let mx = up_max[j][l].max(up_max[j][r + 1 - shift]);
        let mn = up_min[j][l].min(up_min[j][r + 1 - shift]);
        (mx - mn) as i64
    };

    let mut heap: BinaryHeap<(i64, usize, usize)> = BinaryHeap::new();
    let mut seen: HashSet<(usize, usize)> = HashSet::new();
    heap.push((value(0, n - 1), 0, n - 1));
    seen.insert((0, n - 1));
    let mut total = 0i64;
    for _ in 0..k {
        let (v, l, r) = heap.pop().unwrap();
        total += v;
        if l + 1 <= r && seen.insert((l + 1, r)) {
            heap.push((value(l + 1, r), l + 1, r));
        }
        if r >= 1 && l <= r - 1 && seen.insert((l, r - 1)) {
            heap.push((value(l, r - 1), l, r - 1));
        }
    }
    total
}

fn main() {
    println!("{}", max_total_value(vec![1, 3, 2], 2)); // 4
    println!("{}", max_total_value(vec![4, 2, 5, 1], 3)); // 12
    println!("{}", max_total_value(vec![1], 1)); // 0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(max_total_value(vec![1, 3, 2], 2), 4);
        assert_eq!(max_total_value(vec![4, 2, 5, 1], 3), 12);
        assert_eq!(max_total_value(vec![1], 1), 0);
    }
}
