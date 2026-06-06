fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
    let total: i32 = nums.iter().sum();
    let mut left = 0;
    let mut ans = Vec::with_capacity(nums.len());
    for x in nums {
        let right = total - left - x;
        ans.push((left - right).abs());
        left += x;
    }
    ans
}

fn main() {
    println!("{:?}", left_right_difference(vec![10, 4, 8, 3])); // [15, 1, 11, 22]
    println!("{:?}", left_right_difference(vec![1]));           // [0]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(left_right_difference(vec![10, 4, 8, 3]), vec![15, 1, 11, 22]);
        assert_eq!(left_right_difference(vec![1]), vec![0]);
    }
}
