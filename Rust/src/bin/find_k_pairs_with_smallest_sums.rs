use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
    let mut res = Vec::new();
    if nums1.is_empty() || nums2.is_empty() {
        return res;
    }
    let k = k as usize;
    // min-heap of (sum, i, j)
    let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
    for i in 0..nums1.len().min(k) {
        heap.push(Reverse((nums1[i] + nums2[0], i, 0)));
    }
    while res.len() < k {
        let Reverse((_, i, j)) = match heap.pop() {
            Some(x) => x,
            None => break,
        };
        res.push(vec![nums1[i], nums2[j]]);
        if j + 1 < nums2.len() {
            heap.push(Reverse((nums1[i] + nums2[j + 1], i, j + 1)));
        }
    }
    res
}

fn main() {
    println!("{:?}", k_smallest_pairs(vec![1, 7, 11], vec![2, 4, 6], 3)); // [[1, 2], [1, 4], [1, 6]]
    println!("{:?}", k_smallest_pairs(vec![1, 1, 2], vec![1, 2, 3], 2)); // [[1, 1], [1, 1]]
    println!("{:?}", k_smallest_pairs(vec![1, 2], vec![3], 3)); // [[1, 3], [2, 3]]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            k_smallest_pairs(vec![1, 7, 11], vec![2, 4, 6], 3),
            vec![vec![1, 2], vec![1, 4], vec![1, 6]]
        );
        assert_eq!(
            k_smallest_pairs(vec![1, 1, 2], vec![1, 2, 3], 2),
            vec![vec![1, 1], vec![1, 1]]
        );
        assert_eq!(
            k_smallest_pairs(vec![1, 2], vec![3], 3),
            vec![vec![1, 3], vec![2, 3]]
        );
    }
}
