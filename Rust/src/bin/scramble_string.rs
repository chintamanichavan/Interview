use std::collections::HashMap;

fn solve<'a>(a: &'a str, b: &'a str, memo: &mut HashMap<(&'a str, &'a str), bool>) -> bool {
    if a == b {
        return true;
    }
    if let Some(&v) = memo.get(&(a, b)) {
        return v;
    }
    // Anagram check.
    let mut cnt = [0i32; 26];
    for (x, y) in a.bytes().zip(b.bytes()) {
        cnt[(x - b'a') as usize] += 1;
        cnt[(y - b'a') as usize] -= 1;
    }
    if cnt.iter().any(|&c| c != 0) {
        memo.insert((a, b), false);
        return false;
    }
    let n = a.len();
    for i in 1..n {
        if (solve(&a[..i], &b[..i], memo) && solve(&a[i..], &b[i..], memo))
            || (solve(&a[..i], &b[n - i..], memo) && solve(&a[i..], &b[..n - i], memo))
        {
            memo.insert((a, b), true);
            return true;
        }
    }
    memo.insert((a, b), false);
    false
}

fn is_scramble(s1: String, s2: String) -> bool {
    let mut memo: HashMap<(&str, &str), bool> = HashMap::new();
    solve(&s1, &s2, &mut memo)
}

fn main() {
    println!("{}", is_scramble("great".into(), "rgeat".into())); // true
    println!("{}", is_scramble("abcde".into(), "caebd".into())); // false
    println!("{}", is_scramble("a".into(), "a".into()));         // true
    println!("{}", is_scramble("abc".into(), "bca".into()));     // true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert!(is_scramble("great".into(), "rgeat".into()));
        assert!(!is_scramble("abcde".into(), "caebd".into()));
        assert!(is_scramble("a".into(), "a".into()));
        assert!(is_scramble("abc".into(), "bca".into()));
    }
}
