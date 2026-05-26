use std::collections::{HashSet, VecDeque};

fn sliding_puzzle(board: Vec<Vec<i32>>) -> i32 {
    const NEIGHBORS: [&[usize]; 6] = [
        &[1, 3],
        &[0, 2, 4],
        &[1, 5],
        &[0, 4],
        &[1, 3, 5],
        &[2, 4],
    ];
    let mut start = [0u8; 6];
    let mut zero = 0usize;
    for i in 0..2 {
        for j in 0..3 {
            let idx = i * 3 + j;
            start[idx] = b'0' + board[i][j] as u8;
            if board[i][j] == 0 {
                zero = idx;
            }
        }
    }
    let target = *b"123450";
    if start == target {
        return 0;
    }

    let mut queue: VecDeque<([u8; 6], usize, i32)> = VecDeque::new();
    let mut seen: HashSet<[u8; 6]> = HashSet::new();
    seen.insert(start);
    queue.push_back((start, zero, 0));
    while let Some((state, z, steps)) = queue.pop_front() {
        for &nb in NEIGHBORS[z] {
            let mut nxt = state;
            nxt.swap(z, nb);
            if nxt == target {
                return steps + 1;
            }
            if seen.insert(nxt) {
                queue.push_back((nxt, nb, steps + 1));
            }
        }
    }
    -1
}

fn main() {
    println!("{}", sliding_puzzle(vec![vec![1, 2, 3], vec![4, 0, 5]])); // 1
    println!("{}", sliding_puzzle(vec![vec![1, 2, 3], vec![5, 4, 0]])); // -1
    println!("{}", sliding_puzzle(vec![vec![4, 1, 2], vec![5, 0, 3]])); // 5
    println!("{}", sliding_puzzle(vec![vec![1, 2, 3], vec![4, 5, 0]])); // 0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(sliding_puzzle(vec![vec![1, 2, 3], vec![4, 0, 5]]), 1);
        assert_eq!(sliding_puzzle(vec![vec![1, 2, 3], vec![5, 4, 0]]), -1);
        assert_eq!(sliding_puzzle(vec![vec![4, 1, 2], vec![5, 0, 3]]), 5);
        assert_eq!(sliding_puzzle(vec![vec![1, 2, 3], vec![4, 5, 0]]), 0);
    }
}
