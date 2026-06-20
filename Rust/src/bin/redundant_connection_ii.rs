fn find(uf: &mut Vec<usize>, mut x: usize) -> usize {
    while uf[x] != x {
        uf[x] = uf[uf[x]];
        x = uf[x];
    }
    x
}

fn find_redundant_directed_connection(mut edges: Vec<Vec<i32>>) -> Vec<i32> {
    let n = edges.len();
    let mut parent = vec![0i32; n + 1];
    let mut cand1: Option<Vec<i32>> = None;
    let mut cand2: Option<Vec<i32>> = None;
    for i in 0..n {
        let (u, v) = (edges[i][0], edges[i][1]);
        if parent[v as usize] != 0 {
            cand1 = Some(vec![parent[v as usize], v]);
            cand2 = Some(vec![u, v]);
            edges[i][1] = 0; // disable cand2 in the union pass
        } else {
            parent[v as usize] = u;
        }
    }

    let mut uf: Vec<usize> = (0..=n).collect();
    for e in &edges {
        let (u, v) = (e[0], e[1]);
        if v == 0 {
            continue;
        }
        let (ru, rv) = (find(&mut uf, u as usize), find(&mut uf, v as usize));
        if ru == rv {
            return cand1.unwrap_or_else(|| vec![u, v]);
        }
        uf[rv] = ru;
    }
    cand2.unwrap()
}

fn main() {
    println!(
        "{:?}",
        find_redundant_directed_connection(vec![vec![1, 2], vec![1, 3], vec![2, 3]])
    ); // [2, 3]
    println!(
        "{:?}",
        find_redundant_directed_connection(vec![
            vec![1, 2],
            vec![2, 3],
            vec![3, 4],
            vec![4, 1],
            vec![1, 5]
        ])
    ); // [4, 1]
    println!(
        "{:?}",
        find_redundant_directed_connection(vec![vec![2, 1], vec![3, 1], vec![4, 2], vec![1, 4]])
    ); // [2, 1]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            find_redundant_directed_connection(vec![vec![1, 2], vec![1, 3], vec![2, 3]]),
            vec![2, 3]
        );
        assert_eq!(
            find_redundant_directed_connection(vec![
                vec![1, 2],
                vec![2, 3],
                vec![3, 4],
                vec![4, 1],
                vec![1, 5]
            ]),
            vec![4, 1]
        );
        assert_eq!(
            find_redundant_directed_connection(vec![
                vec![2, 1],
                vec![3, 1],
                vec![4, 2],
                vec![1, 4]
            ]),
            vec![2, 1]
        );
    }
}
