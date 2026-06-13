use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
    let n = grid.len();
    let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
    let mut seen = vec![vec![false; n]; n];
    heap.push(Reverse((grid[0][0], 0, 0)));
    let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    while let Some(Reverse((t, r, c))) = heap.pop() {
        if r == n - 1 && c == n - 1 {
            return t;
        }
        if seen[r][c] {
            continue;
        }
        seen[r][c] = true;
        for (dr, dc) in dirs {
            let nr = r as i32 + dr;
            let nc = c as i32 + dc;
            if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {
                let (nr, nc) = (nr as usize, nc as usize);
                if !seen[nr][nc] {
                    heap.push(Reverse((t.max(grid[nr][nc]), nr, nc)));
                }
            }
        }
    }
    -1
}

fn main() {
    println!("{}", swim_in_water(vec![vec![0, 2], vec![1, 3]])); // 3
    println!(
        "{}",
        swim_in_water(vec![
            vec![0, 1, 2, 3, 4],
            vec![24, 23, 22, 21, 5],
            vec![12, 13, 14, 15, 16],
            vec![11, 17, 18, 19, 20],
            vec![10, 9, 8, 7, 6]
        ])
    ); // 16
    println!("{}", swim_in_water(vec![vec![0]])); // 0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(swim_in_water(vec![vec![0, 2], vec![1, 3]]), 3);
        assert_eq!(
            swim_in_water(vec![
                vec![0, 1, 2, 3, 4],
                vec![24, 23, 22, 21, 5],
                vec![12, 13, 14, 15, 16],
                vec![11, 17, 18, 19, 20],
                vec![10, 9, 8, 7, 6]
            ]),
            16
        );
        assert_eq!(swim_in_water(vec![vec![0]]), 0);
    }
}
