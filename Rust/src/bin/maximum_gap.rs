fn maximum_gap(nums: Vec<i32>) -> i32 {
    let n = nums.len();
    if n < 2 {
        return 0;
    }
    let (mn, mx) = nums.iter().fold((nums[0], nums[0]), |(lo, hi), &x| {
        (lo.min(x), hi.max(x))
    });
    if mn == mx {
        return 0;
    }

    // Pigeonhole: max gap >= ceil((mx-mn)/(n-1)), so it lies between buckets of that size.
    let bucket_size = ((mx - mn) as usize / (n - 1)).max(1);
    let num_buckets = (mx - mn) as usize / bucket_size + 1;
    let mut buckets: Vec<Option<(i32, i32)>> = vec![None; num_buckets];

    for &x in &nums {
        let i = (x - mn) as usize / bucket_size;
        buckets[i] = Some(match buckets[i] {
            None => (x, x),
            Some((lo, hi)) => (lo.min(x), hi.max(x)),
        });
    }

    let mut best = 0;
    let mut prev_max = mn;
    for b in buckets.into_iter().flatten() {
        let (lo, hi) = b;
        best = best.max(lo - prev_max);
        prev_max = hi;
    }
    best
}

fn main() {
    println!("{}", maximum_gap(vec![3, 6, 9, 1]));  // 3
    println!("{}", maximum_gap(vec![10]));          // 0
    println!("{}", maximum_gap(vec![1, 1, 1, 1]));  // 0
    println!("{}", maximum_gap(vec![1, 10000000])); // 9999999
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(maximum_gap(vec![3, 6, 9, 1]), 3);
        assert_eq!(maximum_gap(vec![10]), 0);
        assert_eq!(maximum_gap(vec![1, 1, 1, 1]), 0);
        assert_eq!(maximum_gap(vec![1, 10_000_000]), 9_999_999);
    }
}
