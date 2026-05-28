const MOD: i64 = 1_000_000_007;

fn profitable_schemes(n: i32, min_profit: i32, group: Vec<i32>, profit: Vec<i32>) -> i32 {
    let n = n as usize;
    let mp = min_profit as usize;
    let mut dp = vec![vec![0i64; mp + 1]; n + 1];
    dp[0][0] = 1;
    for i in 0..group.len() {
        let g = group[i] as usize;
        let p = profit[i] as usize;
        for j in (g..=n).rev() {
            for k in (0..=mp).rev() {
                let v = dp[j - g][k];
                if v == 0 {
                    continue;
                }
                let nk = (k + p).min(mp);
                dp[j][nk] = (dp[j][nk] + v) % MOD;
            }
        }
    }
    let mut total: i64 = 0;
    for j in 0..=n {
        total = (total + dp[j][mp]) % MOD;
    }
    total as i32
}

fn main() {
    println!("{}", profitable_schemes(5, 3, vec![2, 2], vec![2, 3]));        // 2
    println!("{}", profitable_schemes(10, 5, vec![2, 3, 5], vec![6, 7, 8])); // 7
    println!("{}", profitable_schemes(1, 1, vec![1, 1], vec![1, 1]));        // 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(profitable_schemes(5, 3, vec![2, 2], vec![2, 3]), 2);
        assert_eq!(profitable_schemes(10, 5, vec![2, 3, 5], vec![6, 7, 8]), 7);
        assert_eq!(profitable_schemes(1, 1, vec![1, 1], vec![1, 1]), 2);
    }
}
