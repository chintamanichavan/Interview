use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn smallest_range(nums: Vec<Vec<i32>>) -> Vec<i32> {
    let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
    let mut cur_max = i32::MIN;
    for (i, row) in nums.iter().enumerate() {
        heap.push(Reverse((row[0], i, 0)));
        cur_max = cur_max.max(row[0]);
    }
    let mut best = vec![heap.peek().unwrap().0 .0, cur_max];
    loop {
        let Reverse((val, i, j)) = heap.pop().unwrap();
        if cur_max - val < best[1] - best[0] {
            best = vec![val, cur_max];
        }
        if j + 1 == nums[i].len() {
            break;
        }
        let nxt = nums[i][j + 1];
        cur_max = cur_max.max(nxt);
        heap.push(Reverse((nxt, i, j + 1)));
    }
    best
}

fn main() {
    println!(
        "{:?}",
        smallest_range(vec![
            vec![4, 10, 15, 24, 26],
            vec![0, 9, 12, 20],
            vec![5, 18, 22, 30]
        ])
    ); // [20, 24]
    println!(
        "{:?}",
        smallest_range(vec![vec![1, 2, 3], vec![1, 2, 3], vec![1, 2, 3]])
    ); // [1, 1]
    println!("{:?}", smallest_range(vec![vec![1], vec![2], vec![3]])); // [1, 3]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            smallest_range(vec![
                vec![4, 10, 15, 24, 26],
                vec![0, 9, 12, 20],
                vec![5, 18, 22, 30]
            ]),
            vec![20, 24]
        );
        assert_eq!(
            smallest_range(vec![vec![1, 2, 3], vec![1, 2, 3], vec![1, 2, 3]]),
            vec![1, 1]
        );
        assert_eq!(smallest_range(vec![vec![1], vec![2], vec![3]]), vec![1, 3]);
    }
}
