use std::collections::HashSet;

fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
    let mut prefixes: HashSet<i32> = HashSet::new();
    for mut x in arr1 {
        while x > 0 {
            prefixes.insert(x);
            x /= 10;
        }
    }

    let mut best = 0;
    for mut y in arr2 {
        while y > 0 {
            if prefixes.contains(&y) {
                best = best.max(digits(y));
                break;
            }
            y /= 10;
        }
    }
    best
}

fn digits(mut n: i32) -> i32 {
    let mut d = 0;
    while n > 0 {
        d += 1;
        n /= 10;
    }
    d
}

fn main() {
    println!("{}", longest_common_prefix(vec![1, 10, 100], vec![1000])); // 3
    println!("{}", longest_common_prefix(vec![1, 2, 3], vec![4, 4, 4])); // 0
    println!("{}", longest_common_prefix(vec![1], vec![1]));             // 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(longest_common_prefix(vec![1, 10, 100], vec![1000]), 3);
        assert_eq!(longest_common_prefix(vec![1, 2, 3], vec![4, 4, 4]), 0);
        assert_eq!(longest_common_prefix(vec![1], vec![1]), 1);
    }
}
