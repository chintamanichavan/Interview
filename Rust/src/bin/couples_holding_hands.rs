use std::collections::HashMap;

fn min_swaps_couples(mut row: Vec<i32>) -> i32 {
    let n = row.len();
    let mut pos: HashMap<i32, usize> = row.iter().enumerate().map(|(i, &p)| (p, i)).collect();
    let mut swaps = 0;
    for i in (0..n).step_by(2) {
        let partner = row[i] ^ 1;
        if row[i + 1] == partner {
            continue;
        }
        let j = pos[&partner];
        row.swap(i + 1, j);
        pos.insert(row[j], j);
        pos.insert(row[i + 1], i + 1);
        swaps += 1;
    }
    swaps
}

fn main() {
    println!("{}", min_swaps_couples(vec![0, 2, 1, 3]));             // 1
    println!("{}", min_swaps_couples(vec![3, 2, 0, 1]));             // 0
    println!("{}", min_swaps_couples(vec![0, 2, 4, 1, 3, 5]));       // 2
    println!("{}", min_swaps_couples(vec![5, 4, 2, 6, 3, 1, 0, 7])); // 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(min_swaps_couples(vec![0, 2, 1, 3]), 1);
        assert_eq!(min_swaps_couples(vec![3, 2, 0, 1]), 0);
        assert_eq!(min_swaps_couples(vec![0, 2, 4, 1, 3, 5]), 2);
        assert_eq!(min_swaps_couples(vec![5, 4, 2, 6, 3, 1, 0, 7]), 2);
    }
}
