use std::collections::VecDeque;

fn can_reach(arr: Vec<i32>, start: i32) -> bool {
    let n = arr.len();
    let mut seen = vec![false; n];
    let mut queue: VecDeque<usize> = VecDeque::new();
    let start = start as usize;
    queue.push_back(start);
    seen[start] = true;
    while let Some(i) = queue.pop_front() {
        if arr[i] == 0 {
            return true;
        }
        let step = arr[i];
        for &j in &[i as i32 + step, i as i32 - step] {
            if j >= 0 && (j as usize) < n && !seen[j as usize] {
                seen[j as usize] = true;
                queue.push_back(j as usize);
            }
        }
    }
    false
}

fn main() {
    println!("{}", can_reach(vec![4, 2, 3, 0, 3, 1, 2], 5)); // true
    println!("{}", can_reach(vec![4, 2, 3, 0, 3, 1, 2], 0)); // true
    println!("{}", can_reach(vec![3, 0, 2, 1, 2], 2));       // false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert!(can_reach(vec![4, 2, 3, 0, 3, 1, 2], 5));
        assert!(can_reach(vec![4, 2, 3, 0, 3, 1, 2], 0));
        assert!(!can_reach(vec![3, 0, 2, 1, 2], 2));
    }
}
