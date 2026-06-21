use std::collections::HashSet;

fn pow10(e: usize) -> i64 {
    let mut r = 1i64;
    for _ in 0..e {
        r *= 10;
    }
    r
}

fn rev(s: &str) -> String {
    s.chars().rev().collect()
}

fn nearest_palindromic(n: String) -> String {
    let length = n.len();
    let num: i64 = n.parse().unwrap();
    let mut cands: HashSet<i64> = HashSet::new();
    cands.insert(pow10(length - 1) - 1);
    cands.insert(pow10(length) + 1);

    let prefix: i64 = n[..(length + 1) / 2].parse().unwrap();
    for p in [prefix - 1, prefix, prefix + 1] {
        let s = p.to_string();
        let cand = if length % 2 == 0 {
            format!("{}{}", s, rev(&s))
        } else {
            format!("{}{}", s, rev(&s[..s.len() - 1]))
        };
        cands.insert(cand.parse().unwrap());
    }
    cands.remove(&num);

    let mut best: i64 = -1;
    for &c in &cands {
        if c < 0 {
            continue;
        }
        if best == -1
            || (c - num).abs() < (best - num).abs()
            || ((c - num).abs() == (best - num).abs() && c < best)
        {
            best = c;
        }
    }
    best.to_string()
}

fn main() {
    for t in ["123", "1", "10", "1000", "999"] {
        println!("{}", nearest_palindromic(t.to_string())); // 121, 0, 9, 999, 1001
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(nearest_palindromic("123".into()), "121");
        assert_eq!(nearest_palindromic("1".into()), "0");
        assert_eq!(nearest_palindromic("10".into()), "9");
        assert_eq!(nearest_palindromic("1000".into()), "999");
        assert_eq!(nearest_palindromic("999".into()), "1001");
    }
}
