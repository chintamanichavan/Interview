const EPS: f64 = 1e-6;

fn solve(nums: &[f64]) -> bool {
    let n = nums.len();
    if n == 1 {
        return (nums[0] - 24.0).abs() < EPS;
    }
    for i in 0..n {
        for j in 0..n {
            if i == j {
                continue;
            }
            let rest: Vec<f64> = (0..n)
                .filter(|&x| x != i && x != j)
                .map(|x| nums[x])
                .collect();
            let (a, b) = (nums[i], nums[j]);
            let mut cands = vec![a + b, a - b, a * b];
            if b.abs() > EPS {
                cands.push(a / b);
            }
            for val in cands {
                let mut next = rest.clone();
                next.push(val);
                if solve(&next) {
                    return true;
                }
            }
        }
    }
    false
}

fn judge_point24(cards: Vec<i32>) -> bool {
    let nums: Vec<f64> = cards.iter().map(|&c| c as f64).collect();
    solve(&nums)
}

fn main() {
    println!("{}", judge_point24(vec![4, 1, 8, 7])); // true
    println!("{}", judge_point24(vec![1, 2, 1, 2])); // false
    println!("{}", judge_point24(vec![3, 3, 8, 8])); // true
    println!("{}", judge_point24(vec![1, 1, 1, 1])); // false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert!(judge_point24(vec![4, 1, 8, 7]));
        assert!(!judge_point24(vec![1, 2, 1, 2]));
        assert!(judge_point24(vec![3, 3, 8, 8]));
        assert!(!judge_point24(vec![1, 1, 1, 1]));
    }
}
