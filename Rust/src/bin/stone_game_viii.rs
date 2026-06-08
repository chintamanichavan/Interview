fn stone_game_viii(stones: Vec<i32>) -> i32 {
    let n = stones.len();
    let mut prefix = vec![0i64; n];
    let mut sum = 0i64;
    for (i, &v) in stones.iter().enumerate() {
        sum += v as i64;
        prefix[i] = sum;
    }
    let mut dp = prefix[n - 1];
    for i in (1..n - 1).rev() {
        dp = dp.max(prefix[i] - dp);
    }
    dp as i32
}

fn main() {
    println!("{}", stone_game_viii(vec![-1, 2, -3, 4, -5]));        // 5
    println!("{}", stone_game_viii(vec![7, -6, 5, 10, 5, -2, -6])); // 13
    println!("{}", stone_game_viii(vec![-10, -12]));                // -22
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(stone_game_viii(vec![-1, 2, -3, 4, -5]), 5);
        assert_eq!(stone_game_viii(vec![7, -6, 5, 10, 5, -2, -6]), 13);
        assert_eq!(stone_game_viii(vec![-10, -12]), -22);
    }
}
