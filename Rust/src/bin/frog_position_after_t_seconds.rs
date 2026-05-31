fn dfs(
    adj: &Vec<Vec<usize>>,
    visited: &mut Vec<bool>,
    target: usize,
    t: i32,
    node: usize,
    time: i32,
    prob: f64,
) -> f64 {
    let children: Vec<usize> = adj[node].iter().copied().filter(|&v| !visited[v]).collect();
    if node == target {
        return if time == t || children.is_empty() { prob } else { 0.0 };
    }
    if time == t || children.is_empty() {
        return 0.0;
    }
    let p = prob / children.len() as f64;
    for c in children {
        visited[c] = true;
        let res = dfs(adj, visited, target, t, c, time + 1, p);
        if res > 0.0 {
            return res;
        }
    }
    0.0
}

fn frog_position(n: i32, edges: Vec<Vec<i32>>, t: i32, target: i32) -> f64 {
    let n = n as usize;
    let mut adj = vec![Vec::new(); n + 1];
    for e in &edges {
        let (a, b) = (e[0] as usize, e[1] as usize);
        adj[a].push(b);
        adj[b].push(a);
    }
    let mut visited = vec![false; n + 1];
    visited[1] = true;
    dfs(&adj, &mut visited, target as usize, t, 1, 0, 1.0)
}

fn main() {
    let edges = vec![vec![1, 2], vec![1, 3], vec![1, 7], vec![2, 4], vec![2, 6], vec![3, 5]];
    println!("{}", frog_position(7, edges.clone(), 2, 4));   // 0.1666...
    println!("{}", frog_position(7, edges.clone(), 1, 7));   // 0.3333...
    println!("{}", frog_position(7, edges, 20, 6));          // 0.1666...
    println!("{}", frog_position(1, vec![], 1, 1));          // 1.0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        let edges = vec![vec![1, 2], vec![1, 3], vec![1, 7], vec![2, 4], vec![2, 6], vec![3, 5]];
        assert!((frog_position(7, edges.clone(), 2, 4) - 1.0 / 6.0).abs() < 1e-9);
        assert!((frog_position(7, edges.clone(), 1, 7) - 1.0 / 3.0).abs() < 1e-9);
        assert!((frog_position(7, edges, 20, 6) - 1.0 / 6.0).abs() < 1e-9);
        assert!((frog_position(1, vec![], 1, 1) - 1.0).abs() < 1e-9);
    }
}
