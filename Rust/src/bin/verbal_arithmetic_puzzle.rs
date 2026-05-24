struct Solver {
    rev_words: Vec<Vec<u8>>,
    rev_result: Vec<u8>,
    leading: [bool; 26],
    char_digit: [i32; 26],
    used: [bool; 10],
}

const UNSET: i32 = -1;

impl Solver {
    fn dfs(&mut self, col: usize, idx: usize, carry: i32) -> bool {
        if col == self.rev_result.len() {
            return carry == 0;
        }
        if idx < self.rev_words.len() {
            let w = &self.rev_words[idx];
            if col >= w.len() || self.char_digit[(w[col] - b'A') as usize] != UNSET {
                return self.dfs(col, idx + 1, carry);
            }
            let ch = (w[col] - b'A') as usize;
            for d in 0..10 {
                if self.used[d] || (d == 0 && self.leading[ch]) {
                    continue;
                }
                self.char_digit[ch] = d as i32;
                self.used[d] = true;
                if self.dfs(col, idx + 1, carry) {
                    return true;
                }
                self.char_digit[ch] = UNSET;
                self.used[d] = false;
            }
            return false;
        }

        let mut col_sum = carry;
        for w in &self.rev_words {
            if col < w.len() {
                col_sum += self.char_digit[(w[col] - b'A') as usize];
            }
        }
        let digit = (col_sum % 10) as usize;
        let next_carry = col_sum / 10;
        let r_ch = (self.rev_result[col] - b'A') as usize;
        if self.char_digit[r_ch] != UNSET {
            if self.char_digit[r_ch] as usize != digit {
                return false;
            }
            return self.dfs(col + 1, 0, next_carry);
        }
        if self.used[digit] || (digit == 0 && self.leading[r_ch]) {
            return false;
        }
        self.char_digit[r_ch] = digit as i32;
        self.used[digit] = true;
        if self.dfs(col + 1, 0, next_carry) {
            return true;
        }
        self.char_digit[r_ch] = UNSET;
        self.used[digit] = false;
        false
    }
}

fn is_solvable(words: Vec<String>, result: String) -> bool {
    let max_len = words.iter().map(|w| w.len()).max().unwrap_or(0);
    if max_len > result.len() {
        return false;
    }
    let rev_words: Vec<Vec<u8>> = words
        .iter()
        .map(|w| w.bytes().rev().collect())
        .collect();
    let rev_result: Vec<u8> = result.bytes().rev().collect();

    let mut leading = [false; 26];
    for w in &words {
        if w.len() > 1 {
            leading[(w.as_bytes()[0] - b'A') as usize] = true;
        }
    }
    if result.len() > 1 {
        leading[(result.as_bytes()[0] - b'A') as usize] = true;
    }

    let mut solver = Solver {
        rev_words,
        rev_result,
        leading,
        char_digit: [UNSET; 26],
        used: [false; 10],
    };
    solver.dfs(0, 0, 0)
}

fn s(strs: &[&str]) -> Vec<String> {
    strs.iter().map(|x| x.to_string()).collect()
}

fn main() {
    println!("{}", is_solvable(s(&["SEND", "MORE"]), "MONEY".to_string()));            // true
    println!("{}", is_solvable(s(&["SIX", "SEVEN", "SEVEN"]), "TWENTY".to_string()));  // true
    println!("{}", is_solvable(s(&["LEET", "CODE"]), "POINT".to_string()));            // false
    println!("{}", is_solvable(s(&["A", "B"]), "C".to_string()));                      // true
    println!("{}", is_solvable(s(&["ACA"]), "JA".to_string()));                        // false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert!(is_solvable(s(&["SEND", "MORE"]), "MONEY".to_string()));
        assert!(is_solvable(s(&["SIX", "SEVEN", "SEVEN"]), "TWENTY".to_string()));
        assert!(!is_solvable(s(&["LEET", "CODE"]), "POINT".to_string()));
        assert!(is_solvable(s(&["A", "B"]), "C".to_string()));
        assert!(!is_solvable(s(&["ACA"]), "JA".to_string()));
    }
}
