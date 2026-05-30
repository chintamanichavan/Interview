fn asteroids_destroyed(mass: i32, mut asteroids: Vec<i32>) -> bool {
    asteroids.sort_unstable();
    // Sum of asteroids can reach 1e10, so accumulate in i64.
    let mut m = mass as i64;
    for a in asteroids {
        if m < a as i64 {
            return false;
        }
        m += a as i64;
    }
    true
}

fn main() {
    println!("{}", asteroids_destroyed(10, vec![3, 9, 19, 5, 21])); // true
    println!("{}", asteroids_destroyed(5, vec![4, 9, 23, 4]));      // false
    println!("{}", asteroids_destroyed(1, vec![1]));                // true
    println!("{}", asteroids_destroyed(1, vec![2]));                // false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert!(asteroids_destroyed(10, vec![3, 9, 19, 5, 21]));
        assert!(!asteroids_destroyed(5, vec![4, 9, 23, 4]));
        assert!(asteroids_destroyed(1, vec![1]));
        assert!(!asteroids_destroyed(1, vec![2]));
    }
}
