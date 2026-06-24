use std::collections::HashSet;

fn dfs(node: String, k: i32, seen: &mut HashSet<String>, path: &mut String) {
    for d in 0..k {
        let edge = format!("{}{}", node, d);
        if !seen.contains(&edge) {
            seen.insert(edge.clone());
            dfs(edge[1..].to_string(), k, seen, path);
            path.push_str(&d.to_string());
        }
    }
}

fn crack_safe(n: i32, k: i32) -> String {
    if n == 1 {
        return (0..k).map(|d| d.to_string()).collect();
    }
    let start: String = "0".repeat((n - 1) as usize);
    let mut seen: HashSet<String> = HashSet::new();
    let mut path = String::new();
    dfs(start.clone(), k, &mut seen, &mut path);
    path.push_str(&start);
    path
}

fn main() {
    println!("{}", crack_safe(1, 2)); // 01
    println!("{}", crack_safe(2, 2)); // 01100
    println!("{}", crack_safe(3, 2)); // 0011101000
    println!("{}", crack_safe(2, 3)); // 0221120100
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(crack_safe(1, 2), "01");
        assert_eq!(crack_safe(2, 2), "01100");
        assert_eq!(crack_safe(3, 2), "0011101000");
        assert_eq!(crack_safe(2, 3), "0221120100");
        // de Bruijn length is k^n + (n - 1)
        for (n, k) in [(2u32, 2i32), (3, 2), (2, 3)] {
            assert_eq!(
                crack_safe(n as i32, k).len(),
                (k.pow(n) as usize) + n as usize - 1
            );
        }
    }
}
