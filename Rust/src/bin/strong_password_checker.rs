fn strong_password_checker(password: String) -> i32 {
    let b = password.as_bytes();
    let n = b.len() as i32;
    let (mut has_lower, mut has_upper, mut has_digit) = (false, false, false);
    for &c in b {
        match c {
            b'a'..=b'z' => has_lower = true,
            b'A'..=b'Z' => has_upper = true,
            b'0'..=b'9' => has_digit = true,
            _ => {}
        }
    }
    let mut missing_type = 3;
    if has_lower {
        missing_type -= 1;
    }
    if has_upper {
        missing_type -= 1;
    }
    if has_digit {
        missing_type -= 1;
    }

    // Runs of >= 3 equal chars: L/3 replacements each. Bucket by L%3 for the >20 deletion case.
    let (mut change, mut one, mut two) = (0i32, 0i32, 0i32);
    let mut i = 2usize;
    while i < b.len() {
        if b[i] == b[i - 1] && b[i - 1] == b[i - 2] {
            let mut length = 2i32;
            while i < b.len() && b[i] == b[i - 1] {
                length += 1;
                i += 1;
            }
            change += length / 3;
            match length % 3 {
                0 => one += 1,
                1 => two += 1,
                _ => {}
            }
        } else {
            i += 1;
        }
    }

    if n < 6 {
        return (6 - n).max(missing_type);
    }
    if n <= 20 {
        return change.max(missing_type);
    }

    let del = n - 20;
    change -= del.min(one);
    change -= (del - one).max(0).min(two * 2) / 2;
    change -= (del - one - two * 2).max(0) / 3;
    del + change.max(missing_type)
}

fn main() {
    println!("{}", strong_password_checker("a".into()));                         // 5
    println!("{}", strong_password_checker("aA1".into()));                       // 3
    println!("{}", strong_password_checker("1337C0d3".into()));                  // 0
    println!("{}", strong_password_checker("aaa123".into()));                    // 1
    println!("{}", strong_password_checker("aaaaa".into()));                     // 2
    println!("{}", strong_password_checker("1111111111".into()));               // 3
    println!("{}", strong_password_checker("aaaabbaaabbaaabbaaabbaaaa".into())); // 7
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(strong_password_checker("a".into()), 5);
        assert_eq!(strong_password_checker("aA1".into()), 3);
        assert_eq!(strong_password_checker("1337C0d3".into()), 0);
        assert_eq!(strong_password_checker("aaa123".into()), 1);
        assert_eq!(strong_password_checker("aaaaa".into()), 2);
        assert_eq!(strong_password_checker("1111111111".into()), 3);
        assert_eq!(strong_password_checker("aaaabbaaabbaaabbaaabbaaaa".into()), 7);
    }
}
