use std::collections::BinaryHeap;

fn get_skyline(buildings: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    // (x, neg_h, r): neg_h sorts starts (negative) before ends (0) at same x;
    // taller starts come first, which matters at coincident left edges.
    let mut events: Vec<(i32, i32, i32)> = Vec::with_capacity(buildings.len() * 2);
    for b in &buildings {
        let (l, r, h) = (b[0], b[1], b[2]);
        events.push((l, -h, r));
        events.push((r, 0, 0));
    }
    events.sort();

    // Max-heap on height; entries hold (h, end_x). Sentinel keeps it non-empty.
    let mut heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();
    heap.push((0, i32::MAX));

    let mut result: Vec<Vec<i32>> = Vec::new();
    for (x, neg_h, r) in events {
        if neg_h != 0 {
            heap.push((-neg_h, r));
        }
        while let Some(&(_, end)) = heap.peek() {
            if end <= x {
                heap.pop();
            } else {
                break;
            }
        }
        let cur_max = heap.peek().unwrap().0;
        if result.last().map_or(true, |last| last[1] != cur_max) {
            result.push(vec![x, cur_max]);
        }
    }
    result
}

fn main() {
    println!("{:?}", get_skyline(vec![vec![2, 9, 10], vec![3, 7, 15], vec![5, 12, 12], vec![15, 20, 10], vec![19, 24, 8]]));
    println!("{:?}", get_skyline(vec![vec![0, 2, 3], vec![2, 5, 3]]));
    println!("{:?}", get_skyline(vec![vec![1, 2, 1], vec![1, 2, 2], vec![1, 2, 3]]));
    println!("{:?}", get_skyline(vec![vec![0, 3, 3], vec![1, 5, 3], vec![2, 4, 3], vec![3, 7, 3]]));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            get_skyline(vec![vec![2, 9, 10], vec![3, 7, 15], vec![5, 12, 12], vec![15, 20, 10], vec![19, 24, 8]]),
            vec![vec![2, 10], vec![3, 15], vec![7, 12], vec![12, 0], vec![15, 10], vec![20, 8], vec![24, 0]]
        );
        assert_eq!(get_skyline(vec![vec![0, 2, 3], vec![2, 5, 3]]), vec![vec![0, 3], vec![5, 0]]);
    }
}
