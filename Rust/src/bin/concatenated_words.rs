use std::collections::HashSet;

fn find_all_concatenated_words_in_a_dict(words: Vec<String>) -> Vec<String> {
    let set: HashSet<&str> = words.iter().map(|s| s.as_str()).collect();

    let can_form = |word: &str| -> bool {
        let n = word.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;
        for i in 1..=n {
            for j in 0..i {
                if !dp[j] || (j == 0 && i == n) {
                    continue;
                }
                if set.contains(&word[j..i]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        dp[n]
    };

    words
        .iter()
        .filter(|w| !w.is_empty() && can_form(w))
        .cloned()
        .collect()
}

fn main() {
    let v = |xs: &[&str]| xs.iter().map(|s| s.to_string()).collect::<Vec<_>>();
    println!(
        "{:?}",
        find_all_concatenated_words_in_a_dict(v(&[
            "cat",
            "cats",
            "catsdogcats",
            "dog",
            "dogcatsdog",
            "hippopotamuses",
            "rat",
            "ratcatdogcat"
        ]))
    );
    println!(
        "{:?}",
        find_all_concatenated_words_in_a_dict(v(&["cat", "dog", "catdog"]))
    );
    println!(
        "{:?}",
        find_all_concatenated_words_in_a_dict(v(&["a", "b", "ab", "abc"]))
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    fn v(xs: &[&str]) -> Vec<String> {
        xs.iter().map(|s| s.to_string()).collect()
    }

    #[test]
    fn examples() {
        assert_eq!(
            find_all_concatenated_words_in_a_dict(v(&[
                "cat",
                "cats",
                "catsdogcats",
                "dog",
                "dogcatsdog",
                "hippopotamuses",
                "rat",
                "ratcatdogcat"
            ])),
            v(&["catsdogcats", "dogcatsdog", "ratcatdogcat"])
        );
        assert_eq!(
            find_all_concatenated_words_in_a_dict(v(&["cat", "dog", "catdog"])),
            v(&["catdog"])
        );
        assert_eq!(
            find_all_concatenated_words_in_a_dict(v(&["a", "b", "ab", "abc"])),
            v(&["ab"])
        );
    }
}
