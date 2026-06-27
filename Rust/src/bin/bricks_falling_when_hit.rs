struct Dsu {
    parent: Vec<usize>,
    size: Vec<i32>,
}

impl Dsu {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            size: vec![1; n],
        }
    }
    fn find(&mut self, mut x: usize) -> usize {
        while self.parent[x] != x {
            self.parent[x] = self.parent[self.parent[x]];
            x = self.parent[x];
        }
        x
    }
    fn union(&mut self, a: usize, b: usize) {
        let (ra, rb) = (self.find(a), self.find(b));
        if ra != rb {
            self.parent[ra] = rb;
            self.size[rb] += self.size[ra];
        }
    }
}

fn hit_bricks(grid: Vec<Vec<i32>>, hits: Vec<Vec<i32>>) -> Vec<i32> {
    let m = grid.len();
    let n = grid[0].len();
    let top = m * n;
    let idx = |r: usize, c: usize| r * n + c;
    let mut d = Dsu::new(m * n + 1);

    let mut g = grid.clone();
    for h in &hits {
        g[h[0] as usize][h[1] as usize] = 0;
    }

    for r in 0..m {
        for c in 0..n {
            if g[r][c] == 1 {
                if r == 0 {
                    d.union(idx(r, c), top);
                }
                if r > 0 && g[r - 1][c] == 1 {
                    d.union(idx(r, c), idx(r - 1, c));
                }
                if c > 0 && g[r][c - 1] == 1 {
                    d.union(idx(r, c), idx(r, c - 1));
                }
            }
        }
    }

    let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    let mut res = vec![0i32; hits.len()];
    for i in (0..hits.len()).rev() {
        let (r, c) = (hits[i][0] as usize, hits[i][1] as usize);
        if grid[r][c] == 0 {
            continue;
        }
        let troot = d.find(top);
        let before = d.size[troot];
        g[r][c] = 1;
        if r == 0 {
            d.union(idx(r, c), top);
        }
        for (dr, dc) in dirs {
            let nr = r as i32 + dr;
            let nc = c as i32 + dc;
            if nr >= 0
                && nr < m as i32
                && nc >= 0
                && nc < n as i32
                && g[nr as usize][nc as usize] == 1
            {
                d.union(idx(r, c), idx(nr as usize, nc as usize));
            }
        }
        let troot = d.find(top);
        let after = d.size[troot];
        res[i] = (after - before - 1).max(0);
    }
    res
}

fn main() {
    println!(
        "{:?}",
        hit_bricks(vec![vec![1, 0, 0, 0], vec![1, 1, 1, 0]], vec![vec![1, 0]])
    ); // [2]
    println!(
        "{:?}",
        hit_bricks(
            vec![vec![1, 0, 0, 0], vec![1, 1, 0, 0]],
            vec![vec![1, 1], vec![1, 0]]
        )
    ); // [0, 0]
    println!(
        "{:?}",
        hit_bricks(
            vec![vec![1, 1, 1], vec![0, 1, 0], vec![0, 0, 0]],
            vec![vec![0, 2], vec![2, 0], vec![0, 1], vec![1, 2]]
        )
    ); // [0, 0, 1, 0]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            hit_bricks(vec![vec![1, 0, 0, 0], vec![1, 1, 1, 0]], vec![vec![1, 0]]),
            vec![2]
        );
        assert_eq!(
            hit_bricks(
                vec![vec![1, 0, 0, 0], vec![1, 1, 0, 0]],
                vec![vec![1, 1], vec![1, 0]]
            ),
            vec![0, 0]
        );
        assert_eq!(
            hit_bricks(
                vec![vec![1, 1, 1], vec![0, 1, 0], vec![0, 0, 0]],
                vec![vec![0, 2], vec![2, 0], vec![0, 1], vec![1, 2]]
            ),
            vec![0, 0, 1, 0]
        );
    }
}
