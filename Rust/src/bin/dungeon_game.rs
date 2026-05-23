fn calculate_minimum_hp(dungeon: Vec<Vec<i32>>) -> i32 {
    let m = dungeon.len();
    let n = dungeon[0].len();
    let mut dp = vec![i32::MAX; n + 1];
    dp[n - 1] = 1;
    for i in (0..m).rev() {
        for j in (0..n).rev() {
            let need = dp[j].min(dp[j + 1]) - dungeon[i][j];
            dp[j] = need.max(1);
        }
    }
    dp[0]
}

fn main() {
    println!("{}", calculate_minimum_hp(vec![vec![-2, -3, 3], vec![-5, -10, 1], vec![10, 30, -5]])); // 7
    println!("{}", calculate_minimum_hp(vec![vec![0]]));    // 1
    println!("{}", calculate_minimum_hp(vec![vec![100]]));  // 1
    println!("{}", calculate_minimum_hp(vec![vec![-3]]));   // 4
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            calculate_minimum_hp(vec![vec![-2, -3, 3], vec![-5, -10, 1], vec![10, 30, -5]]),
            7
        );
        assert_eq!(calculate_minimum_hp(vec![vec![0]]), 1);
        assert_eq!(calculate_minimum_hp(vec![vec![100]]), 1);
        assert_eq!(calculate_minimum_hp(vec![vec![-3]]), 4);
    }
}
