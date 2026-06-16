fn dfs(matrix: &Vec<Vec<i32>>, memo: &mut Vec<Vec<i32>>, r: usize, c: usize) -> i32 {
    if memo[r][c] != 0 {
        return memo[r][c];
    }
    let (m, n) = (matrix.len(), matrix[0].len());
    let mut best = 1;
    let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    for (dr, dc) in dirs {
        let nr = r as i32 + dr;
        let nc = c as i32 + dc;
        if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
            let (nr, nc) = (nr as usize, nc as usize);
            if matrix[nr][nc] > matrix[r][c] {
                best = best.max(1 + dfs(matrix, memo, nr, nc));
            }
        }
    }
    memo[r][c] = best;
    best
}

fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
    let (m, n) = (matrix.len(), matrix[0].len());
    let mut memo = vec![vec![0i32; n]; m];
    let mut ans = 0;
    for r in 0..m {
        for c in 0..n {
            ans = ans.max(dfs(&matrix, &mut memo, r, c));
        }
    }
    ans
}

fn main() {
    println!(
        "{}",
        longest_increasing_path(vec![vec![9, 9, 4], vec![6, 6, 8], vec![2, 1, 1]])
    ); // 4
    println!(
        "{}",
        longest_increasing_path(vec![vec![3, 4, 5], vec![3, 2, 6], vec![2, 2, 1]])
    ); // 4
    println!("{}", longest_increasing_path(vec![vec![1]])); // 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            longest_increasing_path(vec![vec![9, 9, 4], vec![6, 6, 8], vec![2, 1, 1]]),
            4
        );
        assert_eq!(
            longest_increasing_path(vec![vec![3, 4, 5], vec![3, 2, 6], vec![2, 2, 1]]),
            4
        );
        assert_eq!(longest_increasing_path(vec![vec![1]]), 1);
    }
}
