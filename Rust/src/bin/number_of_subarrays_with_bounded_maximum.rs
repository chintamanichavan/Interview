fn num_subarray_bounded_max(nums: Vec<i32>, left: i32, right: i32) -> i32 {
    let count = |bound: i32| -> i32 {
        let mut total = 0;
        let mut length = 0;
        for &x in &nums {
            length = if x <= bound { length + 1 } else { 0 };
            total += length;
        }
        total
    };
    count(right) - count(left - 1)
}

fn main() {
    println!("{}", num_subarray_bounded_max(vec![2, 1, 4, 3], 2, 3)); // 3
    println!("{}", num_subarray_bounded_max(vec![2, 9, 2, 5, 6], 2, 8)); // 7
    println!("{}", num_subarray_bounded_max(vec![1, 1, 1], 1, 1)); // 6
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(num_subarray_bounded_max(vec![2, 1, 4, 3], 2, 3), 3);
        assert_eq!(num_subarray_bounded_max(vec![2, 9, 2, 5, 6], 2, 8), 7);
        assert_eq!(num_subarray_bounded_max(vec![1, 1, 1], 1, 1), 6);
    }
}
