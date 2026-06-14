fn min_window(s1: String, s2: String) -> String {
    let a = s1.as_bytes();
    let b = s2.as_bytes();
    let (m, n) = (a.len() as i64, b.len() as i64);
    let mut i: i64 = 0;
    let mut j: i64 = 0;
    let mut start: i64 = -1;
    let mut best = m + 1;
    while i < m {
        if a[i as usize] == b[j as usize] {
            j += 1;
            if j == n {
                let right = i;
                j -= 1;
                while j >= 0 {
                    if a[i as usize] == b[j as usize] {
                        j -= 1;
                    }
                    i -= 1;
                }
                i += 1; // left end
                if right - i + 1 < best {
                    best = right - i + 1;
                    start = i;
                }
                j = 0;
            }
        }
        i += 1;
    }
    if start == -1 {
        String::new()
    } else {
        s1[start as usize..(start + best) as usize].to_string()
    }
}

fn main() {
    println!("{}", min_window("abcdebdde".into(), "bde".into())); // bcde
    println!("{}", min_window("abc".into(), "ac".into())); // abc
    println!("{}", min_window("abcde".into(), "xyz".into())); // (empty)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(min_window("abcdebdde".into(), "bde".into()), "bcde");
        assert_eq!(min_window("abc".into(), "ac".into()), "abc");
        assert_eq!(min_window("abcde".into(), "xyz".into()), "");
    }
}
