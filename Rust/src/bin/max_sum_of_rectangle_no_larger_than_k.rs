use std::collections::BTreeSet;

fn max_sum_submatrix(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
    let m = matrix.len();
    let n = matrix[0].len();
    let k = k as i64;
    let mut best = i64::MIN;
    for left in 0..n {
        let mut rowsum = vec![0i64; m];
        for right in left..n {
            for i in 0..m {
                rowsum[i] += matrix[i][right] as i64;
            }
            // ordered prefix sums; smallest stored prefix >= cur - k
            let mut prefixes: BTreeSet<i64> = BTreeSet::new();
            prefixes.insert(0);
            let mut cur = 0i64;
            for &v in &rowsum {
                cur += v;
                if let Some(&p) = prefixes.range((cur - k)..).next() {
                    best = best.max(cur - p);
                }
                prefixes.insert(cur);
            }
        }
    }
    best as i32
}

fn main() {
    println!(
        "{}",
        max_sum_submatrix(vec![vec![1, 0, 1], vec![0, -2, 3]], 2)
    ); // 2
    println!("{}", max_sum_submatrix(vec![vec![2, 2, -1]], 3)); // 3
    println!("{}", max_sum_submatrix(vec![vec![2, 2, -1]], 0)); // -1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(max_sum_submatrix(vec![vec![1, 0, 1], vec![0, -2, 3]], 2), 2);
        assert_eq!(max_sum_submatrix(vec![vec![2, 2, -1]], 3), 3);
        assert_eq!(max_sum_submatrix(vec![vec![2, 2, -1]], 0), -1);
    }
}
