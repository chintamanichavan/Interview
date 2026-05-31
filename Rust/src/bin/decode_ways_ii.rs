const MOD: i64 = 1_000_000_007;

fn one(c: u8) -> i64 {
    match c {
        b'*' => 9,
        b'0' => 0,
        _ => 1,
    }
}

fn two(c1: u8, c2: u8) -> i64 {
    match c1 {
        b'1' => if c2 == b'*' { 9 } else { 1 },
        b'2' => {
            if c2 == b'*' { 6 }
            else if (b'0'..=b'6').contains(&c2) { 1 }
            else { 0 }
        }
        b'*' => {
            if c2 == b'*' { 15 }
            else if (b'0'..=b'6').contains(&c2) { 2 }
            else { 1 }
        }
        _ => 0,
    }
}

fn num_decodings(s: String) -> i32 {
    let b = s.as_bytes();
    let (mut prev2, mut prev1) = (1i64, one(b[0]));
    for i in 1..b.len() {
        let cur = (one(b[i]) * prev1 + two(b[i - 1], b[i]) * prev2) % MOD;
        prev2 = prev1;
        prev1 = cur;
    }
    (prev1 % MOD) as i32
}

fn main() {
    println!("{}", num_decodings("*".to_string()));  // 9
    println!("{}", num_decodings("1*".to_string())); // 18
    println!("{}", num_decodings("2*".to_string())); // 15
    println!("{}", num_decodings("0".to_string()));  // 0
    println!("{}", num_decodings("**".to_string())); // 96
    println!("{}", num_decodings("*1".to_string())); // 11
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(num_decodings("*".to_string()), 9);
        assert_eq!(num_decodings("1*".to_string()), 18);
        assert_eq!(num_decodings("2*".to_string()), 15);
        assert_eq!(num_decodings("0".to_string()), 0);
        assert_eq!(num_decodings("**".to_string()), 96);
        assert_eq!(num_decodings("*1".to_string()), 11);
    }
}
