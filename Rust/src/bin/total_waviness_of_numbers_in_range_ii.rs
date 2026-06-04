struct Ctx {
    s: Vec<i64>,
    l: usize,
    visited: Vec<bool>,
    cnt: Vec<i64>,
    tot: Vec<i64>,
}

impl Ctx {
    fn idx(&self, pos: usize, started: usize, prev2: i64, prev1: i64) -> usize {
        // prev in -1..9 -> 0..10
        (((pos * 2 + started) * 11 + (prev2 + 1) as usize) * 11) + (prev1 + 1) as usize
    }

    fn dp(&mut self, pos: usize, started: bool, prev2: i64, prev1: i64, tight: bool) -> (i64, i64) {
        if pos == self.l {
            return (1, 0);
        }
        let si = started as usize;
        let key = self.idx(pos, si, prev2, prev1);
        if !tight && self.visited[key] {
            return (self.cnt[key], self.tot[key]);
        }
        let limit = if tight { self.s[pos] } else { 9 };
        let (mut cnt, mut tot) = (0i64, 0i64);
        for d in 0..=limit {
            let ntight = tight && d == limit;
            let (nstarted, np2, np1, event);
            if !started && d == 0 {
                nstarted = false;
                np2 = -1;
                np1 = -1;
                event = 0;
            } else {
                nstarted = true;
                event = if prev1 != -1
                    && prev2 != -1
                    && ((prev1 > prev2 && prev1 > d) || (prev1 < prev2 && prev1 < d))
                {
                    1
                } else {
                    0
                };
                np2 = prev1;
                np1 = d;
            }
            let (sc, st) = self.dp(pos + 1, nstarted, np2, np1, ntight);
            cnt += sc;
            tot += st + event * sc;
        }
        if !tight {
            self.visited[key] = true;
            self.cnt[key] = cnt;
            self.tot[key] = tot;
        }
        (cnt, tot)
    }
}

fn waviness_up_to(n: i64) -> i64 {
    if n < 0 {
        return 0;
    }
    let s: Vec<i64> = n.to_string().bytes().map(|b| (b - b'0') as i64).collect();
    let l = s.len();
    let size = (l + 1) * 2 * 11 * 11;
    let mut ctx = Ctx {
        s,
        l,
        visited: vec![false; size],
        cnt: vec![0; size],
        tot: vec![0; size],
    };
    ctx.dp(0, false, -1, -1, true).1
}

fn total_waviness(num1: i64, num2: i64) -> i64 {
    waviness_up_to(num2) - waviness_up_to(num1 - 1)
}

fn main() {
    println!("{}", total_waviness(120, 130));            // 3
    println!("{}", total_waviness(198, 202));            // 3
    println!("{}", total_waviness(4848, 4848));          // 2
    println!("{}", total_waviness(1, 1_000_000));        // 2230005
    println!("{}", total_waviness(1, 1_000_000_000_000_000)); // 7360000000000005
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(total_waviness(120, 130), 3);
        assert_eq!(total_waviness(198, 202), 3);
        assert_eq!(total_waviness(4848, 4848), 2);
        assert_eq!(total_waviness(1, 1_000_000), 2_230_005);
        assert_eq!(total_waviness(1, 1_000_000_000_000_000), 7_360_000_000_000_005);
    }
}
