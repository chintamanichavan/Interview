fn dfs(
    node: usize,
    time_left: i32,
    quality: i64,
    adj: &Vec<Vec<(usize, i32)>>,
    values: &Vec<i64>,
    visited: &mut Vec<i32>,
    best: &mut i64,
) {
    if node == 0 && quality > *best {
        *best = quality;
    }
    for &(to, cost) in &adj[node] {
        if cost <= time_left {
            let gain = if visited[to] == 0 { values[to] } else { 0 };
            visited[to] += 1;
            dfs(to, time_left - cost, quality + gain, adj, values, visited, best);
            visited[to] -= 1;
        }
    }
}

fn maximal_path_quality(values: Vec<i32>, edges: Vec<Vec<i32>>, max_time: i32) -> i32 {
    let n = values.len();
    let vals: Vec<i64> = values.iter().map(|&x| x as i64).collect();
    let mut adj: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n];
    for e in &edges {
        let (u, v, t) = (e[0] as usize, e[1] as usize, e[2]);
        adj[u].push((v, t));
        adj[v].push((u, t));
    }
    let mut visited = vec![0i32; n];
    let mut best = 0i64;
    visited[0] = 1;
    dfs(0, max_time, vals[0], &adj, &vals, &mut visited, &mut best);
    best as i32
}

fn main() {
    println!("{}", maximal_path_quality(vec![0, 32, 10, 43], vec![vec![0, 1, 10], vec![1, 2, 15], vec![0, 3, 10]], 49)); // 75
    println!("{}", maximal_path_quality(vec![5, 10, 15, 20], vec![vec![0, 1, 10], vec![1, 2, 10], vec![0, 3, 10]], 30)); // 25
    println!("{}", maximal_path_quality(vec![1, 2, 3, 4], vec![vec![0, 1, 10], vec![1, 2, 11], vec![2, 3, 12], vec![1, 3, 13]], 50)); // 7
    println!("{}", maximal_path_quality(vec![5], vec![], 100)); // 5
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(maximal_path_quality(vec![0, 32, 10, 43], vec![vec![0, 1, 10], vec![1, 2, 15], vec![0, 3, 10]], 49), 75);
        assert_eq!(maximal_path_quality(vec![5, 10, 15, 20], vec![vec![0, 1, 10], vec![1, 2, 10], vec![0, 3, 10]], 30), 25);
        assert_eq!(maximal_path_quality(vec![1, 2, 3, 4], vec![vec![0, 1, 10], vec![1, 2, 11], vec![2, 3, 12], vec![1, 3, 13]], 50), 7);
        assert_eq!(maximal_path_quality(vec![5], vec![], 100), 5);
    }
}
