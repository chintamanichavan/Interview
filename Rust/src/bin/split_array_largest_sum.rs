fn split_array(nums: Vec<i32>, k: i32) -> i32 {
    let needed = |cap: i64| -> i32 {
        let mut count = 1;
        let mut cur = 0i64;
        for &x in &nums {
            if cur + x as i64 > cap {
                count += 1;
                cur = x as i64;
            } else {
                cur += x as i64;
            }
        }
        count
    };

    let mut lo = *nums.iter().max().unwrap() as i64;
    let mut hi = nums.iter().map(|&x| x as i64).sum();
    while lo < hi {
        let mid = (lo + hi) / 2;
        if needed(mid) <= k {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    lo as i32
}

fn main() {
    println!("{}", split_array(vec![7, 2, 5, 10, 8], 2)); // 18
    println!("{}", split_array(vec![1, 2, 3, 4, 5], 2)); // 9
    println!("{}", split_array(vec![1, 4, 4], 3)); // 4
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(split_array(vec![7, 2, 5, 10, 8], 2), 18);
        assert_eq!(split_array(vec![1, 2, 3, 4, 5], 2), 9);
        assert_eq!(split_array(vec![1, 4, 4], 3), 4);
    }
}
